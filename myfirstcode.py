import os
import pyttsx3
import time
from googlesearch import search
import webbrowser


name = input("Your Good Name Please : ")
pyttsx3.speak("hello")
pyttsx3.speak(name)

curRentTime = time.strftime("%c")

print("Current Date & Time :", curRentTime)

currentTime = int(time.strftime("%H"))

if currentTime < 12 :
   pyttsx3.speak("Good Morning")
elif currentTime == 12 :
   pyttsx3.speak("Good Noon")
elif currentTime > 12 and currentTime < 18 :
   pyttsx3.speak("Good Afternoon")
elif currentTime >= 18 :
   pyttsx3.speak("Good Evening")

pyttsx3.speak("Welcome to my tool")
pyttsx3.speak("How can i help you ")
pyttsx3.speak("Can you Please chat me with your requirements")
print(" To search Anything in Google type 'Adi' ")

while True:
    p = input("Your Requirements : ")

    if (("run" in p) or ("execute" in p) or ("open"in p) or ("launch"in p)) and (("editor" in p) or ("notepad" in p)) :
       os.system("notepad")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("browser" in p) or ("chrome" in p)) :
       os.system("chrome")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("media player" in p) or ("player" in p)) :
       os.system("wmplayer")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("vlc" in p) or ("another player" in p)) :
       os.system("vlc")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("sublim" in p) or ("python editor" in p)) :
       os.system("sublim_text")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("default browser" in p) or ("Microsoft edge" in p)) :
       os.system("msedge")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and ("virtualbox" in p) :
       os.system("VirtualBox")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and ("anydesk" in p) :
       os.system("AnyDesk")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("codeblocks" in p) or ("code blocks" in p) or ("c coder" in p)) :
       os.system("codeblocks")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("proteus" in p) or ("circuit designer" in p)) :
       os.system("PDS")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("whatsapp" in p) or ("whats app" in p) or ("what's app" in p) or ("what'sapp" in p)) :
       os.system("WhatsApp")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("PDF" in p) or ("reader" in p)) :
       os.system("AcroRd32")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and ("excel" in p) :
       os.system("EXCEL")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("onenote" in p) or ("notes" in p) or ("memo" in p)) :
       os.system("ONENOTE")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("power point" in p) or ("powerpoint" in p)) :
       os.system("POWERPNT")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("word" in p) or ("msword" in p)) :
       os.system("WINWORD")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("task manager" in p) or ("task list" in p) or ("taskmanager" in p)) :
       os.system("taskmgr")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("control panel" in p) or ("control manager" in p) or ("controlmanager" in p)) :
       os.system("control")   
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("zoom" in p) or ("meeting app" in p)) :
       os.system("Zoom")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("weather" in p) or ("climate" in p)) :
       os.system("bingweather")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("calculator" in p) or ("calc" in p)) :
       os.system("calc")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("paint" in p) or ("mspaint" in p)) :
       os.system("mspaint")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("assistant" in p) or ("quick assistant" in p)) :
       os.system("quickassist")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("screen recorder" in p) or ("video recorder" in p)) :
       os.system("psr")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("wordpad" in p) or ("word pad" in p)) :
       os.system("wordpad")
    elif ("shutdown" in p) and (("computer" in p) or ("pc" in p) or ("laptop" in p)) :
       os.system("shutdown /s /t 1")
    elif ("restart" in p) and (("computer" in p) or ("pc" in p) or ("laptop" in p)) :
       os.system("shutdown /r /t 1")
    elif (("run" in p) or ("execute" in p) or ("open" in p) or ("launch"in p)) and (("jupyter notebook" in p) or ("IDE" in p) or ("ide" in p)) :
       os.system("jupyter notebook")                                  
    elif ("Adi" in p) or ("adi" in p) or ("ADI" in p) :
       query = input("Type here Anything you want to search in Google: ")

       for url in search(query, tld="co.in", num = 1, stop = 1, pause=2):
           webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
           webbrowser.get('chrome').open(url)
    elif ("exit" in p) or ("quit" in p) or ("close" in p) :
       pyttsx3.speak("thank you!!! for using my tool , have a nice day")
       break
    else :
       print("ERROR:\n 1.Check the code or\n 2.Might be the application is not present in this PC")   
       