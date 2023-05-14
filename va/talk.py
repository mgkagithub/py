import pyttsx3
input=''
def talks(input):
    # Initialize the text-to-speech engine.
    engine = pyttsx3.init()

    # Set the voice.
    engine.setProperty('voice', 'english-us')

    # Say some text.
    engine.say("Hello, world!")

    # Play the speech.
    engine.runAndWait()
