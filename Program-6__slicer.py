print("**---Welcome To String Cutter Program---**")

string = input("Enter Any String:\n")

last_index = int(input("Enter The Number "
                       "Till Where You Want "
                       "To Cut Your "
                       f"String {string}:\n"))

if last_index > len(string):

    print(f"Your String ,{string} has only {len(string)}"
          f" character and your give cutter "
          f"string index is - {last_index}\nWhich is not"
          f" acceptable please enter a valid number")
else:
    print("Your Cutter String Is:\n")
    
    # String To Be Removed From String
    to_be_removed_str = string[0:last_index]
    # Replacing Above String With Empty Space
    print(string.replace(to_be_removed_str, ''))
    
    print("\n\nPress Enter To Exit The Program")
    input("")
