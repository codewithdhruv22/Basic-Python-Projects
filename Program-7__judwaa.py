print("**---Welcome To Judwaa Programm---++")
print("This Program will return True If The "
      "First And Last Number Of List Is Same")
print("\n\n")


def judwaa(commaSepStr):
    num_list = commaSepStr.split(",")
    last_index = len(num_list) - 1

    if int(num_list[0]) == int(num_list[last_index]):
        return True
    else:
        return False


num_str = input("Please Enter Some Numbers"
                " Separated By Comma (,):\n")
print(judwaa(commaSepStr=num_str))
print("\n\nPress Enter To Exit Program")
input("")