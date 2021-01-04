def main(num1, num2):
    if num1*num2 > 1000:
        return f"The Product of {num1} and {num2} is:\n{num1 * num2}"

    else:
        return f"The Sum of {num1} and {num2} is:\n{num1 + num2}"


n1 = int(input("Please Enter First Number:\n"))
n2 = int(input("Please Enter Second Number:\n"))
print(main(num1=n1, num2=n2))

print("\n\nAgain Calling To Demonstrate Else Condition\n")
n3 = int(input("Please Enter First Number:\n"))
n4 = int(input("Please Enter Second Number:\n"))
print(main(num1=n3, num2=n4))


print("\n\nPlease Press Enter To Exit The Program")
input("")