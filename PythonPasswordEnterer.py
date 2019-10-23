import pyautogui
import time

i = 0

# Click 100 times on the MacOS password box
while i < 100:
	pyautogui.moveTo(1100, 615, duration=0.01)
	pyautogui.mouseDown(); pyautogui.mouseUp()
	pyautogui.typewrite('yourpasswordhere')
	pyautogui.moveTo(1100, 665, duration=0.01)
	pyautogui.mouseDown(); pyautogui.mouseUp()
	time.sleep(1)
	i = i + 1

