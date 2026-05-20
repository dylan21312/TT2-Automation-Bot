import cv2
import os
import config
from common.vision_utils import preprocess_stage_image, split_digits

# ===== 設定 =====
NUMBER_TEMPLATE_DIR = config.SYSTEM.NUMBER_TEMPLATE_DIR
os.makedirs(NUMBER_TEMPLATE_DIR, exist_ok=True)

IMAGE_PATH = "stage_screenshot.png"  # 已截好的關卡圖

# =================


# 偵測數字
def capture_digit_templates():
    img = cv2.imread(IMAGE_PATH)
    if img is None:
        print("讀取圖片失敗")
        return

    binary = preprocess_stage_image(img)
    boxes = split_digits(binary)

    print(f"[Tool] 偵測到 {len(boxes)} 個數字")

    for idx, (x, y, w, h) in enumerate(boxes):
        digit_img = binary[y : y + h, x : x + w]

        # 顯示預覽
        cv2.imshow(f"Digit {idx}", digit_img)
        print(f"請輸入這個數字是什麼（0-9），或 Enter 跳過：")
        key = input("> ").strip()

        if not key.isdigit() or len(key) != 1:
            print("跳過")
            continue

        path = os.path.join(NUMBER_TEMPLATE_DIR, f"{key}.png")
        cv2.imwrite(path, digit_img)
        print(f"已儲存 {path}")

        cv2.destroyAllWindows()

    print("模板擷取完成")
