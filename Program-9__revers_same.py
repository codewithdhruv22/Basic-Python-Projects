print("**---Welcome To Number Reverser Program---**")


def reverse_checker(number):
    reverse_num = int(str(number)[::-1])
    print(f"Reverse Number Is : {reverse_num}")
    if number == reverse_num:
        return True
    else:
        return False


num = int(input("Enter Any Number:\n"))
print(reverse_checker(number=num))

print("\n\nPress Enter To Exit The Program")
input("")
