import pyperclip
import pyautogui
def kopyala():

    pyautogui.hotkey('ctrl','c')
    metin=pyperclip.paste()
    return metin 

 