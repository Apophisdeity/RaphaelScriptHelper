#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@Author: apophis
@File: sq_huo_dong_danren.py
@Time: 2023/8/15 14:41
@Description: 工程描述
"""
import RaphaelScriptHelper
import testDict
import sq_huo_dong

RaphaelScriptHelper.deviceID = "emulator-5554"
RaphaelScriptHelper.deviceType = 1

DAN_REN = {
    "远古宝图": testDict.sq_huo_dong_danren_baotu,
    "百人道场": testDict.sq_huo_dong_danren_daochang,
    "挂机": testDict.sq_huo_dong_danren_guaji,
    "护送": testDict.sq_huo_dong_danren_husong,
    "家族任务": testDict.sq_huo_dong_danren_jiazu,
    "水田迷宫": testDict.sq_huo_dong_danren_migong,
    "试炼之路": testDict.sq_huo_dong_danren_shilian,
    "远古兽王": testDict.sq_huo_dong_danren_shouwang,
    "委托": testDict.sq_huo_dong_danren_weituo,
    "竞技场": testDict.sq_huo_dong_danren_jingji
}


def enter(comment):
    """
    进入某场景
    :param comment:
    :return:
    """
    img_url = DAN_REN.get(comment)
    if img_url is None: Exception("没有找到{}".format(comment))
    if not RaphaelScriptHelper.find_pic_touch(img_url, comment):
        Exception("没有找到{}按钮".format(comment))
    RaphaelScriptHelper.delay(2)


def prefix_danren(comment):
    """
    前缀
    :return:
    """
    sq_huo_dong.enter()
    enter(comment)
    sq_huo_dong.go()


def husong():
    """
    护送
    :return:
    """
    prefix_danren("护送")
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_husong_kaishihusong, "开始护送"):
        RaphaelScriptHelper.delay(2)

        RaphaelScriptHelper.touch(testDict.sq_huo_dong_danren_husong_husongwu)
        print("选择护送物品")
        RaphaelScriptHelper.delay(1)

        RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_husong_queding, "确定")
        RaphaelScriptHelper.delay(8)

        while (RaphaelScriptHelper.find_pic(testDict.sq_fight_ing, "战斗中")
               or RaphaelScriptHelper.find_pic(testDict.sq_huo_dong_danren_husong_husongzhong, "护送中")):
            RaphaelScriptHelper.delay(60)

        while RaphaelScriptHelper.find_pic_touch(testDict.sq_chat, "对话"):
            RaphaelScriptHelper.delay(1)
            while RaphaelScriptHelper.find_pic_touch(testDict.sq_xunlu, "寻路中"):
                RaphaelScriptHelper.delay(20)

        while (RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_jixu, "点击任意区域继续")
               or RaphaelScriptHelper.find_pic_touch(testDict.sq_skip_renyi_guanbi, "点击任意区域关闭")):
            RaphaelScriptHelper.delay(1)


def migong():
    """
    水田迷宫,没写完
    :return:
    """
    prefix_danren("水田迷宫")
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_migong_jinru, "进入迷宫"):
        RaphaelScriptHelper.delay(2)

        RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_migong_jinru_queren, "进入")
        RaphaelScriptHelper.delay(5)
        # 若在队伍中，则此功能必须
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_tuidui, "退队"):
            RaphaelScriptHelper.delay(1)
            RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_migong_jinru_queren, "进入")
            RaphaelScriptHelper.delay(5)

        while RaphaelScriptHelper.touch(testDict.sq_huo_dong_danren_migong_qianjin):
            print("前进")
            RaphaelScriptHelper.delay(3)
            while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_migong_qianjin):
                RaphaelScriptHelper.delay(5)
                print("点击精灵")


def weituo():
    """
    委托
    :return:
    """
    prefix_danren("委托")
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_weituo_queren, "委托确认"):
        RaphaelScriptHelper.delay(1)
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_weituo_queren, "委托确认"):
        RaphaelScriptHelper.delay(1)
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_weituo_kaishi, "开始"):
        RaphaelScriptHelper.delay(1)
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_xunlu, "寻路中"):
        RaphaelScriptHelper.delay(20)
    while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_weituo_shangjiao, "上交"):
        RaphaelScriptHelper.delay(1)
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_husong_queding, "确定"):
            RaphaelScriptHelper.delay(1)
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_huo_dong_danren_weituo_xiala, "下拉"):
            RaphaelScriptHelper.delay(5)
        while RaphaelScriptHelper.find_pic_touch(testDict.sq_chat):
            RaphaelScriptHelper.delay(0.5)


if __name__ == '__main__':
    import ADBHelper
    print(ADBHelper.getDevicesList())
