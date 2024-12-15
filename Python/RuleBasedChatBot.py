import re

# Define a function to respond to specific questions
def respond_to_question(question):
    # Convert the question to lowercase for case-insensitive matching
    question = question.lower()

    # Define rule-based responses
    if re.search(r'\bwhat is physics\b', question):
        return "Physics is the branch of science that deals with the nature and properties of matter and energy. It seeks to understand how the universe behaves at both macroscopic and microscopic levels."

    elif re.search(r'\bwhat is the universe\b', question):
        return "The universe is everything that exists, including all matter, energy, planets, stars, galaxies, and even the empty space between them. It began with the Big Bang approximately 13.8 billion years ago and is still expanding."

    elif re.search(r'\bwhat is i\b', question) or re.search(r'\bwhat is self\b', question):
        return "In human terms, 'I' refers to the self, the consciousness, and the identity of an individual. It represents the thoughts, experiences, and perceptions that make a person who they are."

    # Default response if the question doesn't match any predefined rules
    else:
        return "Sorry, I don't have an answer to that question. Can you ask something else?"

# Example interaction with the chatbot
print("Hello! Ask me anything.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Goodbye!")
        break
    
    response = respond_to_question(user_input)
    print("Bot:", response)
