import cv2
import mss
import numpy as np
import config
from common.init_utils import DIGIT_TEMPLATES


# mss 截圖
def grab_region_on_monitor(monitor_index, left, top, width, height):
    with mss.mss() as sct:
        base = sct.monitors[monitor_index]
        region = {
            "left": base["left"] + left,
            "top": base["top"] + top,
            "width": width,
            "height": height,
        }
        img = np.array(sct.grab(region))
        # mss 擷取的是 BGRA，要轉成 BGR
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)


# 比對截圖與原圖
def screenshot_comparison(screenshot_img, template_img):
    img = cv2.imread(screenshot_img, 0)  # 灰階
    template = cv2.imread(template_img, 0)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    return cv2.minMaxLoc(res)


# 截圖存檔
def screenshot(region, filename):
    img = grab_region_on_monitor(
        config.SYSTEM.MONITOR_INDEX,
        region["left"],
        region["top"],
        region["width"],
        region["height"],
    )
    cv2.imwrite(f"{filename}", img)
    print(f"已儲存 {filename}")


# 圖片灰階、放大、二值化
def preprocess_image(img):
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return binary


# 數字切割 + 模板比對
def recognize_digits_by_template(binary_img):
    contours, _ = cv2.findContours(
        binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    digit_imgs = []
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        if h < 20 or w < 10:
            continue
        digit_imgs.append((x, binary_img[y : y + h, x : x + w]))

    if not digit_imgs:
        return None

    digit_imgs.sort(key=lambda d: d[0])  # 左 → 右

    result = ""
    for _, dimg in digit_imgs:
        dimg = cv2.resize(dimg, (40, 60))

        best_digit = None
        best_score = 0.0

        for digit, tmpl in DIGIT_TEMPLATES.items():
            tmpl_resized = cv2.resize(tmpl, (40, 60))
            score = cv2.matchTemplate(dimg, tmpl_resized, cv2.TM_CCOEFF_NORMED).max()

            if score > best_score:
                best_score = score
                best_digit = digit

        if best_score < 0.6:  # 安全門檻
            return None

        result += best_digit

    return int(result) if result.isdigit() else None
