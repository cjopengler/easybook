#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/11/03 21:46:00
"""

import inspect


class A:
    def __init__(self):
        pass

    def f(self):
        pass

    @classmethod
    def class_f(cls):
        pass

    @staticmethod
    def static_f():
        pass


class B(A):

    def __init__(self):
        pass


def global_f(aa: int, bb: int):
    return aa + bb


a = A()
b = B()

print("begin check...")

assert isinstance(a, A)
assert isinstance(b, A)

assert issubclass(B, A)

assert inspect.isfunction(global_f)

assert inspect.isclass(B)

assert inspect.isfunction(A.static_f)
assert inspect.ismethod(A.class_f)
assert inspect.ismethod(a.f)

print(inspect.getfullargspec(global_f))

