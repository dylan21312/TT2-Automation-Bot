import time
from pytesseract.pytesseract import cleanup
from common.init_utils import (
    move_bluestacks_to_monitor2_keep_size,
    validate_all_config,
    init_monitor_info,
    load_digit_templates,
)
from modules.daily import daily
from modules.skills import start_skills_after_upgrade, unlock_skills, upgrade_skills
from modules.call_summon_upgrade_hero import summon_upgrade_hero
from modules.rebirth import rebirth, upgrade_artifact_all, upgrade_artifact_shadow_book
from common.vision_utils import read_stage_by_template
from tools.capture_digit_templates import capture_digit_templates

EXCUTION_COUNT = 0  # 紀錄執行次數


def main():
    print("主程式啟動")
    global EXCUTION_COUNT
    validate_all_config()  # 檢查 config 設定
    init_monitor_info()  # 初始化螢幕
    load_digit_templates()  # 載入關卡數字模板
    move_bluestacks_to_monitor2_keep_size()  # 將 BlueStacks TT2 模擬器移至螢幕 2(0,0)

    time.sleep(1)  # 等視窗穩定

    while True:
        EXCUTION_COUNT += 1
        daily()  # 簽到、寵物蛋、領寶箱、每日成就

        start_skills_after_upgrade()  # 啟動技能
        summon_upgrade_hero(
            11, after_upgrade_skills=True
        )  # 召喚夥伴、雷霆船 + 升級英雄 + 堆疊技能 2
        rebirth()  # 重生

        # upgrade_artifact_shadow_book()  # 升級闇影之書
        # upgrade_artifact_all()  # 升級所有神器


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[System] 使用者中斷程式")
    except Exception as e:
        print(f"[System] 發生未預期錯誤: {e}")
    finally:
        print(f"=== 共執行 {EXCUTION_COUNT} 次 ===")
        cleanup("my_temp_file")
        print("[System] 程式結束")
