import pyautogui
import time
import random

def move_to_random_point():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    
    # Generate a random target point within the screen boundaries
    target_x = random.randint(0, screen_width)
    target_y = random.randint(0, screen_height)
    
    # Generate a random duration between 0.5 and 3 seconds to simulate different movement speeds
    duration = random.uniform(0.5, 3.0)
    
    # Move to the random point
    pyautogui.moveTo(target_x, target_y, duration=duration)

if __name__ == "__main__":
    while True:
        # Perform the random movement
        move_to_random_point()
        
        # Wait for a random duration between 15 and 45 seconds before moving again
        wait_time = random.randint(15, 45)
        time.sleep(wait_time)