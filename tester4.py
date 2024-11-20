import pyautogui
import time

def move_with_visuals(start_x, start_y, end_x, end_y, duration=1):
    """
    Move the mouse from (start_x, start_y) to (end_x, end_y) with a visual effect.
    :param start_x: Starting X-coordinate.
    :param start_y: Starting Y-coordinate.
    :param end_x: Ending X-coordinate.
    :param end_y: Ending Y-coordinate.
    :param duration: Time in seconds for the complete movement.
    """
    steps = 50  # Number of steps for smooth movement
    sleep_time = duration / steps
    dx = (end_x - start_x) / steps
    dy = (end_y - start_y) / steps

    for i in range(steps):
        x = start_x + (dx * i)
        y = start_y + (dy * i)
        pyautogui.moveTo(x, y)
        time.sleep(sleep_time)

    pyautogui.moveTo(end_x, end_y)  # Ensure the final position is precise
    print(f"Moved visually from ({start_x}, {start_y}) to ({end_x}, {end_y})")

def click_with_visual(x, y, duration=0.2):
    """
    Move the mouse visually to (x, y) and click with a specified duration.
    :param x: X-coordinate of the target.
    :param y: Y-coordinate of the target.
    :param duration: Time in seconds to hold the click.
    """
    current_x, current_y = pyautogui.position()  # Get current mouse position
    move_with_visuals(current_x, current_y, x, y, duration=0.5)  # Move to target visually
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()
    print(f"Clicked with duration at ({x}, {y})")

# Test the visual movement and click
def test_visual_click():
    print("Switch to the target screen. Movement will start in 5 seconds...")
    time.sleep(5)

    # Define test coordinates
    test_coords = [(440, 185), (691, 174), (915, 382)]

    # Loop through the coordinates
    for x, y in test_coords:
        click_with_visual(x, y, duration=0.3)

# Run the test
test_visual_click()