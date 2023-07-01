import pyautogui
import subprocess
import time
import threading
import ctypes
import keyboard
import logging

INACTIVITY_THRESHOLD = 600  
COUNTDOWN_DURATION = 60  
MAX_SHUTDOWN_RETRIES = 3

countdown_active = False

def display_shutdown_warning(message):
    ctypes.windll.user32.MessageBoxW(0, message, "PC Shutdown Warning", 0x40 | 0x1)

def check_activity():
    last_mouse_position = pyautogui.position()
    last_activity_time = time.time()

    def on_keyboard_activity(event):
        nonlocal last_activity_time
        last_activity_time = time.time()

    keyboard.on_press(on_keyboard_activity)

    global countdown_active

    while True:
        current_mouse_position = pyautogui.position()
        current_time = time.time()

        if current_mouse_position != last_mouse_position:
            last_mouse_position = current_mouse_position
            last_activity_time = current_time

            if countdown_active:
                countdown_active = False

        mouse_inactivity_time = current_time - last_activity_time

        if mouse_inactivity_time >= INACTIVITY_THRESHOLD and not countdown_active:
            countdown_active = True
            display_shutdown_warning("PC will shut down in 1 minute.")
            threading.Timer(COUNTDOWN_DURATION, initiate_shutdown).start()
            break

def initiate_shutdown(retries=0):
    try:
        global countdown_active

        if countdown_active:
            for remaining_time in range(COUNTDOWN_DURATION, 0, -1):
                if not countdown_active:
                    return

                display_shutdown_warning(f"PC will shut down in {remaining_time} seconds.")
                time.sleep(1)

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
