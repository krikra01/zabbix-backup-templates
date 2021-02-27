import settings

def payload_all_template():
    payload_template = {
        "jsonrpc": "2.0",
        "method": "template.get",
        "params": {
            "output": "extend"
        },
        "auth": "{0}".format(settings.AUTH_KEY),
        "id": 1
    }
    return payload_template

def payload_all_export(template_id):
    payload_export_template = {
        "jsonrpc": "2.0",
        "method": "configuration.export",
        "params": {
            "options": {
                "templates": [
                    "{0}".format(template_id)
                ]
            },
            "format": "xml"
        },
        "auth": "{0}".format(settings.AUTH_KEY),
        "id": 1
    }
    return payload_export_template