import cv2
import mss
import os
import config
import win32gui
import win32con

DIGIT_TEMPLATES = {}


# 初始化螢幕資訊
def init_monitor_info():
    with mss.mss() as sct:
        monitor = sct.monitors[config.SYSTEM.MONITOR_INDEX]

        config.MONITOR.LEFT = monitor["left"]
        config.MONITOR.TOP = monitor["top"]
        config.MONITOR.WIDTH = monitor["width"]
        config.MONITOR.HEIGHT = monitor["height"]

        print(
            f"[INIT] 使用螢幕 {config.SYSTEM.MONITOR_INDEX} | "
            f"left={config.MONITOR.LEFT}, top={config.MONITOR.TOP}, "
            f"{config.MONITOR.WIDTH}x{config.MONITOR.HEIGHT}"
        )


# 檢查點擊座標合法性
def validate_click_pos(value):
    # 單點 (x, y)
    if (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(v, int) for v in value)
    ):
        return

    # 矩形 ((x1, y1), (x2, y2))
    if (
        isinstance(value, tuple)
        and len(value) == 2
        and all(isinstance(p, tuple) and len(p) == 2 for p in value)
        and all(isinstance(n, int) for p in value for n in p)
    ):
        return

    raise ValueError("必須是 (x, y) 或 ((x1, y1), (x2, y2))，且皆為 int")


# 檢查座標範圍合法性
def validate_region(region):
    if not isinstance(region, dict):
        raise TypeError("必須是 dict")

    required_keys = ("left", "top", "width", "height")

    for key in required_keys:
        if key not in region:
            raise KeyError(f"缺少 key: {key}")

        if not isinstance(region[key], (int, float)):
            raise TypeError(f"{key} 必須是數字")

    if region["width"] <= 0 or region["height"] <= 0:
        raise ValueError("width / height 必須 > 0")

    return region


# 檢查 config.UI 設定
def validate_ui_config():
    errors = []

    for attr in dir(config.UI):
        if attr.startswith("__"):
            continue

        value = getattr(config.UI, attr)

        try:
            if attr.endswith("_CLICK_POS"):
                validate_click_pos(value)

            elif attr.endswith("_REGION"):
                validate_region(value)

        except Exception as e:
            errors.append(f"config.UI.{attr} → {e}")

    if errors:
        raise RuntimeError("UI 設定檢查失敗：\n" + "\n".join(errors))
    print("[CONFIG] UI 設定檢查通過")


# 檢查 config.SYSTEM 設定
def validate_system_config():
    if not isinstance(config.SYSTEM.MONITOR_INDEX, int):
        raise RuntimeError("config.SYSTEM.MONITOR_INDEX 必須是 int")
    print("[CONFIG] SYSTEM 設定檢查通過")


def validate_all_config():
    print("===== 開始檢查 config 設定 =====")
    validate_system_config()
    validate_ui_config()
    print("===== config 設定全部通過 =====")


# 把名稱為 BlueStacks TT2 的模擬器固定在螢幕 2 的左上(0,0)
def move_bluestacks_to_monitor2_keep_size():
    def enum_handler(hwnd, _):
        title = win32gui.GetWindowText(hwnd)
        if "BlueStacks TT2" in title:
            # 目前視窗位置與大小
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]

            # 螢幕 2 左上角（假設主螢幕 1920x1080）
            target_left = config.MONITOR.LEFT
            target_top = config.MONITOR.TOP

            # 只移動，不改大小
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOP,
                target_left,
                target_top,
                width,
                height,
                win32con.SWP_NOZORDER,
            )

            print("[Window] BlueStacks TT2 已移動到螢幕2 (0,0)")

    win32gui.EnumWindows(enum_handler, None)


# 關卡數字模板載入與比對工具
def load_digit_templates():
    base = config.SYSTEM.NUMBER_TEMPLATE_DIR

    for i in range(10):
        path = os.path.join(base, f"{i}.png")
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise RuntimeError(f"模板讀取失敗: {path}")

        _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
        DIGIT_TEMPLATES[str(i)] = img

    print("[Vision] 數字模板載入完成")
