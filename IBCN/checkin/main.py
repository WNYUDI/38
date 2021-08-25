#!/usr/bin/python3
import base64

from telethon import TelegramClient, events, sync

import config

if config.TELEGRAM_SESSION_NAME == None or len(config.TELEGRAM_SESSION_NAME) == 0:
    raise Exception('config TELEGRAM_SESSION_NAME (' +
                    str(config.TELEGRAM_SESSION_NAME) + ')')

if config.TELEGRAM_API_ID == None or len(config.TELEGRAM_API_ID) == 0:
    raise Exception('config TELEGRAM_API_ID (' +
                    str(config.TELEGRAM_API_ID) + ')')

if config.TELEGRAM_API_HASH == None or len(config.TELEGRAM_API_HASH) == 0:
    raise Exception('config TELEGRAM_API_HASH (' +
                    str(config.TELEGRAM_API_HASH) + ')')

if config.TELEGRAM_SESSION_CHARSET == None or len(config.TELEGRAM_SESSION_CHARSET) == 0:
    raise Exception('config TELEGRAM_SESSION_CHARSET (' +
                    str(config.TELEGRAM_SESSION_CHARSET) + ')')

if config.TELEGRAM_SESSION_CONTENT == None or len(config.TELEGRAM_SESSION_CONTENT) == 0:
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
                    str(config.TELEGRAM_SESSION_CHARSET) + ')')

telegram_client = TelegramClient(
    config.TELEGRAM_SESSION_NAME, config.TELEGRAM_API_ID, config.TELEGRAM_API_HASH)

telegram_client = telegram_client.start()

if telegram_client == None:
    raise Exception('Telegram sign in failed TelegramClient(' +
                    str(telegram_client) + ')')

telegram_message = telegram_client.send_message(
    'IBCNbot_bot', '/checkin')

if telegram_message == None:
    raise Exception('Telegram send message failed TelegramMessage(' +
                    str(telegram_message) + ')')

print('send message success, please go to Telegram or IBCN website check and confirm whether to check in successfully')
