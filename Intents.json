import json
import random

with open('intents.json', 'r') as file:
    data = json.load(file)

print("Bot: Hello! Type 'quit' to stop")

while True:
    user_input = input("You: ").lower()

    if user_input == "quit":
        print("Bot: Goodbye!")
        break

    found = False
    for intent in data['intents']:
        for pattern in intent['patterns']:
            if pattern in user_input:
                response = random.choice(intent['responses'])
                print(f"Bot: {response}")
                found = True
                break
        if found:
            break
