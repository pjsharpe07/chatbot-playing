
print('[common func] Loading NLP system...')
import spacy
nlp = spacy.load("en_core_web_md")
print('[common func] NLP system loaded...')



#######################################################
############# guessing the category here ##############
#######################################################


def guess_category(sentence):
    # this is the input sentence
    sentence = nlp(f'{sentence}')

    # all the values we are testing
    testing_values = [
        nlp(u'weather'),
        nlp(u'space'),
        nlp(u'tacos')
    ]

    # list of similarity values
    sim_values = [
        sentence.similarity(x) for x in testing_values
    ] 


    # finding the best match
    best_match_score, best_index = max((v, i) for i, v in enumerate(sim_values))
    return round(best_match_score, 2), testing_values[best_index]


##### for debugging purposes ####
if __name__  == '__main__':
    input = input('What would you like to test? ')
    score, category = guess_category(input)
    print(f'When the input is "{input}"')
    print('Score is', score)
    print('The best category is', category)


