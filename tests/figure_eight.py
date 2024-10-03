import pyautogui
import time
import math

def figure_eight_motion(center_x, center_y, radius, duration=5, steps=100):
    """Moves the mouse in a figure-8 pattern"""
    for t in range(steps):
        # Time variable normalized between 0 and 2*pi (one loop of the figure-8)
        angle = (t / steps) * 2 * math.pi

        # Calculate x and y position for figure-8 using trigonometric functions
        x = int(center_x + radius * math.sin(angle))
        y = int(center_y + radius * math.sin(angle) * math.cos(angle))

        # Move the cursor to the calculated position
        pyautogui.moveTo(x, y, duration=0.01)

if __name__ == "__main__":
    # Set initial parameters
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width / 2
    center_y = screen_height / 2
    radius = 100  # Radius for the figure-8 movement
    duration = 5  # Duration of the figure-8 movement in seconds

    while True:
        # Call the figure-eight movement function
        figure_eight_motion(center_x, center_y, radius, duration)
        
        # Wait for 30 seconds before moving again
        time.sleep(30)
