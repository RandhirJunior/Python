# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:40:31 2020

@author: Randhirs
"""

import speech_recognition as sr 
import webbrowser as web


def main() :
    
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2)
        
        print("Please Say somethings.....")
        
        audio2 = r.listen(source2)
        
        print("Recognizing now.........")
        
        try :
            dest = r.recognize_google(audio2)
            print("You have said :" + dest)
            
            web.get(path).open(dest)
            
            
            
        except Exception as e :
            print("Error :" +str(e))
            
if __name__ == "__main__" :
    main()   