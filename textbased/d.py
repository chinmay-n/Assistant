import speech_recognition
import pyttsx
import requests
from bs4 import BeautifulSoup
import sys

sys.stdout = open('file', 'w')

speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 150)
types=['noun','verb','adjective']

def speak(text):
	speech_engine.say(text)
#	speech_engine.runAndWait()

def listen():
	r=raw_input("\n")
	return str(r)

def query(q):
	url	= "https://www.google.co.in/search?q="
	q	= q.replace(' ','+')
	url	= url+q
	req 	= requests.get(url)
	bs 	= BeautifulSoup(req.content,'html.parser')
	ans 	= bs.find('div',class_='g')
	a 	= strip(ans)
	return str(a)

def strip(html):
	a=str(html)
	q=a.find('<')
	while (q >= 0):
		w 	= a.find('>')
		j 	= a.find('</span>')
	#	print str(q) + ' ' + str(j) + '\n'
		if(q == j):
			a 	= a[:(q+7)]+'\n'+a[w+1:]
		a 	= a[:q]+a[w+1:]	
		q 	= a.find('<')
	for i in types:
		a = a.replace(i,(i+' '))
	return a

speak("Say something!")
#speak("I heard you say " + listen())
a 	= query(listen())
print a
speak("Result is" + a)
