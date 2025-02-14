import spacy

# Loading the correct model
nlp = spacy.load("en_core_web_lg")

# FAQ database
faq_data = {
    "what is your name": "I am a chatbot here to assist you!",
    "how can I contact support": "You can contact support via email at support@example.com.",
    "what is the refund policy": "Our refund policy allows returns within 30 days of purchase.",
    "how to reset my password": "To reset your password, go to the login page and click on 'Forgot Password'.",
    "where is your company located": "Our company is located in New York, USA.",
}


# Function to preprocess text
def preprocess_spacy(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])


# Function to find the best response using word vectors
def get_best_response(user_input):
    user_input = nlp(preprocess_spacy(user_input))  # Convert input to a SpaCy doc

    best_match = None
    highest_similarity = 0.0

    for question in faq_data.keys():
        processed_question = nlp(preprocess_spacy(question))  # Convert question to a SpaCy doc

        # Use .vector_norm instead of .similarity to ensure vectors exist
        if user_input.vector_norm and processed_question.vector_norm:
            similarity = user_input.similarity(processed_question)
        else:
            similarity = 0  # If either vector is empty, set similarity to 0

        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = question

    return faq_data[
        best_match] if best_match and highest_similarity > 0.6 else "Sorry, I don't understand your question."


# Chatbot loop
print("Chatbot: Hello! Ask me anything or type 'exit' to quit.")

while True:
    user_query = input("You: ")

    if user_query.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = get_best_response(user_query)
    print("Chatbot:", response)
