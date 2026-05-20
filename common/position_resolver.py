import config


# 把座標轉換為螢幕上的座標(考慮到雙螢幕的情況)
def get_position(pos):
    left = config.MONITOR.LEFT
    top = config.MONITOR.TOP

    # === 區域座標 ((x1,y1),(x2,y2)) ===
    if isinstance(pos, tuple) and len(pos) == 2 and isinstance(pos[0], tuple):
        (x1, y1), (x2, y2) = pos
        return (
            (left + x1, top + y1),
            (left + x2, top + y2),
        )

    # === 單點座標 (x,y) ===
    x, y = pos
    return left + x, top + y


# 主頁面
class MainPage:
    # 右上角 X 關閉
    def cancel_click_pos():
        return get_position(config.UI.CANCEL_CLICK_POS)

    # 彈跳禮包 右上角 X 關閉
    def gift_pack_cancel_click_pos():
        return get_position(config.UI.MAIN_PAGE_GIFT_PACK_CANCEL_REGION)

    # 右下角跳過
    def skip_click_pos():
        return get_position(config.UI.SKIP_CLICK_POS)

    # 短頁面展開箭頭
    def expand_arrow_click_pos():
        return get_position(config.UI.EXPAND_ARROW_CLICK_POS)

    # 簽到
    def sign_click_pos():
        return get_position(config.UI.SIGN_CLICK_POS)

    # 領取簽到獎勵
    def sign_receive_click_pos():
        return get_position(config.UI.SIGN_RECEIVE_CLICK_POS)

    # 寵物蛋
    def egg_click_pos():
        return get_position(config.UI.EGG_CLICK_POS)

    # 召喚夥伴
    def partner_click_pos():
        return get_position(config.UI.PARTNER_CLICK_POS)

    # 召喚雷霆船
    def thunder_boat_click_pos():
        return get_position(config.UI.THUNDER_BOAT_CLICK_POS)

    # 打開角色頁面
    def role_page_click_pos():
        return get_position(config.UI.ROLE_PAGE_CLICK_POS)

    # 打開英雄頁面
    def hero_page_click_pos():
        return get_position(config.UI.HERO_PAGE_CLICK_POS)

    # 打開神器頁面
    def artifact_page_click_pos():
        return get_position(config.UI.ARTIFACT_PAGE_CLICK_POS)

    # 打開英雄頁面
    def shop_page_click_pos():
        return get_position(config.UI.SHOP_PAGE_CLICK_POS)

    # 施放技能1
    def skill1_click_pos():
        return get_position(config.UI.SKILL1_CLICK_POS)

    # 施放技能2
    def skill2_click_pos():
        return get_position(config.UI.SKILL2_CLICK_POS)

    # 施放技能3
    def skill3_click_pos():
        return get_position(config.UI.SKILL3_CLICK_POS)

    # 施放技能4
    def skill4_click_pos():
        return get_position(config.UI.SKILL4_CLICK_POS)

    # 施放技能5
    def skill5_click_pos():
        return get_position(config.UI.SKILL5_CLICK_POS)

    # 施放技能6
    def skill6_click_pos():
        return get_position(config.UI.SKILL6_CLICK_POS)


