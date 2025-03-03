# Temperature Converter

temp = float(input("What is the temperature?: "))
unit = input("What is the unit?: ( C / F / K ) ").strip().lower()

if unit == "c":
    xunit = input("to ( F / K ) ").strip().lower()
    if xunit == "f":
        conv = ((temp*9/5))+32
        print(f"The temperature is {round(conv,2)} F")
    elif xunit == "k":
        conv = temp + 273.15
        print(f"The temperature is {round(conv,2)} K")
    else:
        print("Invalid input.")

elif unit == "f":
    xunit = input("to ( C / K ) ").strip().lower()
    if xunit == "c":
        conv = (temp-32)*(5/9)
        print(f"The temperature is {round(conv,2)} C")
    elif xunit == "k":
        conv = ((temp-32)*(5/9))+273.15
        print(f"The temperature is {round(conv,2)} K")
    else:
        print("Invalid input. ")

elif unit == "k":
    xunit = input("to ( C / F )").strip().lower()
    if xunit == "c":
        conv = temp - 273.15
        print(f"The temperature is {round(conv,2)} C")
    elif xunit == "f":
        conv = ((temp-273.15)*(9/5))+32
        print(f"The temperature is {round(conv,2)} F")
    else:
        print("Invalid input.")

else:
    print("Invalid input.")