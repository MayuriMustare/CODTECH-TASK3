import random
import nltk
import spacy
from nltk.corpus import wordnet

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined responses for common intents
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later! Take care!"],
    "thanks": ["You're welcome!", "No problem! Happy to help!"],
    "unknown": ["I'm sorry, I didn't understand that. Can you please rephrase?"]
}

# Function to detect intent
def get_intent(user_input):
    # Tokenize and normalize input
    doc = nlp(user_input.lower())

    # Basic keyword-based intent detection
    if any(token.lemma_ in ["hello", "hi","hii","hey"] for token in doc):
        return "greeting"
    elif any(token.lemma_ in ["bye", "goodbye", "see you"] for token in doc):
        return "goodbye"
    elif any(token.lemma_ in ["thank", "thanks","thank you"] for token in doc):
        return "thanks"
    else:
        return "unknown"

# Function to generate a response
def generate_response(intent):
    return random.choice(responses.get(intent, responses["unknown"]))

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I am your AI assistant. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get intent and generate response
        intent = get_intent(user_input)
        response = generate_response(intent)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
