import datetime

print("**--Welcome To Future Teller Program--**")

# Getting Name
name = input("Enter Your Name:\n")
print("\n\n")
# Formatting Name
name = name.title()

# Getting Age
age = int(input(f"{name}, Please Your Age (In Years):\n"))

# Checking That If Age Should Be Between 0 - 150 Years
if age < 0 or age > 150:
    print("Please Enter A Valid Age")
else:
    current_year = int(datetime.datetime.now().strftime("%Y"))
    future_age = current_year + 100
    print(f"{name}, Thank You For Entering Your Information:\n\n")
    print(f"{name}, Your Future Is:")
    print(f"You will be 100 years old on {future_age}")
    print("\n\n\nPlease Press Enter To Exit The Program")
    input("")
