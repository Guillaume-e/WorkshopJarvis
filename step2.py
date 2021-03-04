from gtts import gTTS as gtts
from datetime import datetime as dt
import os

#.MP3 FUNCTIONS FROM GTTS , THIS IS THE STANDARD
def audio_br(words, mp3name, language="pt"):
   teste = gtts(text=words,lang=language)
   teste.save("%s.mp3")

tempo = dt.now()
begin = "Olá! são " + str(tempo.hour) + " horas e "+ str(tempo.minute) + "     minutos"
#GENERATE MY .MP3
audio_br(begin,"A_BEGIN")