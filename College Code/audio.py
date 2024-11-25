import pyttsx3 

engine = pyttsx3.init()

rate = engine.getProperty('rate')
print("Current rate:", rate)

engine.setProperty('rate', 100)

voices = engine.getProperty('voices')
print("Available voices:", voices)

engine.setProperty('voice', voices[0].id)

def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

SpeakText("manu bhai")