import pydirectinput
import keyboard
import time
import threading

running = False

def spam_actions():
    global running
    while running:
        start_time = time.time()
        
        # Press space
        pydirectinput.press('space')
        
        # Wait so it dont fuck up
        time.sleep(0.1)
        pydirectinput.click()
        
        # Wait so shit dont go kabloom
        elapsed = time.time() - start_time
        time.sleep(max(0, 3 - elapsed + 0.5))

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
