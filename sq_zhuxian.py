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
RaphaelScriptHelper.deviceID = "emulator-5556"
RaphaelScriptHelper.deviceType = 1


if __name__ == '__main__':
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
