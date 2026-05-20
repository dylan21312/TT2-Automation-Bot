import config
import cv2
import mss
import numpy as np
from common.screen_utils import screenshot

screenshot(config.UI.ACHIEVEMENT_REGION, "achievement_template.png")
