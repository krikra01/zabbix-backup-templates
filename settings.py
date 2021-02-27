import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

ZABBIX_URL = os.getenv("ZABBIX_URL")
AUTH_KEY = os.getenv("AUTH_KEY")
TEMPLATES_PATH = os.getenv("TEMPLATES_PATH")