# Python compound interest calculator

Principal = float(input("Enter your initial principal balance: "))

while Principal <= 0 :
    print("Principal amount should be positive!")
    Principal = float(input("Enter your initial principal balance: "))

rate = float(input("Enter the interest rate: "))
rate = rate / 100

while rate <= 0 :
    print("Rate should be positive!")
    rate = float(input("Enter the interest rate: "))

n = int(input("Enter the number of times interest is compounded per year?: "))

while n <= 0:
    print("N should be positive!")
    n = int(input("Enter the number of times interest is compounded per year?: "))

time = float(input("How many years?"))

while time <= 0:
    print("Time should be positive!")
    time = float(input("How many years?"))

amount = float(Principal * (1 + rate/n)**(n*time))

print(f"The total amount is {amount:,.2f}")
