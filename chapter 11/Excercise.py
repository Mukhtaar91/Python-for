fo = input("Enter file")
if len(fo) < 1: fo == "parse.txt"
handle = open("parse.txt")
add = +0
import re
nums = []
regex = '[0-9]+'
try:
    for num in handle:
        match = re.findall(regex,num)
        if match:
            nums.append(int(match))
            print(nums)
            
except:
    print('Invalid')

