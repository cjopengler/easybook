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

from daily.circle_import.x_class import XClass


class YClass:

    def __init__(self, x: XClass):
        self.x = x

    def f(self):
        print(self.x.value)
