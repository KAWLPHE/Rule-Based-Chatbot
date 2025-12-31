"""
Rule-Based Chatbot
Author: Isomiddin

Description:
A simple rule-based chatbot that responds to user input
using predefined patterns and fallback logic.
"""

import random


# Knowledge base (rules)
RESPONSES = {
    "greeting": {
        "keywords": ["hi", "hello", "hey"],
        "answers": [
            "Hello! How can I help you?",
            "Hi there!",
            "Hey! What can I do for you?"
        ],
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you"],
        "answers": [
            "Goodbye! 👋",
            "See you later!",
            "Take care!"
        ],
    },
    "name": {
        "keywords": ["your name", "who are you"],
        "answers": [
            "I'm a simple rule-based chatbot 🤖",
            "You can call me RuleBot."
        ],
    },
    "help": {
        "keywords": ["help", "what can you do"],
        "answers": [
            "I can chat with you using simple rules.",
            "Try greeting me or asking who I am."
        ],
    },
}

FALLBACK_RESPONSES = [
    "Sorry, I didn't understand that.",
    "Can you rephrase your question?",
    "I'm still learning. Try something else!"
]


def normalize_text(text: str) -> str:
    """Normalize user input."""
    return text.lower().strip()


def get_response(user_input: str) -> str:
    """
    Find a response based on predefined rules.
    Returns a random matching answer or a fallback response.
    """
    text = normalize_text(user_input)

    for rule in RESPONSES.values():
        for keyword in rule["keywords"]:
            if keyword in text:
                return random.choice(rule["answers"])

    return random.choice(FALLBACK_RESPONSES)


def chat() -> None:
    """Start chatbot conversation."""
    print("=" * 45)
    print("🤖 RULE-BASED CHATBOT")
    print("Type 'exit' to quit")
    print("=" * 45)

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")


def main() -> None:
    chat()


if __name__ == "__main__":
    main()
