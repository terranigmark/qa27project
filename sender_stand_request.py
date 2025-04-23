import configuration
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

response = get_logs()
print(response.status_code)
print(response.headers)

