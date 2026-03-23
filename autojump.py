import pydirectinput
import keyboard
import time
import threading

running = False

def spam_actions():
    global running
    while running:
        # Press space
        pydirectinput.press('space')
        
        # Wait 0.3 seconds, then click
        time.sleep(0.1)
        pydirectinput.click()
        
        # Wait remaining time (1.7 total loop)
        time.sleep(2)

def toggle():
    global running
    running = not running
    if running:
        print("Started...")
        threading.Thread(target=spam_actions, daemon=True).start()
    else:
        print("Stopped.")

keyboard.add_hotkey('F8', toggle)

print("Press F8 to start/stop")
keyboard.wait()