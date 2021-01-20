#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2021 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2021/01/20 22:07:00
"""

import torch

linear = torch.nn.Linear(4, 2)

weight = torch.nn.Parameter(torch.tensor([1., 2.], dtype=torch.float))

print(f"before weight: {weight}")

with torch.no_grad():
    weight.copy_(torch.tensor([3., 4.], dtype=torch.float))

print(f"after weight: {weight}")

