import my_modules.common_functions as func
import my_modules.speaking as speech
import my_modules.listening as listen
import time

'''
This process will listen through the module listening.py
and speak through the speaking.py
There is some light defense against not understanding

'''
process_active = True

while process_active:

    speech.speak('What would you like to hear about?')
    user_words = listen.listen()

    if user_words is None:
        speech.speak("I'm sorry. I didn't catch that. Try again?")
    elif user_words.lower() in ('goodbye', 'bye', 'adios', 'exit'):
        speech.speak('Exiting process. Have a great day!')
        process_active = False
    else:
        # get category and score
        score, category = func.guess_category(user_words)
        
        # say/do something something
        speech.speak(f'With input: {user_words}')
        speech.speak(f'The category is {category} with score of {score}')
        # initialize process again
        time.sleep(0.5)
