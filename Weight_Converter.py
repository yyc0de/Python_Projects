weight = float(input("Weight? "))
unit = input("(K)g or (L)bs? ").strip().lower()
if unit == "k" :
    new_weight = (weight*2.20462).__round__(2)
    print("Your weight in pound is " , new_weight)
elif unit == "l" :
    new_weight = (weight/2.20462).__round__(2)
    print("Your weight in kilogram is " + str(new_weight))
else:
    print("Invalid input. Try Again.")

