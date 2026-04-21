#Aim:-Write a Python program that manipulates and prints strings using various string methods.

st1 = "YashTailor"
st2 = "12345abc"

print(len(st1))
print(st1.lower())
print(st1.upper())
print(st1.capitalize())
print(st1.title())
print(st1.strip())
print(st1.replace("i",'y'))
print(st1.find("l"))
print(st1.startswith("Y"))
print(st1.endswith("r"))
print(st1.split())
print(st1.split("s"))
print(st1.join("12"))
print(st1.isalpha())
print(st2.isdigit())
print(st2.isalnum())
print(st1.zfill(13))
print("yash".center(8,'|'))