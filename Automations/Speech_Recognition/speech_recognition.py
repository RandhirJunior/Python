# -*- coding: utf-8 -*-
"""
Created on Sun May 10 00:58:13 2020

@author: Randhirs
"""

import speech_recognition as sr 


def main() :
    r = sr.Recognizer()
    
    
    # use the microphone as source for input. 
    with sr.Microphone() as source2:
        # wait for a second to let the recognizer 
        # adjust the energy threshold based on 
        # the surrounding noise level 
        r.adjust_for_ambient_noise(source2)
        
        
        print("Please Say somethings.....")
        
        #listens for the user's input
        audio2 = r.listen(source2)
        
        try :
            print("You have said :\n " + r.recognize_google(audio2))
            
        except Exception as e :
            print("Error " + str(e))

if __name__ == "__main__" :
    main()            