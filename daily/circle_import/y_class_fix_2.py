#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/10/13 21:17:00
"""


class YClass:

    def f(self, x: "XClass"):
        from daily.circle_import.x_class import XClass
        x: XClass = x
        print(x.value)


