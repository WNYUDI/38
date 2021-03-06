#!/usr/bin/python3
# 一个脚本，用于通过Telegram登录IBCN
import base64
import re

import requests
from telethon import TelegramClient, events, sync

import config

if config.TELEGRAM_SESSION_NAME == None:
    raise Exception('config TELEGRAM_SESSION_NAME (' +
                    str(config.TELEGRAM_SESSION_NAME) + ')')

if config.TELEGRAM_API_ID == None:
    raise Exception('config TELEGRAM_API_ID (' +
                    str(config.TELEGRAM_API_ID) + ')')

if config.TELEGRAM_API_HASH == None:
    raise Exception('config TELEGRAM_API_HASH (' +
                    str(config.TELEGRAM_API_HASH) + ')')

if config.TELEGRAM_SESSION_CHARSET == None:
    raise Exception('config TELEGRAM_SESSION_CHARSET (' +
                    str(config.TELEGRAM_SESSION_CHARSET) + ')')

if config.TELEGRAM_SESSION_CONTENT == None:
    raise Exception('config TELEGRAM_API_HASH (' +
                    str(config.TELEGRAM_SESSION_CONTENT) + ')')

if config.TELEGRAM_SESSION_CHARSET == 'base64':
    content = base64.decodebytes(
        bytes(config.TELEGRAM_SESSION_CONTENT, encoding='ASCII'))
    fp = open(config.TELEGRAM_SESSION_NAME, 'wb')
    fp.write(content)
    fp.flush()
    fp.close()
else:
    raise Exception('unknown TELEGRAM_SESSION_CHARSET (' +
                    str(config.TELEGRAM_SESSION_CONTENT) + ')')

response = requests.get('https://dash.ibcn.space/auth/login', timeout=60)

if response.status_code != 200:
    raise Exception('IBCN sign in response status_code (' +
                    str(response.status_code) + ')')

if response.text == None:
    raise Exception('IBCN sign in response text (' + str(response.text) + ')')

ibcn_signin_verify_numbers = re.findall(r'number: "(.*?)"', response.text)

if len(ibcn_signin_verify_numbers) == 0:
    raise Exception('IBCN sign in verify number (' +
                    str(len(ibcn_signin_verify_numbers)) + ')')

ibcn_signin_verify_number = ibcn_signin_verify_numbers[0]

telegram_client = TelegramClient(
    config.TELEGRAM_SESSION_NAME, config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

telegram_client = telegram_client.start()

if telegram_client == None:
    raise Exception('Telegram sign in failed TelegramClient(' +
                    telegram_client + ')')

telegram_message = telegram_client.send_message(
    'IBCNbot_bot', ibcn_signin_verify_number)

if telegram_message == None:
    raise Exception('Telegram send message failed TelegramMessage(' +
                    telegram_message + ')')
else:
    print('success')
