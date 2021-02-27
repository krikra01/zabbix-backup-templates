import requests
import json
import logging
import zabbix
import settings
import os

logging.basicConfig(filename="template-status.log", datefmt='%d-%b-%y %H:%M:%S', filemode='a', level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s - %(funcName)s: %(message)s', )

response_all_template = requests.request("POST", settings.ZABBIX_URL, data=json.dumps(zabbix.payload_all_template()), headers=settings.HEADERS)

try:
    try:
        os.mkdir(settings.TEMPLATES_PATH)
        logging.info("The folder created")
    except OSError:
        logging.info("The folder already exists")

    for template in response_all_template.json()["result"]:
        template_name = template["host"]
        template_id = template["templateid"]

        template_file = open('./templates/{0}.xml'.format(template_name), "w+")

        response_export_template = requests.request("POST", settings.ZABBIX_URL,
                                                    data=json.dumps(zabbix.payload_all_export(template_id)),
                                                    headers=settings.HEADERS)

        for export in response_export_template.json()["result"]:
            template_file.write(export)
        template_file.close()
        logging.info("id: {0} host: {1} | Backup succeed".format(template_id, template_name))
except BaseException:
    logging.critical("Failed fetch dict on step - request all template")
    logging.error("Backup Failed")
