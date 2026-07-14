# Basic Input&Output
# Description: Student Info Formatter script
# Demonstrates: Input, Type Casting, String Manipulation, Math, and f-strings.

print("=== Student Info System ===\n")

#collecting Strings from user
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")

# Convert input strings to numbers
age = int(input("Enter your age: "))
fav_number = float(input("Enter your favourite number: "))

#Display formatted greeting

full_name = f"{first_name} {surname}"
print(f"\nWelcome, {full_name}!")

print("\n" + "="*40)
print("             STUDENT PROFILE CARD             ")
print("="*40)

#Display name in UPPERCASE and Title Case
print(f"Name (UPPERCASE): {full_name.upper()}")
print(f"Name (Title Case): {full_name.title()}")

#Calculate and display age in months
age_in_months = age * 12
print(f"Age in Months:     {age_in_months} months")

#Round the favourite number to 2 decimal places
rounded_fav_num = round(fav_number, 2)
print(f"Favourite Number:  {rounded_fav_num}")

print("="*40)
print("              DATA TYPE VERIFICATION           ")
print("="*40)

#Print the data type of each collected value using type()
print(f"first_name variable type: {type(first_name)}")
print(f"surname variable type:    {type(surname)}")
print(f"age variable type:        {type(age)}")
print(f"fav_number variable type: {type(fav_number)}")

print("="*40)
