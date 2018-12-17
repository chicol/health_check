# -*- coding: utf-8 -*-
__author__ = 'chicol'

import os

def transfer_seperator(path):

    real_sep = os.path.sep
    if real_sep == '/':
        return path
    else:
        return path.replace("/", real_sep)

