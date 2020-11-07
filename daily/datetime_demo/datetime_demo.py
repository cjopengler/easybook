#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
时间与日期

Authors: PanXu
Date:    2020/11/07 10:56:00
"""

from datetime import datetime

my_time = datetime(year=2020, month=11, day=7, hour=11, minute=3, second=2)


# 格式化输出
FORMATE_1 = '%Y-%m-%d %H:%M:%S'
FORMATE_2 = "%Y/%m/%d"

print(f"格式化输出 -----------------")
print(f"my time formate1: {my_time.strftime(FORMATE_1)}")
print(f"my time formate2: {my_time.strftime(FORMATE_2)}")

# 格式化转换
my_time_new = datetime.strptime("2020-11-07 11:03:02", FORMATE_1)

print(f"字符串日期转换成 datetime -------------------")
print(f"my_time copy: {my_time_new.strftime(FORMATE_1)}")


# 计算时间差
from datetime import timedelta

yesterday = my_time - timedelta(days=1)

print(f"时间差计算 --------------------")
print(f"my time: {my_time.strftime(FORMATE_1)}, yesterday time: {yesterday.strftime(FORMATE_1)}")

now = datetime.now()

print(f"获取当前时间 -------------------")
print(f"now: {now.strftime(FORMATE_1)}")

# 时间与时间戳转换

import time

my_timestamp = my_time.timetuple()
my_timestamp = int(time.mktime(my_timestamp))

print(f"与时间戳转换 -----------------")
print(f"my_timestamp: {my_timestamp}")

my_time_from_timestamp = datetime.fromtimestamp(my_timestamp)
print(f"my_time_from_timestamp: {my_time_from_timestamp.strftime(FORMATE_1)}")




