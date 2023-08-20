#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@Author: apophis
@File: demo.py
@Time: 2023/8/14 21:28
@Description: 工程描述
"""
import RaphaelScriptHelper, testDict

RaphaelScriptHelper.deviceID = "emulator-5554"
RaphaelScriptHelper.deviceType = 1


def task_zhuxian():
    """
    主线任务
    :return:
    """
    count = 0

    while count < 10:
        while (RaphaelScriptHelper.find_pic_touch(testDict.sq_chat, "对话")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_juqing, "跳过剧情")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_x, "关闭弹窗")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_guanbi, "跳过关闭")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_jixu, "跳过继续")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_chengren_lilian, "跳过成人历练")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_get_lingqu, "领取任务奖励")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_use_wupin, "使用道具")):
            RaphaelScriptHelper.delay(0.1)
            count = 0
        while RaphaelScriptHelper.find_pic(testDict.sq_xunlu, "寻路中"):
            RaphaelScriptHelper.delay(10)
            count = 0
            continue

        while RaphaelScriptHelper.find_pic_touch(testDict.sq_prefix_fight, "准备进入战斗"):
            RaphaelScriptHelper.random_delay()
            count = 0
        while RaphaelScriptHelper.find_pic(testDict.sq_fight_ing, "战斗中"):
            RaphaelScriptHelper.delay(10)
            count = 0
            continue

        # 点击主线
        RaphaelScriptHelper.touch(testDict.sq_zhuxian)
        if count != 0: count += 1


def task_jingjichang():
    """
    竞技场
    :return:
    """

    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_enter, "点击活动")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_jingjichang_1, "点击竞技场")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_jingjichang_2, "前往")
    RaphaelScriptHelper.delay(20)
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_jingji_enter, "进入竞技场")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_jingji_start_1, "开始挑战")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_jingji_start_2, "开始挑战")
    RaphaelScriptHelper.delay(2)
    for _ in range(3):
        if _ == 0:
            tar = testDict.sq_huo_dong_danren_jingji_select_1
        elif _ == 1:
            tar = testDict.sq_huo_dong_danren_jingji_select_2
        else:
            tar = testDict.sq_huo_dong_danren_jingji_select_3
        RaphaelScriptHelper.touch(tar)
        print("选择对手，进入战斗")
        RaphaelScriptHelper.delay(3)
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_fight_ing, "战斗中"):
            RaphaelScriptHelper.delay(10)
        # 判断战斗是否结束
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_jixu, "战斗胜利，退出结算界面"):
            RaphaelScriptHelper.delay(3)


def task_shilianzhilu():
    """
    试炼之路
    :return:
    """
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_enter, "点击活动")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_shilian, "点击试炼之路")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_jingjichang_2, "前往")
    RaphaelScriptHelper.delay(20)
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_shilian_start, "开始试炼")
    RaphaelScriptHelper.delay(2)
    while True:
        pos = RaphaelScriptHelper.find_pic(testDict.huodong_shilian_5)
        if pos is not None: break
    RaphaelScriptHelper.touch((pos[0] + 200, pos[1]))
    print("选择关卡")
    RaphaelScriptHelper.delay(1)
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_shilian_queren, "试炼")
    RaphaelScriptHelper.random_delay()
    if RaphaelScriptHelper.find_pic(testDict.huodong_shilian_7):
        RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_x_buguize, "打不过")
        RaphaelScriptHelper.random_delay()
        RaphaelScriptHelper.touch(testDict.huodong_shilian_9)
        RaphaelScriptHelper.random_delay()
        RaphaelScriptHelper.find_pic_touch(testDict.sign_return, "返回")
        RaphaelScriptHelper.random_delay()
        RaphaelScriptHelper.find_pic_touch(testDict.leave, "离开")
        RaphaelScriptHelper.delay(3)
        print("打不过了")
        return
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_fight_ing, "战斗中"):
        RaphaelScriptHelper.delay(10)
    # 判断战斗是否结束
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_jixu, "战斗胜利，退出结算界面"):
        RaphaelScriptHelper.delay(3)


def task_weituo():
    """
    委托
    :return:
    """
    RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_enter, "点击活动")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_weituo_1, "委托")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_jingjichang_2, "前往")
    RaphaelScriptHelper.delay(20)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_weituo_3, "委托2")
    RaphaelScriptHelper.delay(2)
    RaphaelScriptHelper.find_pic_touch(testDict.huodong_weituo_4, "开始任务")
    RaphaelScriptHelper.delay(20)
    while (RaphaelScriptHelper.find_pic_touch(testDict.sq_chat, "对话")
           or RaphaelScriptHelper.find_pic_touch(testDict.sq_get_lingqu, "领取")):
        RaphaelScriptHelper.delay(2)

    while RaphaelScriptHelper.find_pic_touch(testDict.sq_prefix_fight, "准备进入战斗"):
        RaphaelScriptHelper.random_delay()


if __name__ == '__main__':
    print(RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_migong_jingling))