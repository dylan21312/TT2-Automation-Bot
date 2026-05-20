import config
import pyautogui
import time
import random
from common.vision_utils import (
    check_cancel,
    check_raid_card,
    check_skill_unlock,
    ckeck_expand_arrow,
)
from common.position_resolver import MainPage, RolePage, HeroPage
from common.input_utils import click_list, human_click, mouse_scroll


# 解鎖技能
def unlock_skills():
    print("=== 解鎖技能並啟動 開始 ===")
    # 檢查角色頁面是否有"突襲卡片"
    while True:
        human_click(MainPage.role_page_click_pos())  # 打開角色頁面

        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖示
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面

        if check_raid_card():  # 檢查角色頁面角色是否為"最高等級"文字
            break
        else:
            mouse_scroll(RolePage.mouse_scroll_pos(), total=300)
            time.sleep(random.uniform(1, 1.3))

    human_click(RolePage.upgrade_character_click_pos(), (0.3, 0.5))  # 升級主角

    # 解鎖技能
    unlock_skills = [
        RolePage.role_page_skill1_click_pos(),
        RolePage.role_page_skill2_click_pos(),
        RolePage.role_page_skill3_click_pos(),
        RolePage.role_page_skill4_click_pos(),
        RolePage.role_page_skill5_click_pos(),
        RolePage.role_page_skill6_click_pos(),
    ]

    click_list(unlock_skills, (0.3, 0.5))

    if check_cancel():
        human_click(MainPage.cancel_click_pos())  # 右上方 X

    start_skills_after_unlock()
    print("=== 解鎖技能並啟動 結束 ===")


# 升級技能
def upgrade_skills():
    print("=== 升級技能並啟動 開始 ===")

    # 檢查角色頁面是否有"突襲卡片"文字
    while True:
        human_click(MainPage.role_page_click_pos())  # 打開角色頁面
        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面
        if check_raid_card():  # 檢查角色頁面是否有"突襲卡片"文字
            mouse_scroll(RolePage.mouse_scroll_pos(), total=300)
            time.sleep(random.uniform(1, 1.3))
            break
        else:
            time.sleep(random.uniform(1, 1.3))

    # 升級主角
    human_click(RolePage.upgrade_character_click_pos(), (0.3, 0.5))

    # 解鎖技能 4、6
    unlock_skills = [
        RolePage.role_page_skill4_click_pos(),
        RolePage.role_page_skill6_click_pos(),
    ]
    click_list(unlock_skills, (0.2, 0.3))

    upgrade_max_skills((1, 2, 3, 5))  # 升級技能 1, 2, 3, 5

    if check_cancel():
        human_click(MainPage.cancel_click_pos())  # 右上方 X

    print("=== 升級技能並啟動 結束 ===")


def upgrade_max_skills(skill_ids=(1, 2, 3, 5)):
    for i in skill_ids:
        human_click(getattr(RolePage, f"role_page_skill{i}_click_pos")(), (0.3, 0.5))
        human_click(
            getattr(RolePage, f"role_page_skill{i}_max_click_pos")(), (0.3, 0.5)
        )


# "解鎖"技能後啟動技能
def start_skills_after_unlock():

    skills = [
        MainPage.skill1_click_pos(),  # 開技能1
        MainPage.skill2_click_pos(),  # 開技能2
        MainPage.skill3_click_pos(),  # 開技能3
        MainPage.skill4_click_pos(),  # 開技能4
        MainPage.skill5_click_pos(),  # 開技能5
        MainPage.skill6_click_pos(),  # 開技能6
    ]

    click_list(skills, (0.1, 0.3))


# "升級"技能後啟動技能
def start_skills_after_upgrade():
    if check_skill_unlock() == False:
        upgrade_skills()

    skills = [
        (MainPage.skill1_click_pos, 1),  # 技能 1 按 1 次
        (MainPage.skill2_click_pos, 1),  # 技能 2 按 1 次
        (MainPage.skill3_click_pos, 1),  # 技能 3 按 1 次
        (MainPage.skill4_click_pos, 1),  # 技能 4 按 1 次
        (MainPage.skill6_click_pos, 1),  # 技能 5 按 1 次
        (MainPage.skill5_click_pos, 1),  # 技能 6 按 1 次
    ]

    for click_fn, times in skills:
        for _ in range(times):
            human_click(click_fn(), (0.1, 0.15))
