import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)  # Vitesse de parole
    engine.setProperty("volume", 1.0)  # Volume max
    engine.say(text)
    engine.runAndWait()