# 角色頁面
class RolePage:
    # 成就
    def achievement_click_pos():
        return get_position(config.UI.ACHIEVEMENT_CLICK_POS)

    def achievement_cancel_click_pos():
        return get_position(config.UI.ACHIEVEMENT_CANCEL_CLICK_POS)

    # 成就頁面每日領取1
    def achievement_receive1_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE1_CLICK_POS)

    # 成就頁面每日領取2
    def achievement_receive2_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE2_CLICK_POS)

    # 成就頁面每日領取3
    def achievement_receive3_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE3_CLICK_POS)

    # 成就頁面每日領取4
    def achievement_receive4_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE4_CLICK_POS)

    # 成就頁面每日領取5
    def achievement_receive5_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE5_CLICK_POS)

    # 成就頁面每日領取6
    def achievement_receive6_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE6_CLICK_POS)

    # 成就頁面每日領取7
    def achievement_receive7_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE7_CLICK_POS)

    # 成就頁面每日領取8
    def achievement_receive8_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE8_CLICK_POS)

    # 成就頁面每日領取9
    def achievement_receive9_click_pos():
        return get_position(config.UI.ACHIEVEMENT_RECEIVE9_CLICK_POS)

    # 滑鼠移動至座標使用滾輪
    def mouse_scroll_pos():
        return get_position(config.UI.MOUSE_SCROLL_POS)

    # 升級角色
    def upgrade_character_click_pos():
        return get_position(config.UI.UPGRADE_CHARACTER_CLICK_POS)

    # 角色頁面重生按鈕
    def role_page_rebirth_click_pos():
        return get_position(config.UI.ROLE_PAGE_REBIRTH_CLICK_POS)

    # 重生頁面重生按鈕
    def rebirth_page_rebirth_click_pos():
        return get_position(config.UI.REBIRTH_PAGE_REBIRTH_CLICK_POS)

    # 技能1
    def role_page_skill1_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL1_CLICK_POS)

    # 技能2
    def role_page_skill2_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL2_CLICK_POS)

    # 技能3
    def role_page_skill3_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL3_CLICK_POS)

    # 技能4
    def role_page_skill4_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL4_CLICK_POS)

    # 技能5
    def role_page_skill5_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL5_CLICK_POS)

    # 技能6
    def role_page_skill6_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL6_CLICK_POS)

    # 升滿技能1
    def role_page_skill1_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL1_MAX_CLICK_POS)

    # 升滿技能2
    def role_page_skill2_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL2_MAX_CLICK_POS)

    # 升滿技能3
    def role_page_skill3_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL3_MAX_CLICK_POS)

    # 升滿技能4
    def role_page_skill4_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL4_MAX_CLICK_POS)

    # 升滿技能5
    def role_page_skill5_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL5_MAX_CLICK_POS)

    # 升滿技能6
    def role_page_skill6_max_click_pos():
        return get_position(config.UI.ROLE_PAGE_SKILL6_MAX_CLICK_POS)


# 英雄頁面
class HeroPage:

    # 滑鼠移動至座標使用滾輪
    def mouse_scroll_pos():
        return get_position(config.UI.MOUSE_SCROLL_POS)

    # 英雄1
    def hero1_upgrade_click_pos():
        return get_position(config.UI.HERO1_UPGRADE_CLICK_POS)

    # 英雄2
    def hero2_upgrade_click_pos():
        return get_position(config.UI.HERO2_UPGRADE_CLICK_POS)

    # 英雄3
    def hero3_upgrade_click_pos():
        return get_position(config.UI.HERO3_UPGRADE_CLICK_POS)

    # 英雄4
    def hero4_upgrade_click_pos():
        return get_position(config.UI.HERO4_UPGRADE_CLICK_POS)

    # 英雄5
    def hero5_upgrade_click_pos():
        return get_position(config.UI.HERO5_UPGRADE_CLICK_POS)

    # 英雄6
    def hero6_upgrade_click_pos():
        return get_position(config.UI.HERO6_UPGRADE_CLICK_POS)

    # 英雄7
    def hero7_upgrade_click_pos():
        return get_position(config.UI.HERO7_UPGRADE_CLICK_POS)

    # 英雄8
    def hero8_upgrade_click_pos():
        return get_position(config.UI.HERO8_UPGRADE_CLICK_POS)

    # 英雄9
    def hero9_upgrade_click_pos():
        return get_position(config.UI.HERO9_UPGRADE_CLICK_POS)


# 神器頁面
class ArtifactPage:
    # 升級所有神器
    def artifact_all_click_pos():
        return get_position(config.UI.ARTIFACT_ALL_CLICK_POS)

    # 升級闇影之書
    def artifact_shadow_book_click_pos():
        return get_position(config.UI.ARTIFACT_SHADOW_BOOK_CLICK_POS)

    # 滑鼠移動至座標使用滾輪
    def mouse_scroll_pos():
        return get_position(config.UI.MOUSE_SCROLL_POS)


# 商店頁面
class ShopPage:
    # 寶箱(左)
    def treasure_left_click_pos():
        return get_position(config.UI.TREASURE_LEFT_CLICK_POS)

    # 寶箱(中)
    def treasure_middle_click_pos():
        return get_position(config.UI.TREASURE_MIDDLE_CLICK_POS)

    # 寶箱(右)
    def treasure_right_click_pos():
        return get_position(config.UI.TREASURE_RIGHT_CLICK_POS)

    # 領取寶箱
    def receive_treasure_click_pos():
        return get_position(config.UI.TREASURE_RECEIVE_CLICK_POS)
