
#The in keyword can also be used to check to see if one  
# #string is "in" another string. The in expression is a
#logical expression that returns True or False and can 
#be used in an if statement



fruit = "banana"

'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit: 
    print('found it!')


#String Comparison





#String Library 

greet = "Hello Bob"

zap = greet.lower()

print (zap)

print (greet)

print ('Hi There' .lower())

#how to make a string lowercase lower()

#object method

hi = 'Asalamu Alaikum'

hi_lower = hi.lower()

print (hi_lower)

print (hi)


#make a object string capital

big = 'welcome to the program'

bigCaps = big.upper()

print(bigCaps)


#check the type of object and what methods it have

stuff = 'Hello world'

type (stuff)

dir (stuff)

#find method

fruit ='banana'
pos = fruit.find('na')

print(pos)


#search and replace the replace() function

greet = 'Hellow Bob'
nstr = greet.replace ('Bob' , 'Jane')
print (nstr)

nstr = greet.replace('o', 'x')

print (nstr)

#to take a string and remove whitespace at the beginning and/ or end
#lstrip() remove whitespace at the left 
#rstrip() remove whitespace at the right
#strip() removes both beggining and ending whitespace

greet = '  Hello Bob     '

lgreet = greet.lstrip()

print(lgreet)

rgreet = greet.rstrip()

print (rgreet)

bgreet = greet.strip()

print (bgreet)


#when you want to know what a line starts with
#when you want to find a word in strings

line = 'Please have a nice day'

line1 = line.startswith('Please')

if line1 is True:

    print ("True")


line2 =line.startswith('Please')

if line2 is False:

    print("False")


    

    
data = 'From Mukhtaar Ishmail.Sajjad@gmail.com/swa July 5 1991'

monk = data.find('@')

print (monk)

zael = data.find(' ' ,monk)

print (zael)


waje = data[monk+1 : zael]

print (waje)





