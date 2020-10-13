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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from daily.circle_import.x_class import XClass


class YClass:

    def f(self, x: "XClass"):

        print(x.value)


