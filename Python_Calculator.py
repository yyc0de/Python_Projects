# Python Calculator

operator = input("Enter an operator: (+,-,x,/)")
x1 = float(input("What is the first number?: "))
x2 = float(input("What is the second number?: "))

if operator == "+":
    z1 = x1 + x2
    print(f"The sum is {round(z1,2)}!")

elif operator == "-":
    z1 = x1 - x2
    print(f"The difference is {round(z1,2)}!")

elif operator == "x":
    z1 = x1 * x2
    print(f"The product is {round(z1,2)}!")

elif operator == "/":
    z1 = x1 / x2
    print(f"The quotient is {round(z1,2)}!")

else:
    print("Your operator is invalid!")