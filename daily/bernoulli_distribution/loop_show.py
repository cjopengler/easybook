#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/11/25 17:22:00
"""

import torch


def loop(x: torch.Tensor):
    for i in range(10):
        sample = torch.bernoulli(x)

        print(f"{i}: {sample}")


def loop_by_class():

    x = torch.tensor([0.3])
    m = torch.distributions.Bernoulli()

    for i in range(10):
        print(f"{i}: {m.sample()}")


def masked_sequence(length: int, prob: float):
    probs = torch.full((length,), prob)
    masked = torch.bernoulli(probs)

    print(f"mask=1的数量: {masked.sum()}")

    print(masked)
    return masked
