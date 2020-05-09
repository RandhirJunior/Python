# -*- coding: utf-8 -*-
"""
Created on Sun May 10 01:57:21 2020

@author: Randhirs
"""

from gtts import gTTS

tts = gTTS(text =" hello friend how are you", lang='en')
tts.save("convertertext.mp3")

print("Text conveterted successfuly")