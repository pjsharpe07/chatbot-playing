import pyttsx3
import time
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import os

print('[speaking] Speaking module loaded...')

# establish male or female voice
m_or_f = int(os.getenv('M_OR_F')) if os.getenv('M_OR_F') else 1 

### init voice engine and configure voice
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[m_or_f].id)   # changing index, changes voices. 1 for female


def speak(phrase):
    # print(f'Saying {phrase}')
    engine.say(phrase)
    engine.runAndWait()
    time.sleep(0.5)


if __name__ == '__main__':
    engine.say("Voice module installed and functioning properly")
    engine.runAndWait()