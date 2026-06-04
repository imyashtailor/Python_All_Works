#Match :- begining ma je string hoi te j match karse
#search :- koi pn ne find kare
#findall :- baddha matches ek sathe aape (content aape)
#non-overlaping string ne find karva mate and ae string ne extract kare che and result list and tuple format ma aape che.
#finditr :- one by one print kare (position aape)
#sub :- replace kare string ne 
#split :- seperate kare words or character


#What is Regex(Regular Expression) :- it is highly specialized sequeced of character that forms a search pattern
#used to find, match, validate or manipulate text that is known as regular expression
import re

st = "sun in evening at in most"


# k = re.match("sun",st)
# k = re.search("at",st)
# k = re.findall("in",st)
# k = re.finditer("in",st)
# print(next(k))
# print(next(k))

# k = re.sub("s","t",st)
# print(k)

#space thi split kare
# k = re.split(" ",st)
# print(k)

# k = re.split("eve",st)
# print(k)

#Match character and usages

# k = re.search("H.l","Hello Python") #DOT(.) => only one character hovo joye
# k = re.search("H.l","Hl0lo Python") # output :- None

# k = re.search("^Hello","Hello Python") #caret(^) => Matches the start of the string
# k = re.search("^Python","Hello Python") # output :- None

# k = re.search("Python?","Hello Python") #Doller($) => Matches the end of the string
# k = re.search("Hello$","Hello Python") # output :- None

# k = re.search("Ja*v","Java Hello Python") #Aestrick(*) => zero or more repetitions of the preceding
# pehla no character 0 or more time aave
# k = re.search("re*t","Java Hello Python") # output :- None (koi word exists ni hoi to error aape)

# k = re.search("Ja+v","Jaaaaaaaaava Hello Python") #Plus(+) => Matches one or more repetitions of the preceding
#pehla no character ochama ocho ek vakaht aavo joye
# k = re.search("Ja+v","J Hello Python") # output :- None

# k = re.search("Hello?","Hello World") #Question_Mark(?) => Mathces zero or one occurence of the prcedece element
# k = re.search("Hello?t","Hello World") # output :- None

# k = re.search("[aeiou]","Hello World") #[] => Matches any of the characters inside the bracket

#[-] (hyphen) :- defines the range inside the square brackets
# parentheses() :- groups expressions and captured match parts
#abc(+) group expressions and captured match parts (group bananva mate)

#word boundray
#ae words ni start and end find karva mate use thy.
k = re.findall(r"\bpython\b","hello python bro")
print(k)

