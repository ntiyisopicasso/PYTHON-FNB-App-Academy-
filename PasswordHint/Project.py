#Password hint is a script that give you a hint based on the password you entered

#user input password
password = input("Enter your password: ")

#removing spaces before and after password
password = password.strip();

#getting the first character and the last character of password
firstLetter = password[0].upper()
lastLetter = password[-1].upper()

#password hint
print(f"Your password starts with {firstLetter} and ends with {lastLetter}")

rePassword = input("Re- enter password: ")

#if the password is correct
if password == rePassword : 
    print("Correct password!!")

#if the password is incorrect 
else : 
    print(" Incorrect password")