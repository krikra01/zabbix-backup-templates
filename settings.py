import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Script config

ZABBIX_URL = 'https://{0}/api_jsonrpc.php'.format(os.getenv("ZABBIX_URL"))
HEADERS = {'Content-type': 'application/json'}
TEMPLATES_PATH = '{0}'.format(os.getenv("TEMPLATES_PATH"))
AUTH_KEY = os.getenv("AUTH_KEY")