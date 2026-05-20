import config
import cv2
import pyautogui
import time
import random
from common.input_utils import click_list, human_click, mouse_scroll
from common.vision_utils import (
    check_gift_page_cancel,
    check_max_level4,
    check_max_level5,
    check_max_level6,
    check_max_level7,
    check_max_level8,
    check_max_level9,
    check_new_hero_mark,
    check_specialize,
    check_cancel,
    ckeck_expand_arrow,
    read_stage_by_template,
)
from common.screen_utils import screenshot
from common.position_resolver import MainPage, RolePage, HeroPage

_execution_count = 0
_same_count = 0
_last_img = None
_last_stage = None
_last_ocr_time = 0

OCR_MIN_INTERVAL = 0.3  # 最快 OCR 間隔（秒）
OCR_FAIL_COOLDOWN = 1.5  # OCR 失敗後冷卻時間


# 點擊召喚夥伴、雷霆船
def click_summon():
    if check_cancel():
        human_click(MainPage.cancel_click_pos())  # 右上角X
    human_click(MainPage.partner_click_pos(), (0.3, 0.5))  # 召喚夥伴
    human_click(MainPage.thunder_boat_click_pos(), (0.3, 0.5))  # 召喚雷霆船


# 升級英雄
def upgrade_hero():
    while True:
        human_click(MainPage.hero_page_click_pos())  # 打開英雄頁面
        if ckeck_expand_arrow():  # 檢查是否有頁面展開箭頭圖像
            human_click(MainPage.expand_arrow_click_pos())  # 展開頁面
        # 檢查英雄頁面是否有"專精"
        if check_specialize():
            if check_new_hero_mark():
                mouse_scroll(HeroPage.mouse_scroll_pos(), total=300)
                time.sleep(random.uniform(2.0, 2.2))

            # 升級英雄
            upgrade_heroes = [
                HeroPage.hero2_upgrade_click_pos(),
                HeroPage.hero3_upgrade_click_pos(),
            ]
            # 檢查英雄是否為最高等級
            check_max_level = [
                (check_max_level4, HeroPage.hero4_upgrade_click_pos()),
                (check_max_level5, HeroPage.hero5_upgrade_click_pos()),
                (check_max_level6, HeroPage.hero6_upgrade_click_pos()),
                (check_max_level7, HeroPage.hero7_upgrade_click_pos()),
                (check_max_level8, HeroPage.hero8_upgrade_click_pos()),
                (check_max_level9, HeroPage.hero9_upgrade_click_pos()),
            ]

            for check_func, click_pos in check_max_level:
                if check_func():
                    break
                else:
                    upgrade_heroes.append(click_pos)
            click_list(upgrade_heroes, (0.1, 0.3))

            human_click(MainPage.cancel_click_pos())  # 右上角X
            break
        else:
            print('英雄頁面"專精"圖像匹配失敗')
            time.sleep(random.uniform(1, 1.3))


# 堆疊技能 1
def stack_skill(skill_number=1):
    # 技能升滿級後，因為魔力不足，無法一次啟動所有技能推疊，升完英雄後再繼續嘗試疊滿技能1的堆疊
    if check_cancel():
        human_click(MainPage.cancel_click_pos())  # 右上角 X
    human_click(
        getattr(MainPage, f"skill{skill_number}_click_pos")(), (0.3, 0.5)
    )  # 堆疊技能5


# 召喚夥伴、雷霆船 + 升級英雄
def summon_upgrade_hero(count=1, after_upgrade_skills=False):
    # 重生後先檢查是否有彈跳禮包
    # if check_gift_page_cancel():
    #     human_click(MainPage.gift_pack_cancel_click_pos())

    for Execution_count in range(count):
        print(f"=== 召喚夥伴 + 升級英雄 第{Execution_count+1}次 開始 ===")
        # click_summon()
        upgrade_hero()
        # if after_upgrade_skills:
        #     stack_skill(2)  # 堆疊第 2 個技能
        time.sleep(random.uniform(5, 7))
    print(f"=== 召喚夥伴 + 升級英雄 共{count}次 執行完畢 ===")


# 召喚夥伴、雷霆船 + 升級英雄 + 推疊技能1 + 檢查關卡
def summon_upgrade_hero_check_stage(cycle_times=10, each_cycle_times=7):
    global _execution_count
    screenshot_stage_template()
    while True:
        print(f"=== 關卡截圖 第{_execution_count+1}次循環 開始 ===")

        _execution_count += 1

        summon_upgrade_hero(each_cycle_times)  # 召喚夥伴並升級英雄
        # 技能升滿級後，因為魔力不足，無法一次啟動所有技能推疊，升完英雄後再繼續嘗試疊滿技能1的堆疊
        if check_cancel():
            human_click(MainPage.cancel_click_pos())  # 右上角 X
        human_click(MainPage.skill1_click_pos(), (0.3, 0.5))  # 堆疊技能1

        check_stage()  # 檢查是否卡關
        if _same_count == 3 or _execution_count == cycle_times:
            break

    print(f"=== 關卡截圖 共{_execution_count}次循環 執行完畢 ===")


# 取得初始關卡
def screenshot_stage_template():
    while True:
        screenshot(config.UI.STAGE_REGION, "stage_template.png")
        img = cv2.imread("stage_template.png")
        _last_stage = read_stage_by_template(img)
        print(f"關卡初始 {_last_stage}")
        if _last_stage is not None:
            print(f"[OCR] 取得關卡初始 {_last_stage}")
            break
        time.sleep(random.uniform(1, 1.5))


# 檢查是否卡關
def check_stage():
    global _last_stage, _same_count
    while True:
        screenshot(config.UI.STAGE_REGION, "stage_screenshot.png")
        img = cv2.imread("stage_screenshot.png")
        stage = read_stage_by_template(img)

        # 沒讀到（過圖動畫）
        if stage is None:
            print("[OCR] 未取得關卡，可能過圖中")
            continue
        # 與初始關卡相同
        if stage == _last_stage:
            _same_count += 1
            print(f"[OCR] 關卡 {stage} 沒變動 {_same_count} 次")
        else:
            _same_count = 0
            print(f"[OCR] 關卡有變化 {_last_stage} → {stage}")
            _last_stage = stage
        break
