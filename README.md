# Shutdown.py

Shutdown.py is an automated PC shutdown program that monitors user activity and initiates a system shutdown when no movement or keyboard activity is detected for a specified period of time. It helps ensure energy efficiency and provides an additional layer of security for your PC.

## Features

-   Monitors mouse movement and keyboard activity.
-   Starts a countdown and displays a warning before initiating the shutdown.
-   Allows cancellation of the countdown if activity is detected.
-   Retries the shutdown process in case of errors.
-   Logs error messages for troubleshooting.

## Use Cases

-   Energy Efficiency: Automatically shut down your PC after a period of inactivity to conserve power and reduce electricity consumption.
-   Security: Protect your system from unauthorized access by initiating a shutdown when idle.
-   Productivity: Encourage regular breaks by setting a time limit for inactivity and prompting users to resume their work.

## How to Run

1.  Make sure you have Python installed on your system.
2.  Install the required dependencies by running the following command:
    `pip install pyautogui keyboard` 
3.  Download the `shutdown.py` file from this repository.
4.  Open a terminal or command prompt and navigate to the directory where the `shutdown.py` file is located.
5.  Run the program using the following command:
 `python shutdown.py` 
    

## Run on Startup (Windows)

To run the `shutdown.py` program automatically on startup, follow these steps:

1.  Press `Win + R` to open the Run dialog box.
2.  Type `shell:startup` and press Enter. This will open the Startup folder.
3.  Copy the `shutdown.py` file and paste it into the Startup folder.
4.  The program will now run every time you start your computer.

Note: The instructions for running on startup may vary for different operating systems.
