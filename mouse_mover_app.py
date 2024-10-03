import pyautogui
import time
import random
import threading
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily GIF Viewer")
        self.is_running = False
        self.thread = None

        # Create image label to display GIFs
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Create "New" and "Save" buttons
        self.new_button = tk.Button(root, text="New", command=self.start_moving)
        self.new_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save", command=self.stop_moving)
        self.save_button.pack(pady=5)

        # Display a random GIF when the app starts
        self.display_random_gif()

    def display_random_gif(self):
        # List of GIF URLs
        gif_urls = [
            'https://media.giphy.com/media/3o7aD4xgHcJX3vNj4w/giphy.gif',
            'https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif',
            'https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif',
            'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3ZjdDd1eWRuNjMxYXk4NXZmajBvaHZ5OWpnZm1mOWh6eGpsdmQzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/elQ5RkAm90DZpirhRg/giphy.gif',
            'https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif'
        ]

        # Select a random GIF URL
        gif_url = random.choice(gif_urls)

        try:
            # Fetch the GIF
            response = requests.get(gif_url)
            response.raise_for_status()
            img_data = response.content

            # Load the GIF
            image = Image.open(BytesIO(img_data))

            # Convert to PhotoImage
            self.photo_image = ImageTk.PhotoImage(image)

            # Update the label with the new image
            self.image_label.config(image=self.photo_image)

        except Exception as e:
            print(f"Error fetching GIF: {e}")

    def move_mouse_randomly(self):
        while self.is_running:
            # Perform the random movement
            self.move_to_random_point()

            # Wait for a random duration between 15 and 45 seconds before moving again
            wait_time = random.randint(15, 45)
            time.sleep(wait_time)

    def move_to_random_point(self):
        # Get the screen size
        screen_width, screen_height = pyautogui.size()

        # Generate a random target point within the screen boundaries
        target_x = random.randint(0, screen_width)
        target_y = random.randint(0, screen_height)

        # Generate a random duration between 0.5 and 3 seconds to simulate different movement speeds
        duration = random.uniform(0.5, 3.0)

        # Move to the random point
        pyautogui.moveTo(target_x, target_y, duration=duration)

    def start_moving(self):
        # Start the mouse movement thread if not already running
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.move_mouse_randomly)
            self.thread.start()
        # Display a new random GIF
        self.display_random_gif()

    def stop_moving(self):
        if self.is_running:
            self.is_running = False
            if self.thread is not None:
                self.thread.join()
                self.thread = None

    def on_closing(self):
        self.stop_moving()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
