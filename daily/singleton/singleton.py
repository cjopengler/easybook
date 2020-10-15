#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

#
# Copyright (c) 2020 PanXu, Inc. All Rights Reserved
#
"""
brief

Authors: PanXu
Date:    2020/10/15 20:38:00
"""


class Singleton:
    """
    单例模式
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

            # 初始化
            cls.__instance.value = 3
        return cls.__instance

    def __init__(self):
        print("Init Singleton ...")


if __name__ == '__main__':

    instance1 = Singleton()
    instance2 = Singleton()
    print(instance1.value)

    assert id(instance1) == id(instance2)
