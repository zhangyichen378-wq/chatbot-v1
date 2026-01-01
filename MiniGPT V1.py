# Super Mini-ChatGPT with Math Quiz

import random
import datetime

print("Hello! I am Super Mini-ChatGPT 🤖. Type 'exit' to quit.")

user_name = ""

# Predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How's it going?"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Doing well! How about you?", "I'm good, thanks!"],
    "your name": ["I am Super Mini-ChatGPT, your Python assistant."],
    "joke": [
        "Why did the computer go to the doctor? It caught a virus!",
        "Why did the robot cross the road? Because it was programmed to!",
        "Why do programmers prefer dark mode? Light attracts bugs!",
        "Why did the developer go broke? Because he used all his cache!",
        "Why was the computer cold? It left its Windows open!",
        "How do computers eat snacks? They microchip them!"
    ],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "your age": ["I am timeless! ⏳"],
    "fact": [
        "Did you know? Honey never spoils.",
        "Fun fact: Octopuses have three hearts.",
        "Did you know? Bananas are berries, but strawberries aren't.",
        "Fun fact: The Eiffel Tower can be 15 cm taller during hot days."
    ]
}

def ask_math(question):
    """Ask a math question directly from user input"""
    try:
        answer = eval(question)
        user_answer = float(input(f"{question} = "))
        if user_answer == answer:
            print("Super Mini-ChatGPT: Correct! 🎉")
        else:
            print(f"Super Mini-ChatGPT: Wrong! ❌ The correct answer is {answer}")
    except:
        print("Super Mini-ChatGPT: Invalid math expression!")

def random_math_quiz():
    """Generate a random simple math question"""
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])
    question = f"{a}{op}{b}"
    print(f"Super Mini-ChatGPT: Solve this: {question}")
    ask_math(question)

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Super Mini-ChatGPT: Goodbye! 👋")
        break

    # Remember user's name
    if "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip().title()
        print(f"Super Mini-ChatGPT: Nice to meet you, {user_name}!")
        continue

    # Ask current time
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Super Mini-ChatGPT: The current time is {current_time}")
        continue

    # Start a math quiz
    if "quiz" in user_input:
        random_math_quiz()
        continue

    # Math expressions directly
    if any(op in user_input for op in "+-*/"):
        ask_math(user_input)
        continue

    # Predefined responses
    response_found = False
    for key in responses:
        if key in user_input:
            print("Super Mini-ChatGPT:", random.choice(responses[key]))
            response_found = True
            break

    if not response_found:
        print("Super Mini-ChatGPT: Sorry, I don't understand that 😅")
