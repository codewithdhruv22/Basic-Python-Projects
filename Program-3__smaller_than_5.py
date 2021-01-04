print("**--Smaller Than 5 Number Finder--**")
print("\n")

# Taking Numbers In A String Form
num_str = input("Please Enter 5 Number Separated By Comma(,):\n")

# Making List of num
num_list = num_str.split(",")

# Taking out the numbers from list which are smaller than 5
print("\n\n")
print("From The Given Numbers")
print("Following Number/s is/are smaller than 5:")

for num in num_list:
    if int(num) < 5:
        print(num)
print("\n\nPress Enter To Exit The Program")
input("")


