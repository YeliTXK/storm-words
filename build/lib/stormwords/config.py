#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import errno
import pickle


# Basic
VERSION = '0.0.2'
HOME = os.path.expanduser("~")
BASE_DIR = os.path.join(HOME, '.storm_words')   # 用户数据根目录

DATABASE = 'storm_words.db'
PK_FILE = 'storm_words.pk'
DB_DIR = os.path.join(BASE_DIR, DATABASE)
PK_DIR = os.path.join(BASE_DIR, PK_FILE)

config = {'version': '0'}

# YouDao AICloud config
APP_KEY = ''
SECRET_KEY = ''


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


def save_config():
    with open(PK_DIR, 'wb') as f:
        pickle.dump(config, f)


def prepare():
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)

    if os.path.isfile(PK_DIR):
        with open(PK_DIR, 'rb') as f:
            global config
            config = pickle.load(f)

    if config.get('version', '0') < VERSION:
        config['version'] = VERSION
        save_config()


# def set_dict_path(path):
#     config['stardict'] = path
#     save_config()


