#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/10/13 21:12:00
"""

# from daily.circle_import.y_class import YClass
# from daily.circle_import.y_class_fix_1 import YClass
# from daily.circle_import.y_class_fix_2 import YClass
from daily.circle_import.y_class_fix_3 import YClass


class XClass:

    def __init__(self, value: int, y: YClass):
        self.value = value
        y.f(self)


if __name__ == '__main__':
    XClass(value=3, y=YClass())

