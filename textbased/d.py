import speech_recognition
import pyttsx

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)

def speak(text):
	speech_engine.say(text)
	speech_engine.runAndWait()

def listen():
	r=raw_input("\n")
	return str(r)

speak("Say something!")
speak("I heard you say " + listen())