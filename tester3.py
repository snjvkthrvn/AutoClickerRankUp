import pyautogui
import time

print("Clicking on a visible item on the screen in 5 seconds...")
time.sleep(5)
pyautogui.click(439, 189)  # Replace (100, 100) with a known clickable position
print("Click completed.")
