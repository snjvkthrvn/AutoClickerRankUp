import pyautogui
import time

# List of image filenames to check
images_to_check = [
    "rank_up_button.png",
    "top_left_player_list.png",
    "green_rank_up.png",
    "continue_button.png",
    "back_button.png"
]

# Function to check for images
def check_images(images):
    print("Checking for images on the screen...")
    for image in images:
        location = pyautogui.locateOnScreen(image, confidence=0.3)
        if location:
            print(f"Image found: {image} at {location}")
        else:
            print(f"Image not found: {image}")

# Allow some time to switch to the mirrored screen
print("Switch to the mirrored screen. Checking will begin in 5 seconds.")
time.sleep(5)

# Run the check
check_images(images_to_check)