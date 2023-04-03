import pyautogui as pt
limit = int(input("Enter limit : "))
message = input("Enter message : ")
pt.PAUSE = 2.5
i = 0
while (i < limit+1):
    pt.typewrite(message + " ")
    pt.press("enter")
    pt.PAUSE = 0.4
    i=i+1
    