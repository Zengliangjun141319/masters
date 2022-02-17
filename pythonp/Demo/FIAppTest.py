# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     FIAppTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          11/22/2021 4:05 PM
-------------------------------------------------
   Change Activity:
                   11/22/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
import uiautomator2 as u2
import time


class FIAppTest(unittest.TestCase):
    def EditWO(self):
        d = u2.connect()
        d.app_start('com.ForesightIntelligence.FleetIntelligence')
        time.sleep(5)
        d(text='Work Order').click()    # 点击Work order菜单
        time.sleep(3)
        d(text='Completed').click()    # 点击Completed
        time.sleep(2)
        d(text='Open').click()
        time.sleep(2)
        d(text='300').click()
        time.sleep(1)
        d(text='Save').click()

        d.press('back')

    def Mapview(self):
        d = u2.connect()
        d.app_start('com.ForesightIntelligence.FleetIntelligence')
        time.sleep(5)
        d.xpath(
            '//android.widget.RelativeLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').set_text('char')
        d.press('enter')
        d(text='CHARIOTOFFIRE').click()
        d(text='Cancel').click()
        d.xpath(
            '//android.widget.RelativeLayout/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[5]/android.widget.ImageView[1]').click()
        d(text='+ ADD LOCATIONS').click()
        d.xpath(
            '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.Button[3]').click()
        d.click(0.503, 0.498)
        d.xpath(
            '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.Button[3]').click()
        d.click(0.081, 0.801)
        d.xpath(
            '//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.Button[3]').click()
        d.click(0.914, 0.273)
        d(text='GET DIRECTIONS').click()
        d.press("back")


    def test_something(self):
        self.EditWO()


if __name__ == '__main__':
    unittest.main()
