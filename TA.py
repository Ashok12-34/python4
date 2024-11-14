import pyttsx3

engine = pyttsx3.init()

text = input("Enter the text you want to convert to speech: ")

engine.say(text)
engine.runAndWait()
