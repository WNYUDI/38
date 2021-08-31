#!/usr/bin/python3

import requests
import config

if config.SESSION == None or len(config.SESSION) == 0:
    raise Exception('config SESSION (' +
                    str(config.SESSION) + ')')

if config.LATITUDE == None or len(config.LATITUDE) == 0:
    raise Exception('config LATITUDE (' +
                    str(config.LATITUDE) + ')')

if config.LONGITUDE == None or len(config.LONGITUDE) == 0:
    raise Exception('config LONGITUDE (' +
                    str(config.LONGITUDE) + ')')

if config.COUNTRY == None or len(config.COUNTRY) == 0:
    raise Exception('config COUNTRY (' +
                    str(config.COUNTRY) + ')')

if config.CITY == None or len(config.CITY) == 0:
    raise Exception('config CITY (' +
                    str(config.CITY) + ')')

if config.DISTRICT == None or len(config.DISTRICT) == 0:
    raise Exception('config DISTRICT (' +
                    str(config.DISTRICT) + ')')

if config.PROVINCE == None or len(config.PROVINCE) == 0:
    raise Exception('config PROVINCE (' +
                    str(config.PROVINCE) + ')')

if config.TOWNSHIP == None or len(config.TOWNSHIP) == 0:
    raise Exception('config TOWNSHIP (' +
                    str(config.TOWNSHIP) + ')')

if config.STREET == None or len(config.STREET) == 0:
    raise Exception('config STREET (' +
                    str(config.STREET) + ')')

if config.AREACODE == None or len(config.AREACODE) == 0:
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
        'answers': '["0"，"0"，"1"]'
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
