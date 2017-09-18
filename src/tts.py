from gtts import gTTS
import os
import threading


def greet_thread(word):
	tts_thread = threading.Thread(target = greet, args=[word])
	tts_thread.start()
def greet(word):
	tts = gTTS(text=word, lang='en')
	tts.save("good.mp3")
	os.system("mpg321 good.mp3")
