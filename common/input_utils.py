import random
import pyautogui
import time


# 滑鼠滾輪
def mouse_scroll(pos, total=-600):
    """
    pos:
        - (x, y)
        - ((x1, y1), (x2, y2))
    """

    # 單點
    if isinstance(pos[0], int):
        x, y = pos

    # 矩形範圍
    else:
        (x1, y1), (x2, y2) = pos
        x = random.randint(min(x1, x2), max(x1, x2))
        y = random.randint(min(y1, y2), max(y1, y2))

    pyautogui.moveTo(x, y, random.uniform(0.05, 0.15))

    remaining = total
    MAX_STEP = 300  # 滑鼠滾動安全上限

    while remaining != 0:
        step = max(-MAX_STEP, min(MAX_STEP, remaining))
        pyautogui.scroll(step)
        remaining -= step
        time.sleep(random.uniform(0.05, 0.12))


def human_click(pos, delay=(1.0, 1.2)):
    """
    pos:
        - (x, y)
        - ((x1, y1), (x2, y2))
    """

    # 單點
    if isinstance(pos[0], int):
        x, y = pos

    # 矩形範圍
    else:
        (x1, y1), (x2, y2) = pos
        x = random.randint(min(x1, x2), max(x1, x2))
        y = random.randint(min(y1, y2), max(y1, y2))

    # 加入移動微抖動
    pyautogui.moveTo(x, y, random.uniform(0.05, 0.15))
    pyautogui.click()
    time.sleep(random.uniform(*delay))


def click_list(pos_list, delay=(1.0, 1.2)):
    for pos in pos_list:
        human_click(pos, delay)
