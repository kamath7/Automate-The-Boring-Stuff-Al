import pyautogui

pyautogui.typewrite('Hello World',interval=0.2)
pyautogui.typewrite(['Hello','Word','a','b','left','left'],interval=1)
print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('F5')
pyautogui.hotkey('ctrl','o')