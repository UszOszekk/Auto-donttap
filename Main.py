import pyautogui
import webbrowser
import time
import keyboard
import win32api , win32con



st = False
hck = True

print('Auto donttap v1.0')
webbrowser.open('donttap.com', 1)
def c(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

print('hover your mouse over bottom left box and press  "s" !!!crtl + c TO STOP!!!')



while hck:

    if keyboard.is_pressed('s'):
        w,h = pyautogui.position()
        print(w , h)
        hck = False
        st = True
    if keyboard.is_pressed('ctrl + c'):
            print('program stopped with "crtl + c"')
            exit()    


h1 = h - 160
h2 = h1 - 160
h3 = h2 - 160
o = 160

while st == True:
        if keyboard.is_pressed('ctrl + c'):
            print('ending process')
            exit()
        if pyautogui.pixel(w, h)[0] == 0:
            c(w, h)
        if pyautogui.pixel(w + o, h)[0] == 0:
            c(w + o, h)
        if pyautogui.pixel(w + (o*2), h)[0] == 0:
            c(w + (o*2), h)
        if pyautogui.pixel(w + (o*3), h)[0] == 0:
            c(w + (o*3), h)
            #2
        if pyautogui.pixel(w, h1)[0] == 0:
            c(w, h1)
        if pyautogui.pixel(w + o, h1)[0] == 0:
            c(w + o, h1)
        if pyautogui.pixel(w + (o*2), h1)[0] == 0:
            c(w + (o*2), h1)
        if pyautogui.pixel(w + (o*3), h1)[0] == 0:
            c(w + (o*3), h1)
            #3
        if pyautogui.pixel(w, h2)[0] == 0:
            c(w, h2)
        if pyautogui.pixel(w + o, h2)[0] == 0:
            c(w + o, h2)
        if pyautogui.pixel(w + (o*2), h2)[0] == 0:
            c(w + (o*2), h2)
        if pyautogui.pixel(w + (o*3), h2)[0] == 0:
            c(w + (o*3), h2)
            #4
        if pyautogui.pixel(w, h3)[0] == 0:
            c(w, h3)
        if pyautogui.pixel(w + o, h3)[0] == 0:
            c(w + o, h3)
        if pyautogui.pixel(w + (o*2), h3)[0] == 0:
            c(w + (o*2), h3)
        if pyautogui.pixel(w + (o*3), h3)[0] == 0:
            c(w + (o*3), h3)