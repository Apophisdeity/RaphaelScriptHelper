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
import sq_scene

RaphaelScriptHelper.deviceID = "emulator-5554"
RaphaelScriptHelper.deviceType = 1

DANREN = {
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


class HuoDong:
    def __int__(self):
        pass

    def prefix_danren(self, comment):
        """
        前缀
        :return:
        """
        img_url = DANREN[comment]
        if img_url is None: Exception("没有找到对应单人活动：" + comment)
        print("开启单人活动：" + comment)
        sq_scene.huodong_enter()
        sq_scene.action_done(img_url)
        sq_scene.huodong_go()

    def xianhua(self):
        """
        鲜花任务
        :return:
        """
        print("开启社交活动：鲜花任务")
        sq_scene.huodong_enter()
        sq_scene.action_done(testDict.sq_huo_dong_shejiao_start, comment="点击社交")
        sq_scene.action_done(testDict.sq_huo_dong_shejiao_xianhua, comment="开始鲜花任务")
        sq_scene.huodong_go()
        sq_scene.action_done(testDict.sq_huo_dong_shejiao_xianhua_duiyou, ts=30, comment="寻找队友")

        while sq_scene.fight_ing():
            pass
        while sq_scene.skip_cha():
            pass
        RaphaelScriptHelper.touch(testDict.sq_zhuanpan)
        print("转盘领奖")
        RaphaelScriptHelper.delay(6)
        sq_scene.action_done(testDict.sq_quxiao, comment="取消加好友")

    def weituo(self):
        for _ in range(3):
            self.prefix_danren("委托")
            sq_scene.action_done(testDict.sq_huo_dong_danren_weituo_queren, comment="委托确认")
            sq_scene.action_done(testDict.sq_huo_dong_danren_weituo_kaishi, ts=2, comment="开始")
            while sq_scene.xunlu_ing():
                pass
            if sq_scene.action_done(testDict.sq_huo_dong_danren_weituo_shangjiao, comment="上交"):
                if sq_scene.action_done(testDict.sq_huo_dong_danren_husong_queding, ts=1, comment="确定"):
                    pass
                if RaphaelScriptHelper.find_pic_slide(testDict.sq_huo_dong_danren_weituo_xiala[0],
                                                      testDict.sq_huo_dong_danren_weituo_xiala[1]):
                    print("下拉")
                    RaphaelScriptHelper.delay(5)
                while sq_scene.action_done(testDict.sq_chat):
                    pass

    def husong(self):
        """
        护送
        :return:
        """
        for _ in range(3):
            self.prefix_danren("护送")
            sq_scene.action_done(testDict.sq_huo_dong_danren_husong_kaishihusong, ts=2, comment="开始护送")
            RaphaelScriptHelper.touch(testDict.sq_huo_dong_danren_husong_husongwu)
            print("选择护送物品")
            RaphaelScriptHelper.delay(1)

            sq_scene.action_done(testDict.sq_huo_dong_danren_husong_queding, ts=8, comment="确定")

            # 护送中
            while (sq_scene.fight_ing() or RaphaelScriptHelper.find_pic(
                    testDict.sq_huo_dong_danren_husong_husongzhong)):
                RaphaelScriptHelper.delay(60)

            sq_scene.auto_guaji()

    def jingji(self):
        self.prefix_danren("竞技场")
        sq_scene.action_done(testDict.sq_huo_dong_danren_jingji_enter, ts=2, comment="进入竞技场")
        sq_scene.action_done(testDict.sq_huo_dong_danren_jingji_start_1, comment="开始挑战1")
        sq_scene.action_done(testDict.sq_huo_dong_danren_jingji_start_2, comment="开始挑战2")
        for _ in range(3):
            if _ == 0:
                # 青铜1
                tar = testDict.sq_huo_dong_danren_jingji_select_1
            elif _ == 1:
                # 青铜2
                tar = testDict.sq_huo_dong_danren_jingji_select_2
            else:
                # 青铜3
                tar = testDict.sq_huo_dong_danren_jingji_select_3
            RaphaelScriptHelper.touch(tar)
            print("选择对手，进入战斗")
            RaphaelScriptHelper.delay(3)
            while sq_scene.fight_ing():
                pass
            sq_scene.action_done(testDict.sq_skip_renyi_jixu, ts=2, comment="战斗结束")
            sq_scene.action_done(testDict.sq_skip_renyi_jixu_heise, comment="竞技场等级提升")
        sq_scene.action_done(testDict.sq_huo_dong_danren_jingji_lingqu, ts=2, comment="领奖")
        sq_scene.action_done(testDict.sq_return_return, comment="返回")
        sq_scene.action_done(testDict.sq_leave, ts=2, comment="离开")

    def yuangu_baotu(self):
        self.prefix_danren("远古宝图")
        sq_scene.action_done(testDict.sq_huo_dong_danren_baotu_enter, comment="远古宝图")
        sq_scene.start()
        RaphaelScriptHelper.delay(20)
        while sq_scene.fight_ing():
            pass
        RaphaelScriptHelper.touch(testDict.sq_zhuanpan)
        print("转盘领奖")
        RaphaelScriptHelper.delay(5)

    def shilian(self):
        self.prefix_danren("试炼之路")
        sq_scene.action_done(testDict.sq_huo_dong_danren_shilian_start, ts=3, comment="开始试炼")
        sq_scene.action_done(testDict.sq_skip_x_buguize, comment="点X")
        # 简单
        RaphaelScriptHelper.touch(testDict.sq_huo_dong_danren_shilian_road)
        RaphaelScriptHelper.delay(2)

        count = 2
        lf = testDict.sq_huo_dong_danren_shilian_point[0]
        rg = testDict.sq_huo_dong_danren_shilian_point[1]
        while True:
            print("选择关卡")
            RaphaelScriptHelper.touch((lf, rg + count * 60))
            RaphaelScriptHelper.delay(1)
            if not sq_scene.action_done(testDict.sq_huo_dong_danren_shilian_queren, ts=5, comment="试炼"):
                break
            while sq_scene.fight_ing():
                # 若自动战斗没有开启，需要开启
                sq_scene.auto_fight()
                pass
            sq_scene.action_done(testDict.sq_skip_renyi_jixu_heise, comment="点击任意区域继续")
            count += 1
        sq_scene.action_done(testDict.sq_return_return, comment="返回")
        sq_scene.action_done(testDict.sq_leave, ts=2, comment="离开")


if __name__ == '__main__':
    dan_ren = HuoDong()
    dan_ren.xianhua()
