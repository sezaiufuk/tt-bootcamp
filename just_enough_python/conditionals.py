temp = 25


if temp < 23:
    print("A good day for a walk")
elif temp < 30:
    print("Good day for swim")
else:
    print("Find a climate control...")


print("Good for a walk" if temp < 23 else "Good for a swim")
