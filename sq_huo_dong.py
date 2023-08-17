#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@Author: apophis
@File: sq_huo_dong.py
@Time: 2023/8/15 14:41
@Description: 工程描述
"""
import RaphaelScriptHelper
import testDict


def enter():
    """
    进入活动
    :return:
    """
    if not RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_enter, "进入活动"):
        Exception("没有找到活动按钮")
    RaphaelScriptHelper.delay(2)


def leave():
    """
    离开活动
    :return:
    """
    RaphaelScriptHelper.find_pic_touch(testDict.sq_return_x, "离开活动")
    RaphaelScriptHelper.delay(2)


def go(ts=20):
    """
    前往
    :return:
    """
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_go, "前往")
    RaphaelScriptHelper.delay(ts)
