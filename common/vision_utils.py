import config
import cv2
import numpy as np
from common.screen_utils import screenshot, screenshot_comparison
from common.init_utils import DIGIT_TEMPLATES

DEFAULT_THRESHOLD = 0.65
SPECIAL_THRESHOLD = {"8": 0.55, "9": 0.55, "3": 0.55}


# 比對兩張圖片變化
def image_changed(img1, img2, threshold=5):
    if img1 is None or img2 is None:
        return True

    diff = cv2.absdiff(img1, img2)
    mean_diff = np.mean(diff)

    return mean_diff > threshold


# 檢查右上角X
def check_cancel():
    screenshot(config.UI.CANCEL_REGION, "cancel_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "cancel_screenshot.png", "cancel_template.png"
    )
    print(max_val)
    threshold = 0.7  # 70% 相似度

    if max_val >= threshold:
        print('右上角"X"圖示匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        return False


# 主頁彈跳禮包 右上角X
def check_gift_page_cancel():
    screenshot(
        config.UI.MAIN_PAGE_GIFT_PACK_CANCEL_REGION,
        "main_page_gift_pack_cancel_screenshot.png",
    )
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "main_page_gift_pack_cancel_screenshot.png",
        "main_page_gift_pack_cancel_template.png",
    )
    print(max_val)
    threshold = 0.7  # 70% 相似度

    if max_val >= threshold:
        print('彈跳禮包 右上角"X"圖示匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        return False


# 主頁彈跳禮包 右上角X
def check_skill_unlock():
    screenshot(
        config.UI.SKILL1_REGION,
        "skill1_screenshot.png",
    )
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "skill1_screenshot.png",
        "skill1_template.png",
    )
    print(max_val)
    threshold = 0.7  # 70% 相似度

    if max_val >= threshold:
        print("技能 1 圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        return False


# 檢查短頁面展開箭頭
def ckeck_expand_arrow():
    screenshot(config.UI.EXPAND_ARROW_REGION, "expand_arrow_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "expand_arrow_screenshot.png", "expand_arrow_template.png"
    )
    print(max_val)
    threshold = 0.7  # 70% 相似度

    if max_val >= threshold:
        print("短頁面展開箭頭圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        return False


# 檢查角色頁面"突襲卡片"文字
def check_raid_card():
    screenshot(config.UI.RAID_CARD_REGION, "raid_card_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "raid_card_screenshot.png", "raid_card_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('角色頁面"突襲卡片"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('角色頁面"突襲卡片"文字匹配失敗')
        return False


# 檢查專精圖示
def check_specialize():
    screenshot(config.UI.SPECIALIZE_REGION, "specialize_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "specialize_screenshot.png", "specialize_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"專精"圖示匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"專精"圖示匹配失敗')
        return False


# 檢查英雄頁面 新英雄驚嘆號圖示
def check_new_hero_mark():
    screenshot(config.UI.NEW_HERO_MARK_REGION, "new_hero_mark_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "new_hero_mark_screenshot.png", "new_hero_mark_template.png"
    )
    print(max_val)
    threshold = 0.7  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"新英雄驚嘆號"圖示匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"新英雄驚嘆號"圖示匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字4
def check_max_level4():
    screenshot(config.UI.MAX_LEVEL4_REGION, "max_level4_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level4_screenshot.png", "max_level4_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級4"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級4"文字匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字5
def check_max_level5():
    screenshot(config.UI.MAX_LEVEL5_REGION, "max_level5_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level5_screenshot.png", "max_level5_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級5"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級5"文字匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字6
def check_max_level6():
    screenshot(config.UI.MAX_LEVEL6_REGION, "max_level6_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level6_screenshot.png", "max_level6_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級6"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級6"文字匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字7
def check_max_level7():
    screenshot(config.UI.MAX_LEVEL7_REGION, "max_level7_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level7_screenshot.png", "max_level7_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級7"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級7"文字匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字8
def check_max_level8():
    screenshot(config.UI.MAX_LEVEL8_REGION, "max_level8_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level8_screenshot.png", "max_level8_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級8"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級8"文字匹配失敗')
        return False


# 檢查英雄頁面"最高等級"文字9
def check_max_level9():
    screenshot(config.UI.MAX_LEVEL9_REGION, "max_level9_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "max_level9_screenshot.png", "max_level9_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('英雄頁面"最高等級9"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('英雄頁面"最高等級9"文字匹配失敗')
        return False


# 檢查角色頁成就圖示
def check_achievement():
    screenshot(config.UI.ACHIEVEMENT_REGION, "achievement_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "achievement_screenshot.png", "achievement_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('角色頁面"成就"圖示匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('角色頁面"成就"圖示匹配失敗')
        return False


# 檢查角色頁重生文字
def check_role_page_rebirth():
    screenshot(config.UI.ROLE_PAGE_REBIRTH_REGION, "role_page_rebirth_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "role_page_rebirth_screenshot.png", "role_page_rebirth_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('角色頁面"重生"按鈕匹配成功！')
        print("匹配位置:", max_loc)
        return True
    else:
        print('角色頁面"重生"按鈕匹配失敗！')
        return False


# 檢查重生頁重生文字
def check_rebirth_page_rebirth():
    screenshot(
        config.UI.REBIRTH_PAGE_REBIRTH_REGION, "rebirth_page_rebirth_screenshot.png"
    )
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "rebirth_page_rebirth_screenshot.png", "rebirth_page_rebirth_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('重生頁面"重生"按鈕匹配成功！')
        print("匹配位置:", max_loc)
        return True
    else:
        print('重生頁面"重生"按鈕匹配失敗！')
        return False


# 檢查成就頁成就文字
def check_achievement_text():
    screenshot(
        config.UI.ACHIEVEMENT_PAGE_ACHIEVEMENT_REGION, "achievement_text_screenshot.png"
    )
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "achievement_text_screenshot.png", "achievement_text_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('角色頁面"成就"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('角色頁面"成就"文字匹配失敗')
        return False


# 檢查簽到圖示
def check_sign():
    screenshot(config.UI.SIGN_REGION, "sign_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "sign_screenshot.png", "sign_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print("簽到圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("簽到圖示匹配失敗")
        return False


# 檢查寵物蛋圖示
def check_egg():
    screenshot(config.UI.EGG_REGION, "egg_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "egg_screenshot.png", "egg_template.png"
    )
    print(max_val)
    threshold = 0.8  # 80% 相似度

    if max_val >= threshold:
        print("寵物蛋圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("寵物蛋圖示匹配失敗")
        return False


# 檢查神器頁文字 (闇影之書)
def check_shadow_book_text():
    screenshot(config.UI.SHADOW_BOOK_TEXT_REGION, "shadow_book_text_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "shadow_book_text_screenshot.png", "shadow_book_text_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('"闇影之書"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('"闇影之書"文字匹配失敗')
        return False


# 檢查商店文字 (顆鑽石)
def check_diamond_text():
    screenshot(config.UI.DIMOND_TEXT_REGION, "dimond_text_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "dimond_text_screenshot.png", "dimond_text_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print('"顆鑽石"文字匹配成功')
        print("匹配位置:", max_loc)
        return True
    else:
        print('"顆鑽石"文字匹配失敗')
        return False


# 檢查商店寶箱(左)圖示
def check_treasure_left():
    screenshot(config.UI.TREASURE_LEFT_REGION, "treasure_left_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "treasure_left_screenshot.png", "treasure_left_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print("寶箱(左)圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("寶箱(左)圖示匹配失敗")
        return False


# 檢查商店寶箱(中)圖示
def check_treasure_middle():
    screenshot(config.UI.TREASURE_MIDDLE_REGION, "treasure_middle_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "treasure_middle_screenshot.png", "treasure_middle_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print("寶箱(中)圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("寶箱(中)圖示匹配失敗")
        return False


# 檢查商店寶箱(右)圖示
def check_treasure_right():
    screenshot(config.UI.TREASURE_RIGHT_REGION, "treasure_right_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "treasure_right_screenshot.png", "treasure_right_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print("寶箱(右)圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("寶箱(右)圖示匹配失敗")
        return False


# 檢查商店領取寶箱圖示
def check_receive_treasure():
    screenshot(config.UI.RECEIVE_TREASURE_REGION, "receive_treasure_screenshot.png")
    min_val, max_val, min_loc, max_loc = screenshot_comparison(
        "receive_treasure_screenshot.png", "receive_treasure_template.png"
    )
    print(max_val)
    threshold = 0.9  # 90% 相似度

    if max_val >= threshold:
        print("收集所有箱子圖示匹配成功")
        print("匹配位置:", max_loc)
        return True
    else:
        print("收集所有箱子圖示匹配失敗")
        return False


# 預處理關卡圖片
def preprocess_stage_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    _, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    return binary


# 切割每一位數
def split_digits(binary_img):
    h_img, w_img = binary_img.shape[:2]

    contours, _ = cv2.findContours(
        binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    digit_boxes = []

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # 過濾雜訊
        if h < 20 or w < 8:
            continue

        # ===== 關鍵：擴張紅框 =====
        pad_x = int(w * 0.25)  # 左右各 25%
        pad_y = int(h * 0.25)  # 上下各 25%

        x2 = max(0, x - pad_x)
        y2 = max(0, y - pad_y)
        w2 = min(w_img - x2, w + pad_x * 2)
        h2 = min(h_img - y2, h + pad_y * 2)

        digit_boxes.append((x2, y2, w2, h2))

    # 由左到右排序
    digit_boxes.sort(key=lambda b: b[0])
    return digit_boxes


# 單一數字比對
def match_single_digit(digit_img):
    # === 幾何特化判斷數字1（最優先 ===
    if is_thin_digit(digit_img):
        return "1", 0.9

    scores = []

    # === 模板比對 ===
    for d, tmpl in DIGIT_TEMPLATES.items():
        resized = cv2.resize(tmpl, (digit_img.shape[1], digit_img.shape[0]))

        result = cv2.matchTemplate(digit_img, resized, cv2.TM_CCOEFF_NORMED)
        score = result[0][0]
        scores.append((d, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    best_d, best_s = scores[0]
    second_s = scores[1][1]

    # === 差距判斷（避免 5/8/6/9 誤判 ===
    # if best_s < 0.6 or (best_s - second_s) < 0.08:
    #     return None, best_s

    return best_d, best_s


# 取關卡數字
def read_stage_by_template(img, debug=False):
    binary = preprocess_stage_image(img)
    boxes = split_digits(binary)

    stage_chars = []
    debug_img = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    for idx, (x, y, w, h) in enumerate(boxes):
        digit_img = binary[y : y + h, x : x + w]
        digit, score = match_single_digit(digit_img)

        # --- 核心修正 ---
        if digit is None:
            digit = "?"
            score = 0.0

        stage_chars.append(digit)

        if debug:
            color = (0, 255, 0) if score >= 0.6 else (0, 0, 255)
            cv2.rectangle(debug_img, (x, y), (x + w, y + h), color, 1)
            cv2.putText(
                debug_img,
                f"{digit}:{score:.2f}",
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                color,
                1,
            )

    if debug:
        cv2.imwrite("stage_debug.png", debug_img)

    stage_str = "".join(stage_chars)

    # 嚴格判斷
    if stage_str.isdigit():
        return int(stage_str)

    print(f"[OCR] 關卡含不確定位數: {stage_str}")
    return None


# 幾何判斷
def is_thin_digit(digit_img):
    h, w = digit_img.shape
    ratio = w / h
    return ratio < 0.32
