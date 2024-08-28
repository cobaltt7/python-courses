score = float(input("What's your score? "))

if score >= 100:
    print("You got an A+! 😎")
elif score >= 90:
    print("You got a B! 😊")
elif score >= 80:
    print("You got a B! 👍")
elif score >= 70:
    print("You got a C. 🤔")
elif score >= 60:
    print("You got a D... 😬")
else:
    print("You got an F? 💀")

if 60 <= score <= 100:
    print("You passed normally.")
