# import pyttsx3 

# engine = pyttsx3.init()

# rate = engine.getProperty('rate')
# print("Current rate:", rate)

# engine.setProperty('rate', 100)

# voices = engine.getProperty('voices')
# print("Available voices:", voices)

# engine.setProperty('voice', voices[0].id)

# def SpeakText(command):
#     engine.say(command)
#     engine.runAndWait()

# SpeakText("manu bhai")



import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Couldn't catch you")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))