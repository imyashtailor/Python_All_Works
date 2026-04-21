st = "East or west Masala is best"
# con = 'ß'

#print(len(st)) # len() :- return the length of the string.

#print(st.lower()) # lower() :- convert all characters string into small letter

#print(con.casefold()) #casefold() :- convert other languages symbol like(german language like zetta) ne pn convert kare.

#print(st.upper()) #:- convert all characters string into Capital letter

#print(st.capitalize()) #:- first character of string is capital

#print(st.title()) #:- convert the first character of each word string to Uppercase

#print(st.strip()) #:-  remove whitespaces at the begining and at the ending

#print(st.replace("a","r",2)) # :- replace a substring with another string


#print(st.find("w")) #:- searches for a substring and return the index of first position

#print(st.startswith("E")) #:- check if the string starts with specified substring.

#print(st.endswith("s")) #:- check if the string ends with specified substring.

#print(st.split(" ")) #:- split the string into a list of substring.

#print(st.split("a")) #:- particular word thi pn split kari sakiye che

# k = 'A'
# print(k.join("xyz")) # :- joins the strings into a single string

#print("abc".isalpha()) #:- return true if all characters in strings are alphabetical otherwiese false.
#print("2312".isdigit()) #:- return true if all characters in strings are digit(number) otherwise fasle.
#print("abc12".isalnum()) #:- return true if all characters in string are alphanumeric

#print("abcd".zfill(7)) #:- pads the string with zero(0) on the left string reaches specified length.

#print("abc".center(8,'|')) #:- half half way ma pachi center

#Slicing concept
st1 = "SunrisesinEast"

# print(st1)
print(st1[2:])
print(st1[:5])
# print(st1[2:5])
# print(st1[-5:-1])
# print(st1[1:9:2])
# print(st1[::-1])

# a = 'Hello'
# print(a*2)

# b = 'hel'
# print(b.join('hel'))