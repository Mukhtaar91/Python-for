#One common use of dictionaries is counting how often
#we "see" something


ccc = dict()
ccc ['csev'] = 1
ccc ['cwen'] = 1

print(ccc)

ccc ['cwen'] = ccc ['cwen'] + 1 

print(ccc)


#It is an error to reference a key which is not in the ditionary
#We can use the in operator to see if a key is in the dictionary

ccc = dict()
try:
    print(ccc['csev'])

except:
    
    print("Invalid") 

print("Program 1 end")



#When we encouter a new name, we need to add a new entry in
#the dictionary and if this the second or later time we have seen 
#the name we simply add one to the count in the dictionary under that name


counts = dict()
names = ['csev', 'cwen' , 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
print("Program 2 end")

#The get Method for dictionaries
#the pattern of checking to see if a key is already in a dictionary
#and assuming a default value if the key is not there is so common
#that there is a method called get() that does this for us

if name in counts:
    x= counts [name]
else:
    x = 0

x = counts.get (name, 0)

#Simpliefied counting with get()
#we can use get() and provide a default value of zero when the 
#key is not yet in the dictionary - and then just add one

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts [name] = counts.get(name,0) + 1

print(counts)

print("Program 3 end")