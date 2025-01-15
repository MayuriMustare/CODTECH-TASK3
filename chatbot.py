import spacy 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import nltk

# Download NLTK resources
nltk.download('punkt_tab')


# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses (rule-based)
responses = {
    "greet": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "bye": ["Goodbye! Have a great day!", "See you later! Take care!"],
    "name": [" I am an AI chatbot created to assist you with your queries."],
    "age": ["I'm timeless, as I'm just a piece of code!"],
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs!"],
    "Thanks": ["You're welcome!", "No problem! Happy to help!"],
    "default": ["I'm sorry, I didn't understand that. Can you please rephrase?"]
}
# Function to preprocess user input
def preprocess_input(user_input):
    # Tokenization and lowercasing
    tokens = word_tokenize(user_input.lower())
    # Removing punctuation and stopwords
    Stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in Stop_words and word not in string.punctuation]
    return tokens

 # Function to determine intent based on keywords
def get_intent(preprocessed_tokens):
    if any(word in preprocessed_tokens for word in ["hello","hi","hey"]):
        return "greet"
    elif any(word in preprocessed_tokens for word in ["bye","goodbye","see you"]):
        return "bye"
    elif any(word in preprocessed_tokens for word in ["name","who are you"]):
        return "name"
    elif any(word in preprocessed_tokens for word in ["age","old"]):
        return "age"
    elif any(word in preprocessed_tokens for word in ["thanks","thank you"]):
        return "Thanks"
    elif any(word in preprocessed_tokens for word in ["joke","funny"]):
        return "joke"
    else:
        return "default"


# Main chatbot function
def chatbot():
    print("Chatbot: Hello! I am your AI assistant. Type 'exit' to end the chat.")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Preprocess user input
        preprocessed_tokens = preprocess_input(user_input)
        
        # Determine user input
        intent = get_intent(preprocessed_tokens)

        # Fetch response based on intent
        response = responses.get(intent,responses["default"])
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    import nltk
    nltk.download("punkt")
    nltk.download("stopwords")
    chatbot()

    
 
