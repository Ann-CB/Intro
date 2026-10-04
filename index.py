print("Hello! I am AI Bot. What's your name? : ")

name = input()

print(f"Nice to meet you, {name}!")

print("How are you feeling today? (good/bad) : ")

while True:

    mood = input().lower()

    if mood == "good":
        print("I'm glad to hear that!")

    elif mood == "bad":
        print("I'm sorry to hear that. Hope things get better soon.")

    else:
        print("I see. Someties it's hard to put feelings into words.")

    if mood == "stop":
        break
print(f"It was very nice chatting with you, {name}. Goodbye!")