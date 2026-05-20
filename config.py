# =====系統設定 =====
import os


class SYSTEM:
    MONITOR_INDEX = 2

    DAILY_INTERVAL = 12 * 60 * 60  # 執行每日任務間隔時間: 12 小時（秒）

    PROJECT_ROOT = os.path.dirname(
        os.path.abspath(__file__)
    )  # 專案根目錄（ tap_titans_bot ）

    NUMBER_TEMPLATE_DIR = os.path.join(
        PROJECT_ROOT, "number_templates"
    )  # 關卡數字模板讀取路徑


# ===== 螢幕資訊（執行時初始化）=====
class MONITOR:
    LEFT = 0
    TOP = 0
    WIDTH = 0
    HEIGHT = 0


# ===== UI 座標設定 =====
class UI:
    """===== 主頁面 positions====="""

    CANCEL_CLICK_POS = ((514, 46), (522, 50))  # 右上角X
    SKIP_CLICK_POS = ((475, 951), (485, 958))  # 右下角跳過
    EXPAND_ARROW_CLICK_POS = ((439, 577), (448, 580))  # 短頁面展開箭頭

    SIGN_CLICK_POS = ((510, 243), (514, 246))  # 簽到
    SIGN_RECEIVE_CLICK_POS = ((266, 663), (284, 672))  # 簽到獎勵領取
    EGG_CLICK_POS = ((509, 372), (514, 376))  # 寵物蛋
    PARTNER_CLICK_POS = ((213, 527), (220, 530))  # 召喚公會夥伴
    THUNDER_BOAT_CLICK_POS = ((282, 393), (285, 396))  # 召喚雷霆船

    ROLE_PAGE_CLICK_POS = ((38, 995), (49, 1006))  # 打開"角色頁面"
    HERO_PAGE_CLICK_POS = ((133, 993), (145, 1005))  # 打開"英雄頁面"
    ARTIFACT_PAGE_CLICK_POS = ((412, 993), (422, 1006))  # 打開"神器頁面"
    SHOP_PAGE_CLICK_POS = ((504, 994), (515, 1004))  # 打開"商店頁面"

    SKILL1_CLICK_POS = ((40, 923), (52, 930))  # 技能啟動1
    SKILL2_CLICK_POS = ((133, 924), (143, 932))  # 技能啟動2
    SKILL3_CLICK_POS = ((229, 924), (238, 931))  # 技能啟動3
    SKILL4_CLICK_POS = ((320, 922), (329, 930))  # 技能啟動4
    SKILL5_CLICK_POS = ((411, 923), (420, 932))  # 技能啟動5
    SKILL6_CLICK_POS = ((504, 922), (512, 932))  # 技能啟動6

    """===== 角色頁面 positions====="""
    ACHIEVEMENT_CLICK_POS = (234, 109)  # 成就
    ACHIEVEMENT_CANCEL_CLICK_POS = (492, 91)  # 成就頁面右上角 X
    ACHIEVEMENT_RECEIVE1_CLICK_POS = (439, 284)  # 成就頁面每日領取1
    ACHIEVEMENT_RECEIVE2_CLICK_POS = (439, 395)  # 成就頁面每日領取2
    ACHIEVEMENT_RECEIVE3_CLICK_POS = (439, 506)  # 成就頁面每日領取3
    ACHIEVEMENT_RECEIVE4_CLICK_POS = (439, 615)  # 成就頁面每日領取4
    ACHIEVEMENT_RECEIVE5_CLICK_POS = (439, 730)  # 成就頁面每日領取5
    ACHIEVEMENT_RECEIVE6_CLICK_POS = (439, 839)  # 成就頁面每日領取6
    ACHIEVEMENT_RECEIVE7_CLICK_POS = (439, 697)  # 成就頁面每日領取7 (滾輪下拉後的座標)
    ACHIEVEMENT_RECEIVE8_CLICK_POS = (439, 811)  # 成就頁面每日領取8 (滾輪下拉後的座標)
    ACHIEVEMENT_RECEIVE9_CLICK_POS = (439, 921)  # 成就頁面每日領取9 (滾輪下拉後的座標)

    UPGRADE_CHARACTER_CLICK_POS = (467, 194)  # 升級主角
    ROLE_PAGE_REBIRTH_CLICK_POS = ((453, 312), (477, 325))  # 角色頁重生
    REBIRTH_PAGE_REBIRTH_CLICK_POS = ((271, 897), (284, 909))  # 重生頁重生
    ROLE_PAGE_SKILL1_CLICK_POS = ((462, 490), (470, 496))  # 技能1
    ROLE_PAGE_SKILL2_CLICK_POS = ((462, 580), (471, 587))  # 技能2
    ROLE_PAGE_SKILL3_CLICK_POS = ((463, 667), (470, 674))  # 技能3
    ROLE_PAGE_SKILL4_CLICK_POS = ((463, 740), (470, 746))  # 技能4
    ROLE_PAGE_SKILL5_CLICK_POS = ((463, 842), (471, 849))  # 技能5
    ROLE_PAGE_SKILL6_CLICK_POS = ((464, 926), (472, 933))  # 技能6
    ROLE_PAGE_SKILL1_MAX_CLICK_POS = ((335, 491), (343, 497))  # 升滿技能1
    ROLE_PAGE_SKILL2_MAX_CLICK_POS = ((335, 580), (344, 587))  # 升滿技能2
    ROLE_PAGE_SKILL3_MAX_CLICK_POS = ((334, 667), (343, 674))  # 升滿技能3
    ROLE_PAGE_SKILL4_MAX_CLICK_POS = ((335, 740), (344, 747))  # 升滿技能4
    ROLE_PAGE_SKILL5_MAX_CLICK_POS = ((336, 842), (344, 848))  # 升滿技能5
    ROLE_PAGE_SKILL6_MAX_CLICK_POS = ((336, 926), (345, 933))  # 升滿技能6

    """===== 英雄頁面 positions====="""
    MOUSE_SCROLL_POS = ((265, 590), (279, 605))  # 滑鼠移動至座標使用滾輪
    HERO1_UPGRADE_CLICK_POS = ((456, 191), (469, 201))  # 英雄升級1
    HERO2_UPGRADE_CLICK_POS = ((456, 277), (470, 286))  # 英雄升級2
    HERO3_UPGRADE_CLICK_POS = ((455, 368), (469, 376))  # 英雄升級3
    HERO4_UPGRADE_CLICK_POS = ((456, 456), (470, 465))  # 英雄升級4
    HERO5_UPGRADE_CLICK_POS = ((455, 543), (469, 553))  # 英雄升級5
    HERO6_UPGRADE_CLICK_POS = ((456, 630), (469, 639))  # 英雄升級6
    HERO7_UPGRADE_CLICK_POS = ((457, 712), (471, 722))  # 英雄升級7
    HERO8_UPGRADE_CLICK_POS = ((457, 803), (471, 814))  # 英雄升級8
    HERO9_UPGRADE_CLICK_POS = ((456, 893), (470, 104))  # 英雄升級9

    """===== 神器頁面 positions====="""

    ARTIFACT_ALL_CLICK_POS = ((463, 258), (477, 267))  # 升級所有神器
    ARTIFACT_SHADOW_BOOK_CLICK_POS = ((458, 338), (472, 349))  # 升級闇影之書

    """===== 商店頁面 positions====="""
    TREASURE_LEFT_CLICK_POS = (94, 116)  # 商店寶箱(左)
    TREASURE_MIDDLE_CLICK_POS = (279, 116)  # 商店寶箱(中)
    TREASURE_RIGHT_CLICK_POS = (464, 116)  # 商店寶箱(右)
    TREASURE_RECEIVE_CLICK_POS = (280, 870)  # 收集所有箱子

    """===== 截圖範圍 ====="""
    # 右上角 X 按紐
    CANCEL_REGION = {
        "left": 509,  # 區域左上角 X
        "top": 38,  # 區域左上角 Y
        "width": 21,  # 區域寬
        "height": 20,  # 區域高
    }

    # 主頁無預警彈跳禮包 右上角 X 按紐
    MAIN_PAGE_GIFT_PACK_CANCEL_REGION = {
        "left": 506,  # 區域左上角 X
        "top": 152,  # 區域左上角 Y
        "width": 29,  # 區域寬
        "height": 27,  # 區域高
    }

    # 短頁面展開箭頭
    EXPAND_ARROW_REGION = {
        "left": 430,  # 區域左上角 X
        "top": 570,  # 區域左上角 Y
        "width": 29,  # 區域寬
        "height": 17,  # 區域高
    }
    # 上方關卡
    STAGE_REGION = {
        "left": 243,  # 區域左上角 X
        "top": 77,  # 區域左上角 Y
        "width": 74,  # 區域寬
        "height": 20,  # 區域高
    }
    # 簽到
    SIGN_REGION = {
        "left": 494,  # 區域左上角 X
        "top": 228,  # 區域左上角 Y
        "width": 35,  # 區域寬
        "height": 33,  # 區域高
    }
    # 寵物蛋
    EGG_REGION = {
        "left": 494,  # 區域左上角 X
        "top": 357,  # 區域左上角 Y
        "width": 35,  # 區域寬
        "height": 33,  # 區域高
    }
    # 主頁面技能1
    SKILL1_REGION = {
        "left": 18,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }
    # 主頁面技能2
    SKILL2_REGION = {
        "left": 111,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }
    # 主頁面技能3
    SKILL3_REGION = {
        "left": 204,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }
    # 主頁面技能4
    SKILL4_REGION = {
        "left": 295,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }
    # 主頁面技能5
    SKILL5_REGION = {
        "left": 387,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }
    # 主頁面技能6
    SKILL6_REGION = {
        "left": 480,  # 區域左上角 X
        "top": 915,  # 區域左上角 Y
        "width": 57,  # 區域寬
        "height": 25,  # 區域高
    }

    # 角色頁面角色"突襲卡片"文字
    RAID_CARD_REGION = {
        "left": 21,  # 區域左上角 X
        "top": 134,  # 區域左上角 Y
        "width": 54,  # 區域寬
        "height": 17,  # 區域高
    }
    # 角色頁面成就圖示
    ACHIEVEMENT_REGION = {
        "left": 211,  # 區域左上角 X
        "top": 96,  # 區域左上角 Y
        "width": 36,  # 區域寬
        "height": 39,  # 區域高
    }
    # 成就頁面"成就"文字
    ACHIEVEMENT_PAGE_ACHIEVEMENT_REGION = {
        "left": 239,  # 區域左上角 X
        "top": 74,  # 區域左上角 Y
        "width": 77,  # 區域寬
        "height": 44,  # 區域高
    }
    # 角色頁面重生
    ROLE_PAGE_REBIRTH_REGION = {
        "left": 447,  # 區域左上角 X
        "top": 316,  # 區域左上角 Y
        "width": 38,  # 區域寬
        "height": 21,  # 區域高
    }
    # 重生頁面重生
    REBIRTH_PAGE_REBIRTH_REGION = {
        "left": 251,  # 區域左上角 X
        "top": 890,  # 區域左上角 Y
        "width": 52,  # 區域寬
        "height": 32,  # 區域高
    }

    # 英雄頁面專精圖示
    SPECIALIZE_REGION = {
        "left": 30,  # 區域左上角 X
        "top": 95,  # 區域左上角 Y
        "width": 43,  # 區域寬
        "height": 42,  # 區域高
    }

    # 英雄頁面"新英雄驚嘆號"
    NEW_HERO_MARK_REGION = {
        "left": 377,  # 區域左上角 X
        "top": 160,  # 區域左上角 Y
        "width": 11,  # 區域寬
        "height": 17,  # 區域高
    }

    # 英雄頁面"最大等級"文字 4
    MAX_LEVEL4_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 458,  # 區域左上角 Y
        "width": 72,  # 區域寬
        "height": 22,  # 區域高
    }
    # 英雄頁面"最大等級"文字 5
    MAX_LEVEL5_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 545,  # 區域左上角 Y
        "width": 72,  # 區域寬
        "height": 23,  # 區域高
    }
    # 英雄頁面"最大等級"文字 6
    MAX_LEVEL6_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 634,  # 區域左上角 Y
        "width": 70,  # 區域寬
        "height": 21,  # 區域高
    }
    # 英雄頁面"最大等級"文字 7
    MAX_LEVEL7_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 719,  # 區域左上角 Y
        "width": 70,  # 區域寬
        "height": 22,  # 區域高
    }
    # 英雄頁面"最大等級"文字 8
    MAX_LEVEL8_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 806,  # 區域左上角 Y
        "width": 70,  # 區域寬
        "height": 22,  # 區域高
    }
    # 英雄頁面"最大等級"文字 9
    MAX_LEVEL9_REGION = {
        "left": 429,  # 區域左上角 X
        "top": 893,  # 區域左上角 Y
        "width": 71,  # 區域寬
        "height": 24,  # 區域高
    }

    # 神器頁面文字 (闇影之書)
    SHADOW_BOOK_TEXT_REGION = {
        "left": 85,  # 區域左上角 X
        "top": 308,  # 區域左上角 Y
        "width": 73,  # 區域寬
        "height": 24,  # 區域高
    }

    # 商店頁面文字 (顆鑽石)
    DIMOND_TEXT_REGION = {
        "left": 239,  # 區域左上角 X
        "top": 297,  # 區域左上角 Y
        "width": 76,  # 區域寬
        "height": 29,  # 區域高
    }
    # 商店頁面寶箱 (左)
    TREASURE_LEFT_REGION = {
        "left": 77,  # 區域左上角 X
        "top": 103,  # 區域左上角 Y
        "width": 35,  # 區域寬
        "height": 32,  # 區域高
    }
    # 商店頁面寶箱 (中)
    TREASURE_MIDDLE_REGION = {
        "left": 263,  # 區域左上角 X
        "top": 103,  # 區域左上角 Y
        "width": 35,  # 區域寬
        "height": 32,  # 區域高
    }
    # 商店頁面寶箱 (右)
    TREASURE_RIGHT_REGION = {
        "left": 448,  # 區域左上角 X
        "top": 103,  # 區域左上角 Y
        "width": 35,  # 區域寬
        "height": 32,  # 區域高
    }
    # 商店頁面寶箱 (右)
    RECEIVE_TREASURE_REGION = {
        "left": 208,  # 區域左上角 X
        "top": 857,  # 區域左上角 Y
        "width": 168,  # 區域寬
        "height": 33,  # 區域高
    }
