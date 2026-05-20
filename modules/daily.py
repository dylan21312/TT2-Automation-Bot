import config
import pyautogui
import time
import random
from common.vision_utils import (
    check_diamond_text,
    check_egg,
    check_sign,
    check_treasure_left,
    check_treasure_middle,
    check_treasure_right,
    check_receive_treasure,
    check_cancel,
    check_achievement,
    check_achievement_text,
    ckeck_expand_arrow,
)
from common.position_resolver import HeroPage, MainPage, RolePage, ShopPage
from common.input_utils import click_list, human_click, mouse_scroll

_last_daily_time = 0  # 上次執行每日任務的時間


# 每日任務間隔時間(分鐘)
def daily():
    global _last_daily_time

    now = time.time()

    if now - _last_daily_time >= config.SYSTEM.DAILY_INTERVAL:
        print("[Daily] 執行每日任務")

        receive_sign()  # 簽到獎勵每日早上 8 點更新
        receive_eggs()  # 寵物蛋 4 小時產生 1 顆，最多儲存 4 顆
        receive_treasures()  # 商店寶箱每日早上 8 點更新
        receive_daily_achievement()  # 每日成就

        _last_daily_time = now
    else:
        remain = int((config.SYSTEM.DAILY_INTERVAL - (now - _last_daily_time)) / 60)
        print(f"[Daily] 尚未到時間，剩餘 {remain} 分鐘")


# 簽到
def receive_sign():
    if check_sign():
        human_click(MainPage.sign_click_pos())
        human_click(MainPage.sign_receive_click_pos())

        for i in range(3):
            human_click(MainPage.skip_click_pos())
    else:
        print("本日已經簽到完成！")


# 領寵物蛋
def receive_eggs():
    if check_egg():
        human_click(MainPage.egg_click_pos())

        for i in range(2):
            human_click(MainPage.skip_click_pos())
    else:
        print("沒有寵物蛋")


# 領寶箱
def receive_treasures():
    # 打開商店頁面
    human_click(MainPage.shop_page_click_pos())
    if check_diamond_text() == False:
        mouse_scroll(HeroPage.mouse_scroll_pos(), total=-9000)
        time.sleep(random.uniform(1.5, 1.7))

    # 左寶箱，中寶箱，右寶箱
    treasures = [
        (check_treasure_left, ShopPage.treasure_left_click_pos),
        (check_treasure_middle, ShopPage.treasure_middle_click_pos),
        (check_treasure_right, ShopPage.treasure_right_click_pos),
    ]

    for check_func, click_pos_func in treasures:
        if check_func():
            human_click(click_pos_func())
            if check_receive_treasure():
                human_click(ShopPage.receive_treasure_click_pos())

                for _ in range(2):
                    human_click(MainPage.skip_click_pos())
            else:
                human_click(MainPage.skip_click_pos())
            time.sleep(random.uniform(1.5, 1.7))

    # 關閉商店頁面
    if check_cancel():
        human_click(MainPage.cancel_click_pos())

    print("寶箱已領取完成")


# 領每日成就
def receive_daily_achievement():
    # 打開英雄頁
    human_click(MainPage.role_page_click_pos())

    if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
        human_click(MainPage.expand_arrow_click_pos())  # 展開頁面

    if check_achievement():
        # 打開成就頁
        human_click(RolePage.achievement_click_pos())

        # 上半部成就
        top_achievements = [
            RolePage.achievement_receive1_click_pos(),
            RolePage.achievement_receive2_click_pos(),
            RolePage.achievement_receive3_click_pos(),
            RolePage.achievement_receive4_click_pos(),
            RolePage.achievement_receive5_click_pos(),
            RolePage.achievement_receive6_click_pos(),
        ]

        click_list(top_achievements)

        # 滾動
        mouse_scroll(RolePage.mouse_scroll_pos(), total=-600)
        time.sleep(random.uniform(1.5, 1.7))

        # 下半部成就
        bottom_achievements = [
            RolePage.achievement_receive7_click_pos(),
            RolePage.achievement_receive8_click_pos(),
            RolePage.achievement_receive9_click_pos(),
        ]

        click_list(bottom_achievements)

        # 關閉成就頁
        human_click(RolePage.achievement_cancel_click_pos())

    # 關閉角色頁
    if check_cancel():
        human_click(MainPage.cancel_click_pos())

    print("每日成就已領完")
