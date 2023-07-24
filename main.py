# Spam bot made by ghost_bak17

import pyautogui, time
message = input("message: ")
duration = (1)
repeats = input("repeats: ")

time.sleep(0.01)

for i in range(int(repeats)):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(int(duration))