# name = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# result = len(name)
# result = name.find("s")
# result = name.rfind("a")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# name = name.isalpha()
# result = phone_number.count("-")
# phone_number=phone_number.replace("-","")

# print(help(str))

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


user_name = input("Enter your username: ")


if len(user_name) > 12:
    print("Your username can't be more than 12 characters")

elif not user_name.find(" ") == -1: # you can use ---- elif " " in user_name:
    print("Your username can't contain spaces")

elif user_name.isalpha() == False: # you can use ---- any(char.isdigit() for char in user_name):
    print("Your username can't have digits")

else:
    print(f"Welcome {user_name}!")
