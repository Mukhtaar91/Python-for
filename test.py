names = ['Finn  Bindeballe', 
         'Gear Anders Berge', 
         "HappyCodingRobot", 
         "Ron Cromberge", 
         "Sohil"]
import re
regex = '\w+\s+\w+'

for name in names:
    result = re.search(regex, name)
    if result:
        print(name)