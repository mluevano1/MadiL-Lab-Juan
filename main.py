name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("Enter your favorite color: ").strip().lower()

if age < 18:
    age_message = "You are still young!"
elif age < 65:
    age_message = "You are in your prime years!"
else:
    age_message = "You have lots of life experience!"

if color == "blue":
    color_message = "Blue is a calm and trustworthy color."
elif color == "red":
    color_message = "Red is bold and energetic."
elif color == "green":
    color_message = "Green is fresh and balanced."
else:
    color_message = f"{color.title()} is a great choice!"

print(f"Hello {name}, you are {age} years old, and your favorite color is {color}. {age_message} {color_message}")