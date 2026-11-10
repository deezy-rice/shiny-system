import random
import datetime

history = []

jokes = [
    "Why did the chicken cross the road? To get to the other side!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "What do you call a fish without eyes? A fsh!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts!"
]

def get_response(user_input):
    text = user_input.lower().strip()
    history.append(user_input)

    if text in ["hello", "hi", "hey", "yo"]:
        return "Hello! How are you? Type 'help' to see what I can do."
    elif "how are you" in text:
        return "I'm good! Thanks for asking. How about you?"
    elif "your name" in text:
        return "I'm shiny-system bot, made by deezy-rice!"
    elif "joke" in text:
        return random.choice(jokes)
    elif "time" in text:
        now = datetime.datetime.now()
        return f"Right now it's {now.strftime('%H:%M:%S')} on {now.strftime('%Y-%m-%d')}"
    elif "codm" in text or "call of duty" in text:
        return "CODM is fire! What's your favorite gun? Mine is DL Q33."
    elif "free fire" in text:
        return "Free Fire! Booyah! Who's your main character?"
    elif "history" in text:
        if not history:
            return "You haven't said anything yet."
        return "You said:\n" + "\n".join(history)
    elif "help" in text:
        return """I can do this:
- hello - say hi
- joke - get a joke
- time - get current time
- history - see what you said
- codm / free fire - talk games
- bye - exit"""
    elif text in ["bye", "exit", "quit"]:
        return "Bye! See you later!"
    else:
        return "I don't understand. Type 'help' to see what I can do."

print("=== shiny-system bot ===")
print("Type 'help' for commands, 'bye' to exit")

while True:
    user = input("You: ")
    reply = get_response(user)
    print("Bot:", reply)
    if user.lower().strip() in ["bye", "exit", "quit"]:
        break
