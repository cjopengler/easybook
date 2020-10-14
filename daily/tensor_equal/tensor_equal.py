#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/10/14 20:33:00
"""

import torch

from daily.tensor_equal.solution import TensorEqual

x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
y = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])

equal = TensorEqual()

assert equal(x, y)

z = torch.tensor([[2, 2, 2],
                  [4, 5, 6]])

assert not equal(x, z)

