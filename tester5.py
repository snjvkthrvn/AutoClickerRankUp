import pyautogui
import time

# Coordinates to click
x, y = 1127, 7

# Wait for 5 seconds to allow you to switch to the target window
print("Switch to the window where you want to perform the click. The script will execute in 5 seconds...")
time.sleep(5)

# Move the mouse to the specified coordinates and perform a click
pyautogui.moveTo(x, y)
pyautogui.mouseDown()
time.sleep(1)  # Hold the click for 1 second
pyautogui.mouseUp()

print(f"Clicked at ({x}, {y})")