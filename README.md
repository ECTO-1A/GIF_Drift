# GIF Drift
# Mouse Mover with Random GIF Viewer

This Python application moves the mouse cursor randomly at random intervals and displays random GIFs in a GUI window. The GUI features "New" and "Save" buttons to control the mouse movement and refresh the displayed GIFs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Features

- **Random Mouse Movement**: Simulates human-like mouse movements by moving the cursor to random positions on the screen at random intervals.
- **Random GIF Display**: Shows a random GIF in the application window, fetching a new one each time the "New" button is clicked.
- **GUI Controls**:
  - **"New" Button**: Starts the mouse movement (if not already running) and displays a new random GIF.
  - **"Save" Button**: Stops the mouse movement.
- **Customizable Parameters**: Easily adjust movement speed, intervals, and add your own GIFs.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ECTO-1A/GIF_Drift.git
   cd GIF_Drift
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   *Alternatively, you can install dependencies manually:*

   ```bash
   pip install pyautogui requests Pillow
   ```

## Usage

Run the application with:

```bash
python mouse_mover_app.py
```

### GUI Controls

- **"New" Button**: Starts the mouse movement and displays a new random GIF.
- **"Save" Button**: Stops the mouse movement.
- **Closing the Window**: Stops the mouse movement and exits the application.

## Customization

### Adjust Movement Speed and Intervals

- **Movement Speed**: Modify the range in `random.uniform(0.5, 3.0)` within the `move_to_random_point` method to adjust how fast the cursor moves.

  ```python
  duration = random.uniform(0.5, 3.0)  # Adjust the range as needed
  ```

- **Wait Time Between Movements**: Change the range in `random.randint(15, 45)` within the `move_mouse_randomly` method to adjust how frequently the cursor moves.

  ```python
  wait_time = random.randint(15, 45)  # Adjust the range as needed
  ```

### Add More GIFs

- **Edit the `gif_urls` List**: Add or remove URLs in the `gif_urls` list within the `display_random_gif` method.

  ```python
  gif_urls = [
      'https://media.giphy.com/media/3o7aD4xgHcJX3vNj4w/giphy.gif',
      'https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif',
      # Add your own GIF URLs here
  ]
  ```

  Ensure that the URLs point directly to GIF files.

### Change Window Appearance

- **Window Title**: Update the window title in the `__init__` method.

  ```python
  self.root.title("Image Viewer")  # Change to your preferred title
  ```

- **GUI Layout**: Modify how widgets are arranged by changing the `pack` methods or using other layout managers like `grid` or `place`.

## Dependencies

- **Python** 3.x
- **pyautogui**: For controlling mouse movements.
- **requests**: To fetch GIFs from the internet.
- **Pillow (PIL)**: For handling and displaying images.
- **tkinter**: For creating the GUI (comes with standard Python installations).

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Create a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

- **Use Responsibly**: This application automates mouse movements, which may interfere with other applications or tasks. Use it responsibly and ensure it does not violate any policies or terms of service.
- **Permissions**: Depending on your operating system, you may need to grant additional permissions for the script to control the mouse.
- **Ethical Considerations**: Be cautious when disguising application functionalities. Ensure compliance with all applicable laws, regulations, and organizational policies.
- **No Warranty**: This software is provided "as is", without warranty of any kind.

---

**Note**: An active internet connection is required to fetch GIFs from the provided URLs. If you encounter issues with fetching images, ensure your network connection is stable.

For any questions or issues, please open an [issue](https://github.com/ECTO-1A/GIF_Drift/issues) in the repository.