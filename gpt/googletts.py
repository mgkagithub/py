from gtts import gTTS
import os
import pygame
import threading

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def play_sound_async(file_path):
    sound_thread = threading.Thread(target=play_sound, args=(file_path,))
    sound_thread.start()

# Example usage

def text_to_speech(text , filename):
    tts = gTTS(text=text, lang='en')  # Create gTTS instance with English as the language
    tts.save(filename)  # Save the audio to a file
    play_sound(filename)


# Example usage
text = "Hello, how are you today?"
filename = "C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\output.mp3"
text_to_speech(text, filename)
