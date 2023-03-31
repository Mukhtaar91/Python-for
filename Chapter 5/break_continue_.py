#8/2/2014
#4/17/2016
#8/5/2018
#4/22/2020








kids = ["Zahir", "Zubayr", "Zakai", "Zuleikha"]

print ("Welcome to my program my children")

kidname = input("Enter your name")

for kid in kids:
    
    if kidname == 'Zahir':
        print (kidname, "You were born on 8/2/2014")
        break
        continue
    elif kidname == 'Zubayr':
        print (kidname,"You were born on 4/17/2016")
        break
        continue
    
    elif kidname == 'Zakai':

        print (kidname, "You were born on 8/5/2018" )
        break
        continue
    elif kidname == 'Zuleikha':

        print(kidname, "You were born on 4/22/2020")
        break 
        continue

    else:

        print ('You are not one of my children')
        break
        continue





print("End of loop iteration")

