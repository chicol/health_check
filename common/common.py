# -*- coding: utf-8 -*-
__author__ = 'chicol'

import os

def transfer_seperator(path):

    real_sep = os.path.sep
    if real_sep == '/':
        return path
    else:
        return path.replace("/", real_sep)

def zero_fill(data, size):
    if len(data) < size:
        return '0' * (size - len(data)) + str(data)
    elif len(data) == size:
        return data
    else:
        print("data size error.")

