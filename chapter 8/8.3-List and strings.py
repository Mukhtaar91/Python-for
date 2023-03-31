#Best Friends: Strings and List
#split() breaks a string into parts produces a 
#list of strings. We think of these as words. We can
#"access" a particular word or look through all the words.


abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])


print (stuff)

for w in stuff:
    print(w)

line = 'A lot             of spaces'
etc = line.split()
print(etc)
#ignores spaces ^

line = 'first;second;third'
thing = line.split()
print(thing)

print(len(thing))

thing = line.split(';') # you can specify a delimiter to chop from split()
print(thing)
print(len(thing))

#when you do not specify a delimiter, multiple 
#spaces are treated like one delimiter you can
#specify what delimiter character to use in splitting




#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue  #if not says all the lines exept line starting with from
    words = line.split()
    print (words[2])
    print(line)


    

        







#The double split pattern, sometimes we split a line one way, and
#then grab one of the pieces of the line and split that piece again

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008




#LIST SUMMARY
#concept of a collection   #slicing lists
#list and definite loops   #list methods:append,remove
#Indexing and lookup       #sorting list
#list mutability           #Splitting strings into lists of words
#Functions: len, min       #using split to parse strings
#max, sum                  
