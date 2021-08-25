#!/usr/bin/python3

import requests
import config

print(config.SESSION)
print(type(config.SESSION))

if config.SESSION == None:
    raise Exception('config SESSION (' +
                    str(config.SESSION) + ')')

if config.LATITUDE == None:
    raise Exception('config LATITUDE (' +
                    str(config.LATITUDE) + ')')

if config.LONGITUDE == None:
    raise Exception('config LONGITUDE (' +
                    str(config.LONGITUDE) + ')')

if config.COUNTRY == None:
    raise Exception('config COUNTRY (' +
                    str(config.COUNTRY) + ')')

if config.CITY == None:
    raise Exception('config CITY (' +
                    str(config.CITY) + ')')

if config.DISTRICT == None:
    raise Exception('config DISTRICT (' +
                    str(config.DISTRICT) + ')')

if config.PROVINCE == None:
    raise Exception('config PROVINCE (' +
                    str(config.PROVINCE) + ')')

if config.TOWNSHIP == None:
    raise Exception('config TOWNSHIP (' +
                    str(config.TOWNSHIP) + ')')

if config.STREET == None:
    raise Exception('config STREET (' +
                    str(config.STREET) + ')')

if config.AREACODE == None:
    raise Exception('config AREACODE (' +
                    str(config.AREACODE) + ')')

response = requests.post(
    'https://student.wozaixiaoyuan.com/health/save.json', headers={
        'JWSESSION': config.SESSION,
    }, params={
        'latitude': config.LATITUDE,
        'longitude': config.LONGITUDE,
        'country': config.COUNTRY,
        'city': config.CITY,
        'district': config.DISTRICT,
        'province': config.PROVINCE,
        'township': config.TOWNSHIP,
        'street': config.STREET,
        'areacode': config.AREACODE,
        'answers': '["0"]'
    }, timeout=60)

if response.status_code != 200:
    raise Exception('response status_code (' +
                    str(response.status_code) + ')')

content = response.json()

if 'code' not in content:
    raise Exception('response content (' +
                    str(content) + ')')

if content['code'] != 0:
    raise Exception('response content (' +
                    str(content) + ')')

print(response.json())
