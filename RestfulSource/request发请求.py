import requests
import json

from requests.auth import HTTPBasicAuth
# 不想写页面了，用这个requests模块伪造一下

response = requests.post(
    url='http://localhost:8881/v2/login/',
    data={
        'user': 'egon',
        'pwd': 123
    }
)
print(json.loads(response.text))
