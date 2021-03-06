#!/usr/bin/env python
# -*- coding: utf-8 -*-
__auth__ = 'chicol'

import json
import os,re
from itertools import zip_longest
from common.common import transfer_seperator


def is_data_exists(data, condition):

    res = 1 if condition in data else 0
    return res


def judge_condition(data, conditions, results):

    key = list(conditions.keys())[0]
    value = list(conditions.values())[0]
    if len(value) == 5:
        print("conditions: ", value)
        if is_data_exists(data, value):
            results.append(key)
        return is_data_exists(data, value)
    elif len(value) > 5:
        print("conditions: {}".format(value))
        condition_list = re.split('(F[A|B|C][0-9]{2}[F\|T|S|E])', value)
        condition_list = [x for x in condition_list if x != '']
        conditions_str = ''
        start_flag = False
        if value.startswith('F'):
            start_flag = True
            conditions = condition_list[0::2]
            operators = condition_list[1::2]
        else:
            conditions = condition_list[1::2]
            operators = condition_list[0::2]
        if start_flag:
            for condition, operator in zip(conditions, operators):
                conditions_str += str(is_data_exists(data, condition)) + operator
            if len(conditions) > len(operators):
                conditions_str += str(is_data_exists(data, conditions[-1]))
        else:
            for condition, operator in zip(conditions, operators):
                conditions_str += operator + str(is_data_exists(data, condition))
            if len(operators) > len(conditions):
                conditions_str += operators[-1]
        print("conditions_str: {}".format(conditions_str))
        if eval(conditions_str):
            results.append(key)


if '__main__' == __name__:

    data = ['FA01F', 'FA02T', 'FA03F', 'FA04T', 'FA05F', 'FA06T', 'FA07F', 'FA08T', 'FA09F', 'FA10T', 'FA11F', 'FA12T', 'FA13F', 'FA14T', 'FA15F', 'FA16T', 'FA17F', 'FA18T', 'FA19F']
    rule_dir = os.getcwd() + '/data/rule.json'
    rule_dir = transfer_seperator(rule_dir)
    with open(rule_dir, 'r') as f:
        rules = json.load(f)
        print(rules)
    dataQ = rules['dataQuality']
    data_no_pass = dataQ['noPass']
    data_pass = dataQ['pass']
    data_results = []
    station_results = []
    security_results = []
    station_level = None
    print(data_no_pass)
    # 检查数据质量--不通过的结果
    for condition in data_no_pass['conditions']:
        judge_condition(data, condition,data_results)
        print("data_results: {}".format(data_results))
    # 检查数据质量--通过的结果
    for condition in data_pass['conditions']:
        judge_condition(data, condition, data_results)
        print("data_results: {}".format(data_results))

