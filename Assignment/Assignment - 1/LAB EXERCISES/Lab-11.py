#Aim :-  Write a Python program to check if a person is eligible to donate blood using a nested if.

#condition :-Age >= 18 and 18 above , weight = 50 or 50 above

age = int(input("Enter the Age = "))
weight = int(input("Enter the Weight = "))

if age < 18 and weight < 50:
    print("Sorry!..You don't apply to blood donation..")
elif age>=18 and weight>=50:
    print("Eligible for Donating Blood")
else:
    print("Not Eligible for Donating Blood")
    