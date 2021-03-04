#!/bin/python3

#Import for step 1
import playsound, tempfile, gtts, pyaudio
#Import for step 2
import datetime, time
#Import for step 3
import speech_recognition, locale
#Import for step 4
import wikipedia

Ai_name = "Guideon"

def say(audio):
    speech = gtts.gTTS(text=audio, lang="fr")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

def rec_voice():
    say("Je vous ecoute ...")
    rec = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        rec.pause_threshold = 1
	    rec.energy_threshold = 5400
        voice = rec.listen(source)
	try:
            result = rec.recognize_google(voice, language='fr_FR')
        except:
            say("Je n'ai pas compris Idiot")
            result = None
        return result

def rec_loop():
    result = None
    while result == None:
        result = rec_voice()
        time.sleep(1)
    return result.lower()

def say_date():
    locale.setlocale(locale.LC_TIME, "fr_FR")
    current_date = datetime.datetime.now().strftime("%A %d %B %Y %H:%M")
    say(current_date)

if __name__ == "__main__":
    say("Bonjour capitaine !")
    while True:
        result = rec_loop()
        word_array = result.split()
        if (word_array[0] == "fermer"):
            exit(0)
        elif (word_array[0] == "date"):
            say_date()
