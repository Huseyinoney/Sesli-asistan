
import webbrowser
import pyautogui
import time



def müzik_çal(müzik):
    url="https://www.youtube.com/results?search_query="+müzik
    webbrowser.get().open(url)
    
    time.sleep(8)
    pyautogui.click(x=433,y=309)
    
    


    
