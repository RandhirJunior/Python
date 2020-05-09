# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:27:28 2020

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
        
        
        print("Recognizing now.........")
        
        try :
            print("You said \n" + r.recognize_google(audio2))
            print("Audio recorded succesfuly \n")
            
        except Exception as  e :
            print("Error " + str(e))
            
        with open("recorded_audio.wav", "wb") as f:
            f.write(audio2.get_wav_data())
            
            
if __name__ == "__main__" :
    main()            