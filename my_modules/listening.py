import speech_recognition as sr
import time
print('[listen] Listening module loaded...')

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        time.sleep(0.5)
        try:
            heard = r.recognize_google(audio)
            return heard
        except:
            return None
        

if __name__ == "__main__":
    print('Beginning to listen...')
    user_words = listen()
    print(user_words)