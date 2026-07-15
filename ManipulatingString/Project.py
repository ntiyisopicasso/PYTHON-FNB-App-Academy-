# Taking user inputs 

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
bio = input("write a short bio: ")

#creating username
username = firstName[0] + lastName


#merging firstName and lastName and converting them to title
fullname = f"{firstName} {lastName}"
fullname = fullname.title()


#removing space before and after bio
bio=bio.strip()

#replacing "I am" with "I'm"
bio = bio.replace("i am" , "I'm")

#counting characters in bio
bioLength = len(bio)

#printing results
print("*" *30)

print("\n        Infomation captured     \n")

print("*" *30)
print("\n")
print(f"Your username is: " + username) 
print(f"FullNames: " + fullname)
print(f"Your bio have {bioLength} Characters")
print(f"Short bio about yourself: " + bio)


