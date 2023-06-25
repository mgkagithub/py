import pyttsx3
talk = input("Enter text:\n")
def talks(talk):
    # Initialize the text-to-speech engine.
    engine = pyttsx3.init()

    # Set the voice.
    engine.setProperty('voice', 'english-us')

    # Say some text.
    engine.say(talk)

    # Play the speech.
    engine.runAndWait()
talks(talk)