import pyautogui
import subprocess
import time
import threading
import ctypes
import keyboard
import logging

INACTIVITY_THRESHOLD = 540
COUNTDOWN_THRESHOLD = 60
MAX_SHUTDOWN_RETRIES = 3

def display_shutdown_warning(message):
    ctypes.windll.user32.MessageBoxW(0, message, "PC Shutdown Warning", 0x40 | 0x1)

def check_activity():
    last_mouse_position = pyautogui.position()
    last_activity_time = time.time()

    def on_keyboard_activity(event):
        nonlocal last_activity_time
        last_activity_time = time.time()

    keyboard.on_press(on_keyboard_activity)

    while True:
        current_mouse_position = pyautogui.position()
        current_time = time.time()

        if current_mouse_position != last_mouse_position:
            last_mouse_position = current_mouse_position
            last_activity_time = current_time

        mouse_inactivity_time = current_time - last_activity_time

        if mouse_inactivity_time >= INACTIVITY_THRESHOLD:
            display_shutdown_warning("PC will shut down in 1 minute.")
            threading.Timer(COUNTDOWN_THRESHOLD, initiate_shutdown).start()
            break

def initiate_shutdown(retries=0):
    try:
        subprocess.call(['shutdown', '/s', '/f', '/t', '0'], shell=True)
    except subprocess.CalledProcessError as e:
        logging.error("An error occurred while trying to shut down the PC: %s", str(e))

        if retries < MAX_SHUTDOWN_RETRIES:
            logging.info("Retrying shutdown...")
            initiate_shutdown(retries + 1)
        else:
            logging.error("Max shutdown retries exceeded. Unable to shut down.")

            subprocess.call(['shutdown', '/g'], shell=True)

try:
    logging.basicConfig(
        level=logging.ERROR,
        filename="error.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    while True:
        check_activity()
except KeyboardInterrupt:
    pass
