#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json
import sys
import time

import requests

import config

headers = {
    'userauthtype': 'MS',
    'accesstoken': config.ACCESSTOKEN
}

location = json.loads(config.LOCATION)

response = requests.get(
    'https://yfd.ly-sky.com/ly-pd-mb/form/api/healthCheckIn/client/stu/index', headers=headers, timeout=60)

if response.status_code != 200:
    raise Exception('response.status_code:', response.status_code)

questionnairePublishEntityId = response.json(
)['data']['questionnairePublishEntityId']


response = requests.get(
    'https://yfd.ly-sky.com/ly-pd-mb/form/api/questionnairePublish/' + questionnairePublishEntityId + '/getDetailWithAnswer', headers=headers, timeout=60)

if response.status_code != 200:
    raise Exception('response.status_code:', response.status_code)

answerInfoList = []

for subject in response.json()['data']['questionnaireWithSubjectVo']['subjectList']:
    answerInfo = {}
    answerInfo['subjectId'] = subject['id']
    subjectType = subject['subjectType']
    answerInfo['subjectType'] = subjectType
    if subjectType == 'location':
        answerInfo[subjectType] = location
    elif subjectType == 'signleSelect':
        answerInfo[subjectType] = {
            'beSelectValue': '1',
            'fillContent': ''
        }
    elif subjectType == 'multiSelect':
        answerInfo[subjectType] = {
            'optionAnswerList': [
                {
                    'beSelectValue': 'NotThing',
                    'fillContent': ''
                }
            ]
        }
    answerInfoList.append(answerInfo)

data = json.dumps({
    'questionnairePublishEntityId': questionnairePublishEntityId,
    'answerInfoList': answerInfoList,
})

response = requests.post(
    'https://yfd.ly-sky.com/ly-pd-mb/form/api/answerSheet/saveNormal', headers=dict(headers, **{'content-type': 'application/json'}), data=data, timeout=60)

print(response.status_code)
print(response.text)

if response.status_code != 200:
    raise Exception('response.status_code:', response.status_code)


# print(questionnairePublishEntityId)
