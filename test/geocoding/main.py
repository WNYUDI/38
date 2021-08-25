#!/usr/bin/python3

import requests

requests.packages.urllib3.disable_warnings()
geocoding_response = requests.get(
    'https://api.map.baidu.com/geocoding/v3/', params={
        'ak': 'gQsCAgCrWsuN99ggSIjGn5nO',
        'output': 'json',
        'address': '北京市海淀区上地十街10号',
    },
    headers={
        'Referer': 'https://www.piliang.tech/'
    }, timeout=60)

if geocoding_response.status_code != 200:
    raise Exception('geocoding in response status_code (' +
                    str(geocoding_response.status_code) + ')')

geocoding_content = geocoding_response.json()

if 'status' not in geocoding_content:
    raise Exception('geocoding in response content (' +
                    str(geocoding_content) + ')')

if geocoding_content['status'] != 0:
    raise Exception('geocoding in response content status (' +
                    str(geocoding_content['status']) + ')')

if 'result' not in geocoding_content:
    raise Exception('geocoding in response content (' +
                    str(geocoding_content) + ')')

geocoding_content_result = geocoding_content['result']

if 'location' not in geocoding_content_result:
    raise Exception('geocoding in response content result (' +
                    str(geocoding_content_result) + ')')

geocoding_content_result_location = geocoding_content_result['location']

if 'lng' not in geocoding_content_result_location:
    raise Exception('geocoding in response content location (' +
                    str(geocoding_content_result_location) + ')')

if 'lat' not in geocoding_content_result_location:
    raise Exception('geocoding in response content location (' +
                    str(geocoding_content_result_location) + ')')

longitude = geocoding_content_result_location['lng']
latitude = geocoding_content_result_location['lat']


