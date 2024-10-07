str1 = "Python"
str2 = "Is Interesting!"

# String concatenation 
finalStr = str1 + " " + str2
print(finalStr)

# Lenth of a String
print("The length of the above string is:",len(finalStr))

#To Lower Case
print("The string converted to lower case is:",finalStr.lower())

#To Upper Case
print("The string converted to Upper case is:",finalStr.upper())

#replace string
str3 = str2.replace("Interesting", "Awesome")
newStr = str1 + " " + str3
print("Replaced string is:", str1 + " " + str3)

#Print each word in the string using split
print("Total number of words in new string is", newStr.split())

#Print stripped sentence without space
stripStr = "   DevOps is my passion !!!   "
print("The stripped sentence is", stripStr.strip())

#Find a substring in a string
subStr = "passion"
if subStr in stripStr:
    print(subStr, "Has been found in the string: ", stripStr.strip())

#count number of occurrences
countStr = "I eat oats everyday. Eating oats keeps me healthy!"
print("Number of occurences of the word oats is: ", countStr.count("oats"))

#check if free is found in the text
newSent = "Nothing in life comes for free!"
print("free" in newSent)

if "free" in newSent:
  print("Yes, 'free' is present in the sentence:", newSent)

if "oats" not in newSent:
  print("No, 'Oats' is present in the sentence:", newSent)

#replace
repStr = "Learning Python is tough!"
print(repStr.replace("tough", "easy"))

#Concat string and numbers
age = 22
ageSent = f"I am always {age} at heart!"
print(ageSent)

floatSent = f"I am always {age:.2f} at heart!"
print(floatSent)

#Escape characters
print("I love playing \"Volleyball\"!")