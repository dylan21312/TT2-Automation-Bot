import random
import pyautogui
import time
import mss

def human_scroll(x, y, total=-600):
    pyautogui.moveTo(x, y)

    steps = random.randint(3, 6)
    per_step = total // steps

    for _ in range(steps):
        pyautogui.scroll(per_step)
        time.sleep(random.uniform(0.05, 0.12))

MONITOR_INDEX = 2
MONITER2 = mss.mss().monitors[MONITOR_INDEX]
ROLE_PAGE_CLICK_POS = (MONITER2["left"] + 43, 999) # 角色頁面按鈕點擊座標（螢幕相對座標）
pyautogui.click(ROLE_PAGE_CLICK_POS)
time.sleep(random.uniform(1.0, 1.2)) # 隨機等待1~1.2秒 
MONITOR_INDEX = 2  # BS 在副螢幕
MONITER2 = mss.mss().monitors[MONITOR_INDEX]
human_scroll(MONITER2["left"] + 234, 952, total=600)
