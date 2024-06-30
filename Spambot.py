import time,pyautogui
while True:
 time.sleep(3)
 f=open("greetings.txt","r")

 for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

 f.close()


