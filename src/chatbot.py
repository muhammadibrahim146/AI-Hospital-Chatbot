import json
import random
import pickle
import nltk

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# Load data
with open("../data/intents.json") as file:
    intents = json.load(file)

words = pickle.load(open("../model/words.pkl", "rb"))


def clean(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [stemmer.stem(word.lower()) for word in tokens]
    return tokens


def get_response(sentence):

    tokens = clean(sentence)

    for intent in intents["intents"]:

        for pattern in intent["patterns"]:

            pattern_tokens = clean(pattern)

            if set(pattern_tokens).issubset(set(tokens)) or set(tokens).issubset(set(pattern_tokens)):
                return random.choice(intent["responses"])

    return "Sorry, I don't understand your question."


print("=" * 45)
print("      CityCare Hospital CHATBOT")
print("=" * 45)

print("Type 'exit' to quit.\n")

while True:

    message = input("You : ")

    if message.lower() == "exit":
        print("Bot : Goodbye!")
        break

    response = get_response(message)

    print("Bot :", response)