#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@Author: apophis
@File: sq_scene.py
@Time: 2023/8/19 21:28
@Description: 工程描述
"""
import RaphaelScriptHelper
import testDict

RaphaelScriptHelper.deviceID = "emulator-5554"
RaphaelScriptHelper.deviceType = 1


def action_done(pic, ts=1.0, comment=""):
    """
    如果是xx,则点击并且返回true，否则返回false
    :return:
    """
    if RaphaelScriptHelper.find_pic_touch(pic):
        print("点击" + comment)
        RaphaelScriptHelper.delay(ts)
        return True
    return False


def status_done(pic, ts=10, comment=""):
    """
    如果是xx状态，返回true，否则返回false
    :return:
    """
    if RaphaelScriptHelper.find_pic(pic):
        print(comment)
        RaphaelScriptHelper.delay(ts)
        return True
    return False


def pos_done(pos):
    """
    点击某个坐标
    :return:
    """
    return RaphaelScriptHelper.touch(pos)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def is_duihua():
    """
    对话
    :return:
    """
    return action_done(testDict.sq_chat, ts=0.2, comment="对话")


def skip_juqing():
    """
    跳过剧情
    :return:
    """
    return action_done(testDict.sq_skip_juqing, comment="跳过剧情")


def skip_cha():
    """
    点击×，关闭弹窗
    :return:
    """
    return action_done(testDict.sq_skip_x, ts=0.2, comment="点击×，关闭弹窗")


def skip_guanbi():
    """
    点击任意区域关闭
    :return:
    """
    return action_done(testDict.sq_skip_renyi_guanbi, ts=0.2, comment="点击任意区域关闭")


def skip_jixu():
    """
    点击任意区域继续
    :return:
    """
    return action_done(testDict.sq_skip_renyi_jixu, ts=0.2, comment="点击任意区域继续")


def skip_chengren_lilian():
    """
    跳过成人历练
    :return:
    """
    return action_done(testDict.sq_skip_chengren_lilian, ts=0.2, comment="跳过成人历练")


def skip_lingqu():
    """
    领取任务奖励
    :return:
    """
    return action_done(testDict.sq_get_lingqu, ts=0.2, comment="领取任务奖励")


def use_wupin():
    """
    使用道具
    :return:
    """
    return action_done(testDict.sq_use_wupin, comment="使用道具")


def prefix_fight():
    """
    准备进入战斗
    :return:
    """
    return action_done(testDict.sq_prefix_fight, comment="选择战斗")


def prefix_fight_queren():
    """
    准备进入战斗后，确认战斗
    :return:
    """
    return action_done(testDict.sq_prefix_fight_queren, ts=30, comment="挑战")


def huodong_enter():
    """
    点击主页面，进入活动
    :return:
    """
    if not action_done(testDict.sq_huo_dong_enter, comment="点击主页面，进入活动"):
        Exception("没有找到活动按钮")


def huodong_leave():
    """
    离开活动
    :return:
    """
    if not action_done(testDict.sq_return_x, ts=0.2, comment="离开活动"):
        Exception("没有找到离开活动按钮")


def huodong_go():
    """
    前往
    :return:
    """
    action_done(testDict.sq_huo_dong_go, ts=20, comment="前往")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def xunlu_ing():
    """
    寻路中
    :return:
    """
    return status_done(testDict.sq_xunlu, comment="寻路中")


def fight_ing():
    """
    战斗中
    :return:
    """
    return status_done(testDict.sq_fight_ing, ts=10, comment="战斗中")


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def select_zhuxian():
    """
    选择主线
    :return:
    """
    RaphaelScriptHelper.touch(testDict.sq_zhuxian)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def auto_guaji(cycle=1):
    """
    判断是否在走剧情
    :return:
    """
    count = 0
    while count < cycle:
        if prefix_fight():
            prefix_fight_queren()
        while fight_ing():
            count = 0
        while is_duihua():
            count = 0
        if skip_lingqu() or use_wupin() or skip_cha() or skip_jixu() or skip_guanbi() or skip_juqing() or skip_chengren_lilian():
            count = 0
        while xunlu_ing():
            count = 0

        count = count + 1


if __name__ == '__main__':
    auto_guaji(cycle=1000)
