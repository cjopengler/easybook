#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
伯努利分布采样

Authors: PanXu
Date:    2020/11/25 17:19:00
"""

import torch

from daily.bernoulli_distribution import loop_show


a = torch.empty(3, 3).uniform_(0, 1)
print(a)


# loop_show.loop(a)
# loop_show.masked_sequence(200, 0.15)

