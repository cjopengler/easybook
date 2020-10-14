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


class TensorEqual:

    def __call__(self, x: torch.LongTensor, y: torch.LongTensor):
        """
        判断 tensor 是否相当
        :param x: tensor
        :param y: tensor
        :return:
        """

        return (x != y).sum() == 0