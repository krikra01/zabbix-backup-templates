import requests
import json
import logging
import zabbix
import settings
import os

# Конфиг для логирования
logging.basicConfig(filename="template-status.log", datefmt='%d-%b-%y %H:%M:%S', filemode='a', level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s - %(funcName)s: %(message)s', )

url = 'https://{0}/api_jsonrpc.php'.format(settings.ZABBIX_URL)
headers = {'Content-type': 'application/json'}
path = '{0}'.format(settings.TEMPLATES_PATH)


# Вызов функции содержащую словарь с запросом всех шаблонов заббикса
payload_template = zabbix.payload_all_template()

# Построение запроса на получение всех шаблонов на сервер с преобразованием словаря в json
response_all_template = requests.request("POST", url, data=json.dumps(payload_template), headers=headers)

try:
    # Перебор всех элементов пришедших запросом response_all_template, где:
    # host - имя шаблона в БД (без спецсимволов, используется для именования .xml файлов),
    # templateid - id шаблона который необходим для иморта
    try:
        os.mkdir(path)
        logging.info("The folder created")
    except OSError:
        logging.info("The folder already exists")

    for template in response_all_template.json()["result"]:
        template_name = template["host"]
        template_id = template["templateid"]
        # Создаем и называем файл .xml по имени шаблона
        template_file = open('./templates/{0}.xml'.format(template_name), "w+")
        # Функция из файла zabbix.py в которую аргументом передается id пришедшего шаблона, функция позволяет подготовить данные для экспорта
        payload_export_template = zabbix.payload_all_export(template_id)

        # Построение запроса на экспорт
        response_export_template = requests.request("POST", url, data=json.dumps(payload_export_template), headers=headers)

        # Перебор пришедшего шаблона для экспорта и запись xml файла *поле result уже содержит готовый чистый xml*
        for export in response_export_template.json()["result"]:
            template_file.write(export)
        template_file.close()
        logging.info("id: {0} host: {1} | Backup succeed".format(template_id, template_name))
except BaseException:
    logging.critical("Failed fetch dict on step - request all template")
    logging.error("Backup Failed")
