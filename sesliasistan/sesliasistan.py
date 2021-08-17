
from folderadd import folderadd
from oku import kopyala

import speech_recognition as sr
from datetime import datetime 
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from uyanmakontrol import record1
from uyanmakontrol import kontrol
from youtube import müzik_çal
from arama import sözlük
import pyautogui

gün={"bugün günlerden ne","hangi gündeyiz","bugün hangi gün","bugün ne"}
okuma={"bunu oku","oku","seslendir"}
arama={"ara","vikide ara"}
youtube={"youtube'da ara","youtube'da müzik aç"}
özel1={"kırkiki","42"}
özel2={"hayatın evrenin ve her şeyin anlamı","hayatın evrenin ve herşeyin anlamı"}

r = sr.Recognizer()
def record(ask=False):
    with sr.Microphone() as kaynak:
            if ask:
                print(ask)
            ses= r.listen(kaynak,phrase_time_limit=4.0)
                
            voice=""
    try:  
        voice=r.recognize_google(ses,language="tr-TR")
       
    except sr.UnknownValueError:
            print("anlamadım")
    except sr.RequestError:
            print("sistem çalışmıyor")
        
    return voice                    
def cevaplar(voice):
    voice=voice.lower()
    
    if "merhaba"in voice:
        konuş("merhaba")

    elif "adın ne" in voice:
        konuş("adım ....")

    elif "nasılsın" in voice:
       konuş("iyiyim sen nasılsın") 

    elif "saat kaç" in voice: #saatin kaç olduğunu söyler.
        konuş(datetime.now().strftime("%H:%M:%S"))

    elif "arama yap" in voice:#söylenen cümle ya da kelimeyi google'da arar.
        
        search=record(konuş("ne aramak istiyorsun"))
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        konuş(search+'için bulduklarım')

    elif "görüşürüz" in voice: # botu sonlandırır.
        konuş("görüşürüz")
        exit()

    elif  voice in gün: #hangi günde olunduğunu söyler.
        bugün=time.strftime("%A").lower()
        if bugün=="sunday":
            bugün="pazar"
        elif bugün=="monday":
            bugün="pazartesi"
        elif bugün=="tuesday":
            bugün="salı"
        elif bugün=="wednesday":
            bugün="çarşamba"
        elif bugün=="thursday":
            bugün="perşembe"    
        elif bugün=="friday":
            bugün="cuma"
        elif bugün=="saturday":
            bugün="cumartesi"

        konuş(bugün)

    
    elif "twitter'ı aç" in voice:
        voice=voice.lower()
        webbrowser.open('https://twitter.com/')
        konuş("twitter ı açıyorum")

    elif "google'ı aç" in voice:
        webbrowser.open('https://www.google.com.tr/')
        konuş("google'ı açıyorum")

    elif voice in youtube : #youtube'da istenen müziği bulup oynatır.
        konuş("youtubeda hangi şarkıyı açmamı istersin")
        müzik=record()
        müzik_çal(müzik) 
    
    elif voice in özel1:
        konuş("hayatın evrenin ve her şeyin anlamı")

    elif voice in özel2:
        konuş("42")    


   
    
    elif "klasör oluştur" in voice:
        folder=folderadd()
        if(folder==True):
            konuş("klasörü oluşturdum")
        else:
            konuş("klasörü oluşturamadım")    
       
    elif "discord'u aç" in voice:
        konuş("discordu açıyorum")
        os.startfile(r"C:\\Users\\user\\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe")  

    elif "discordu kapat" in voice:
        konuş("discordu kapatıyorum")
        os.system("taskkill /F /IM  Discord.exe")

    elif "bilgisayarı kapat" in voice:
        os.system("shutdown /s /t 1") 

    elif "uyu" in voice:# botu uyku moduna alır.
        konuş("uyan dediğinde burdayım")
        while(1):

            voice1=record1()
            kontrol(voice1)
            if (kontrol(voice1))==1:
                konuş("ben geldim")
                
                break
    elif voice in arama:#wikipedia'da arama yapar.
        konuş("wikide ne aramamı istersin")
        aranacak=record()
        sonuç=sözlük(aranacak)
        konuş(sonuç)           

    elif voice in okuma: #seçilen metni seslendirir.
        metin=kopyala()
        konuş(metin) 

    elif "müziği durdur" in voice:# açık olan youtube sekmesindeki müziği durdurur.
        konuş("müziği durduruyorum")
        pyautogui.hotkey('k')

    elif "müziği oynat" in voice:#açık olan youtube sekmesindeki müziği oynatır.
        konuş("müziği oynatıyorum")
        pyautogui.hotkey('k')
        
   
            
        
def konuş(string):
   tts= gTTS(text=string,lang='tr',slow='false')
   rand=random.randint(1,10000) 
   file='audio-'+str(rand)+'.mp3'
   tts.save(file)
   playsound(file)
   os.remove(file)


while(1):
    voice1=record1()
    kontrol(voice1)
    if (kontrol(voice1))==1:
        break
konuş("nasıl yardımcı olabilirim")
time.sleep(1)
while(1):

    voice=record()
    print(voice)
    cevaplar(voice)
   
    
        




