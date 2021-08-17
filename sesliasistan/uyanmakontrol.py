import os

import speech_recognition as sr



uyanma={"marvin","uyan","günaydın"}

r=sr.Recognizer()

def record1():
    with sr.Microphone() as kaynak1:

            ses= r.listen(kaynak1,phrase_time_limit=3.0)
            voice1=''
    try:
         voice1=r.recognize_google(ses,language="tr-TR")
   
    except sr.UnknownValueError:
            print("uykudayım")
    except sr.RequestError:
            print("sistem çalışmıyor")
    return voice1 

def kontrol(voice1):
    
    voice1=voice1.lower()
    if voice1 in uyanma:
        
        return 1
        
        
              
        
 


