#!/usr/bin/python3

# Github Actions不支持input函数
# 采用Process能够建立起通道，用于支持input
import os
import sys
import time

import config
import processsv

if config.TELEGRAM_BOT_TOKEN_OR_USER_NAME == None:
    raise Exception('config TELEGRAM_BOT_TOKEN_OR_USER_NAME (' +
                    str(config.TELEGRAM_BOT_TOKEN_OR_USER_NAME) + ')')

dir_path = os.path.split(os.path.abspath(__file__))[0]


need_telegram_info = False


def processsv_when_read(text):
    global process
    global need_telegram_info
    if text.endswith('\n'):
        print(text, end='')
        if text[0:-1] == 'TelegramClient start':
            need_telegram_info = True
        if text[0:-1] == 'TelegramClient started':
            need_telegram_info = False
        return True
    elif need_telegram_info and text == 'Please enter your phone (or bot token): ':
        print(text, end='')
        process.exec(config.TELEGRAM_BOT_TOKEN_OR_USER_NAME)
        return True
    else:
        return False


def processsv_when_error(text):
    if text.endswith('\n'):
        print(text, end='')
        return True
    else:
        return False


def processsv_when_exec(text):
    print(text, end='')
    return True


processsv.when_read = processsv_when_read
processsv.when_error = processsv_when_error
processsv.when_exec = processsv_when_exec
process = processsv.start()
process.exec('python ' + dir_path + '/main.py ; exit')
