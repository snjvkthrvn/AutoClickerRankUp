import pyautogui
import time

print("Move your mouse to the target area. Position will be logged in 5 seconds.")
time.sleep(5)
print(f"Mouse position: {pyautogui.position()}")