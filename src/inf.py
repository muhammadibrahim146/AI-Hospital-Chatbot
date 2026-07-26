
import json
import nltk
import pickle

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

nltk.download("punkt")

with open("../data/intents.json") as file:
    intents = json.load(file)

words = []
classes = []
documents = []

ignore = ["?", "!", ".", ","]

for intent in intents["intents"]:

    for pattern in intent["patterns"]:

        tokens = nltk.word_tokenize(pattern)

        words.extend(tokens)

        documents.append((tokens, intent["tag"]))

        if intent["tag"] not in classes:
            classes.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w not in ignore]

words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

pickle.dump(words, open("../model/words.pkl", "wb"))

pickle.dump(classes, open("../model/classes.pkl", "wb"))

print("Vocabulary Created Successfully")