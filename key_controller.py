import pyautogui
import time

def press_space():
    pyautogui.press('space')
    print("Đã nhấn SPACE!")
    time.sleep(0.3)  # Tránh spam phím quá nhanh
