import pyautogui
import time

# Wait a few seconds to switch to the mirrored screen
time.sleep(5)

# Take a screenshot of the current screen
screenshot = pyautogui.screenshot()
screenshot.save("test_screen.png")
print("Screenshot saved as test_screen.png")