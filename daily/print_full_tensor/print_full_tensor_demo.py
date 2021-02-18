#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2021 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2021/02/18 13:02:00
"""

import numpy as np
import torch

print(f"short print------------------")

x = np.eye(100, dtype=np.int)
print(x)

y = torch.eye(100, dtype=torch.int)
print(y)


torch.set_printoptions(profile="full")
np.set_printoptions(threshold=np.inf)

print(f"full print------------------")

x = np.eye(100, dtype=np.int)
print(x)

y = torch.eye(100, dtype=torch.int)
print(y)



