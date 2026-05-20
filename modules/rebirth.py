import config
import pyautogui
import time
import random
from common.vision_utils import (
    check_cancel,
    check_rebirth_page_rebirth,
    check_role_page_rebirth,
    check_shadow_book_text,
    ckeck_expand_arrow,
    screenshot_comparison,
    screenshot,
)
from common.position_resolver import MainPage, RolePage, HeroPage, ArtifactPage
from common.input_utils import human_click, mouse_scroll


# 重生
def rebirth():
    print("=== 重生開始 ===")

    while True:
        #  打開角色頁面
        human_click(MainPage.role_page_click_pos())

        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面

        #  角色頁面重生按鈕
        if check_role_page_rebirth():

            human_click(RolePage.role_page_rebirth_click_pos())

            #  重生頁面重生按鈕
            if check_rebirth_page_rebirth():

                human_click(RolePage.rebirth_page_rebirth_click_pos())

                time.sleep(random.uniform(8, 10))  # 重生後loading 畫面時間
                break
            else:
                time.sleep(1, 1.2)
        else:
            mouse_scroll(RolePage.mouse_scroll_pos(), total=300)
            time.sleep(random.uniform(1, 1.3))

    print("=== 重生結束 ===")


# 升神器(闇影之書)
def upgrade_artifact_shadow_book():
    print("=== 升級神器 (闇影之書) 開始 ===")
    #  打開神器頁面
    while True:
        human_click(MainPage.artifact_page_click_pos())

        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面

        if check_shadow_book_text():
            break
        else:
            mouse_scroll(ArtifactPage.mouse_scroll_pos(), total=300)
            time.sleep(random.uniform(1, 1.3))

    # 升級點四下即可達最大有效值
    for _ in range(4):
        human_click(
            ArtifactPage.artifact_shadow_book_click_pos(), (0.1, 0.2)
        )  # 升級闇影之書

    if check_cancel():
        human_click(MainPage.cancel_click_pos())

    print("=== 升級神器 (闇影之書) 結束 ===")


# 升神器(所有神器)
def upgrade_artifact_all():
    print("=== 升級神器 (所有神器) 開始 ===")
    #  打開神器頁面
    while True:
        human_click(MainPage.artifact_page_click_pos())

        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面

        if check_shadow_book_text():
            break
        else:
            mouse_scroll(ArtifactPage.mouse_scroll_pos(), total=300)
            time.sleep(random.uniform(1, 1.3))

    # 升級點四下即可達最大有效值
    for _ in range(4):
        human_click(ArtifactPage.artifact_all_click_pos(), (0.1, 0.2))  # 升級所有神器

    if check_cancel():
        human_click(MainPage.cancel_click_pos())

    print("=== 升級神器 (所有神器) 結束 ===")
