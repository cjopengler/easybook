#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
json 以 OrderDict 形式载入

Authors: PanXu
Date:    2020/11/03 21:38:00
"""
import json
from collections import OrderedDict

with open("order_dict.json", encoding="utf-8") as f:

    common_dict = json.load(f)

    print(f"common dict {type(common_dict)} --------------")

    for k, v in common_dict.items():
        print(f"{k}: {v}")

with open("order_dict.json", encoding="utf-8") as f:
    ordered_dict = json.load(f, object_pairs_hook=OrderedDict)

    print(f"order dict {type(ordered_dict)}--------------")
    for k, v in ordered_dict.items():
        print(f"{k}: {v}")



