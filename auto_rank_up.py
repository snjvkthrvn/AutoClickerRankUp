import pyautogui
import time

# Coordinates for each step
coordinates = {
    "top_left_player": (439, 189),      # Step 1: Double-click on the player in the top left
    "rank_up_button": (437, 217),      # Step 2: Double-click on the Rank Up button
    "top_left_player_list": (691, 174), # Step 3: Double-click the top-left player in the player list
    "green_rank_up": (918, 380),       # Step 4: Double-click Rank Up again and let the animation play
    "continue_button": (915, 382),     # Step 5: Double-click the Continue button
    "back_button": (446, 114),         # Step 6: Double-click the Back button
}

# Function to click at specific coordinates with a duration
def click_with_duration(coord_name, duration=0.2, wait=0.5):
    if coord_name in coordinates:
        x, y = coordinates[coord_name]
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown()
        time.sleep(duration)  # Hold the click for the specified duration
        pyautogui.mouseUp()
        print(f"Clicked with duration on {coord_name} at ({x}, {y})")
        time.sleep(wait)
    else:
        print(f"Coordinates for {coord_name} not found.")

# Automated rank-up process
def auto_rank_up():
    print("Starting auto rank-up process. Switch to the game window now.")
    time.sleep(5)  # Time to switch to the game screen

    while True:
        try:
            # Step 1: Double-click on the player in the top left
            click_with_duration("top_left_player", duration=0.2, wait=1)

            # Step 2: Double-click on the Rank Up button
            click_with_duration("rank_up_button", duration=0.2, wait=1)

            # Step 3: Double-click the top-left player in the player list
            click_with_duration("top_left_player_list", duration=0.2, wait=1)

            # Step 4: Double-click Rank Up again and let the animation play (~5 seconds)
            click_with_duration("green_rank_up", duration=0.2, wait=8)

            # Step 5: Double-click the Continue button in the bottom right
            click_with_duration("continue_button", duration=0.2, wait=1)

            # Step 6: Double-click the Back button in the top left corner
            click_with_duration("back_button", duration=0.2, wait=1)

            # Step 7: Repeat until the player list is exhausted
            print("Completed one rank-up cycle. Repeating...")
        except KeyboardInterrupt:
            print("Auto rank-up stopped by user.")
            break

# Run the script
auto_rank_up()