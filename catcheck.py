import time
import random
import msvcrt

def password_with_stars(prompt=""):
    print(prompt, end="", flush=True)
    chars = []

    while True:
        ch = msvcrt.getch()

        if ch in (b"\r", b"\n"):  # Enter
            print()
            break

        elif ch == b"\x08":  # Backspace
            if chars:
                chars.pop()
                print("\b \b", end="", flush=True)

        else:
            chars.append(ch)
            print("*", end="", flush=True)

    return b"".join(chars).decode("utf-8", errors="ignore")


CAT = r"""
 /\_/\  
( o.o )   meow?
 > ^ <
"""

HAPPY_CAT = r"""
 /\_/\  
( ^_^ )   meow~!
 > ^ <
"""

SAD_CAT = r"""
 /\_/\  
( o.O )   ...?
 > ^ <
"""

thinking_phrases = [
    "meow... checking",
    "tap tap... keyboard",
    "hmm... suspicious",
    "sniff sniff...",
    "mrrr... thinking"
]

happy_phrases = [
    "meow~! purr purr!",
    "access granted, human!",
    "purrr~ correct!",
    "you may pass 😼"
]

sad_phrases = [
    "confused meow...",
    "nope, try again",
    "the cat tilts its head",
    "huh?"
]

correct_password = "meow123"
attempts = 3

print("🐱 A fluffy cat is guarding the system...")
print(CAT)

while attempts > 0:
    password = password_with_stars("🔐 Enter password: ")

    print("\n🐾", random.choice(thinking_phrases), end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\n")

    if password == correct_password:
        print(HAPPY_CAT)
        print("😺", random.choice(happy_phrases))
        print("✅ Access granted!")
        input("\nPress Enter to exit...")
        break
    else:
        attempts -= 1
        print(SAD_CAT)
        print("🙀", random.choice(sad_phrases))
        print(f"❌ Attempts left: {attempts}")

        if attempts == 0:
            print("\n🐱 The cat gives up...")
            print("🔒 Access denied.")
            input("\nPress Enter to exit...")