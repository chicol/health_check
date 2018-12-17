#!/usr/bin/env python
# -*- coding: utf-8 -*-
__auth__ = 'chicol'

import json
import os,re
from common.common import transfer_seperator


def is_data_exists(data, condition):

    res = 1 if condition in data else 0
    return res


def judge_condition(data, conditions):

    key = list(conditions.keys())[0]
    value = list(conditions.values())[0]
    if len(value) == 5:
        print("conditions: ", is_data_exists(data, value))
        if is_data_exists(data, value):
            data_results.append(key)
        return is_data_exists(data, value)
    elif len(value) > 5:
        print("conditions: {}".format(value))
        condition_list = re.split('(F[A|B|C][0-9]{2}[F|T|S|E])', value)
        while '' in condition_list:
            condition_list.remove('')
        # 取list中第奇数个元素 ==> 条件
        condition_key_list = condition_list[0::2]
        condition_operator_list = condition_list[1::2]
        print("condition_list: {}".format(condition_list))
        print("condition_key_list: {}".format(condition_key_list))
        print("condition_operator_list: {}".format(condition_operator_list))
        conditions_str = ''
        for key,operator in zip(condition_key_list,condition_operator_list):
            print("key: {}, operator: {}".format(key, operator))
            conditions_str += str(is_data_exists(data, key)) + operator
        print("conditions_str: {}".format(conditions_str))

        # conditions = 'FA02F&FA03F'


if '__main__' == __name__:

    data = ['FA01F', 'FA02T', 'FA03F', 'FA04T', 'FA05F', 'FA06T', 'FA07F', 'FA08T', 'FA09F', 'FA10T', 'FA21F', 'FA12T', 'FA13F', 'FA14T', 'FA15F', 'FA16T', 'FA17F', 'FA18T', 'FA19T']
    rule_dir = os.getcwd() + '/data/rule.json'
    rule_dir = transfer_seperator(rule_dir)
    with open(rule_dir, 'r') as f:
        rules = json.load(f)
        print(rules)
    dataQ = rules['dataQuality']
    data_no_pass = dataQ['noPass']
    data_results = []
    station_results = []
    security_results = []
    station_level = None
    print(data_no_pass)
    condition = data_no_pass['conditions'][1]
    print(condition)
    # print("value: {}".format(condition.values()))
    condition1 = {'FAR07F': 'FA01T&(FA02T|(FA03T&FA18T&FA19T))&FA04T&FA05T&(FA06T|FA07T)&(FA08T|FA10T)&(FA11T|FA12T|FA13T|FA14T)&FA15T&FA16T&FA17T'}
    # judge_condition(data, list(condition.values())[0])
    judge_condition(data, condition1)