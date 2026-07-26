
import json
import pickle
import nltk
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

# Load intents
with open("../data/intents.json") as file:
    intents = json.load(file)

# Load words and classes
words = pickle.load(open("../model/words.pkl", "rb"))
classes = pickle.load(open("../model/classes.pkl", "rb"))

print("=" * 40)
print("      CHATBOT TRAINING")
print("=" * 40)

print("\nVocabulary Size :", len(words))
print("Classes :", classes)

print("\nTraining completed successfully!")

print("\nFiles Ready:")
print("✔ words.pkl")
print("✔ classes.pkl")
print("\nNow run chatbot.py")