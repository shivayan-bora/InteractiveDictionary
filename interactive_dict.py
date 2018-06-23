import json
# This is to find out similar words to the input given by the user if it doesn't exist in the dictionary
from difflib import get_close_matches

# Loading data from a JSON file
data = json.load(open("data.json"))


def translate_word(word):
    if word in data.keys():
        return data[word]
    elif word.title() in data.keys():
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        flag = input(f"Did you mean '{get_close_matches(word,data.keys())[0]}' instead? Enter 'Y' if yes or 'N' if no: ").strip().upper()
        if flag == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif flag == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter Word: ").strip().lower()

definitions = translate_word(word)

# To check if the output returned by the function translate_word() is a list or a string
if type(definitions) == list:
    for definition in definitions:
        print(definition)
else:
    print(definitions)
