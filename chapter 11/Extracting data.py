#Matching and Extracting Data
#re.search() returns a True/False depending on whether 
#the string matches the regular expressions
#if we actually want the matching strings to be extracted
#we use re.findall()


# "^"  Matches the beginning of a line
#  "$" Matches the end of the line
# "." Matches any character
# "\s" Matches whitespace
#  "\S" Matches any non-whitespace character
# "*" Reapeats a character zero or more times
# "*?" Reapeats a character zero or more times (non-greedy)
# "+" Repeats a character one or more times
# "+?" Repeats a character one or more times (non-greedy)
# "[aeiou]" Matches a single charaxcter in the listed set
# "[^XYZ]" Matches a single character not in the listed set
# "[a-z0-9]"
#"(" Indicates where the string excraction is to start
# ")" Indicates where the string excration ss to end


import re
x = "My 2 favorite numbers Are 19 and 42 and 0"
y = re.findall ('[0-9]+ ',x)
print("The digits I found are", y)
#When we use re.findall(), it returns a list of zero
#or more substrings that match the regular expressions
y = re.findall('[AEIOU]+',x)
print("The uppercase vowels found are" ,y)

#Greedy Matching
#The repeat characters(*and+) push outward in both 
# directions(greedy) to match the larest possible string

import re
x= 'From: Using the : charc ter'
y= re.findall('^F.+:',x)
print(y)

#Non-Greedy Matching
#if you add a ? character, the + and * chill chill out a bit
#? gives you the shortest expression
import re
x = "From: Using the: character "
y = re.findall("^F.+?:", x)
print(y)


lst = list()
filename= input("Enter file name")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)
for line in handle:
    line = line.strip()

    if re.findall("^From.+:", line):   #greedy matching
        
        
        lst.append(line)

lst2 = list()
filename= input("Enter file name")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)
for lin in handle:
    lin = lin.strip()
    
    if re.findall("^F.+?:", lin):   #Non-greedy matching
    
        lst2.append(lin)
        

count = 0


for word1, word2 in zip(lst,lst2):
    count  = count + 1
    #print (count,"greedy",word1,count,"non-greedy",word2)
import re
filename= input("Enter file name")
if len(filename) < 1 : filename = "mbox-short.txt"
handle = open(filename)    
try:
      
    for line in handle:
        line = line.rstrip()
        lst = re.findall('^From (\S+@\S+) ', line)
        if len(lst) > 0:
            print (lst)

except:
    print("Invalid")


data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16"
atpos = data.find("@")
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]

print(host)

#double split pattern
line = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split("@")
print(pieces[1])

#The Regular expression Version

import re
lin = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y= re.findall('@([^ ]*)',lin)
print(y)

#'@([^ ]*)'
# ^Look through the string until  you find an at sign
# * < Match many of them

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    
    num = float(stuff[0])
    numlist.append(num)
    
print('Maximum:', min(numlist))

import re
x = "We just received $10.00 for cookies"
y = re.findall('\$[0-9.]+',x)

print(y)

#if you want a special regualr expression character
#to just behave normally(most of the time) you prefix
# it with "\"
