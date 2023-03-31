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
import os
fn = "C:\Users\MookS\Desktop\Python World\Learning Python\Python for Everyone\chapter 11\Regular expression.py"
os.path.exists(fn)

hand = open("mbox-short.txt")
for line in hand:
    line= line.rstrip()
    if line.find('From:') >= 0:
        print(line)

print("Second \n Program")

import re  #imports regular expressions

hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search ('From:', line):
        print(line)

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

        
print("Second \n Program")


import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)