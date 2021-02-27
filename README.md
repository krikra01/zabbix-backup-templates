# Overview

The script allows you to make a backup copy of Zabbix templates, saving them in .xml format.

The script was written for working needs and does not pretend to be perfect, but it works :)

# Install

1. Clone this repository
2. Rename the .env.example to .env, edit params for: **ZABBIX_URL**, **AUTH_KEY**
    1. the authorization key can be obtained this way:
    ```
       curl -XPOST --header "Content-Type: application/json" --data '{
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "ZabbixUser",
            "password": "awesomepassword"
        },
        "id": 1
        }' https://zabbix.company.com/api_jsonrpc.php
    ```
    Sample response:
   ```
   {
    "jsonrpc": "2.0",
    "result": "0424bd59b807674191e7d77572075f33",
    "id": 1
    }
   ```
3. Activate virtual env, and install requirments
    ```
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
    ```
4. Run the script
    ```
    python3 main.py
    ```

After executing the script, the "templates /" directory will be created, where all templates will be saved in .xml format
A log file will also be created - template-status.log