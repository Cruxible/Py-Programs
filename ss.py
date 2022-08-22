import pyautogui, time
time.sleep(5)
screeshot = pyautogui.screenshot()
screeshot.save('image1.png')
print('screenshot taken using pyautogui.')
time.sleep(3)
