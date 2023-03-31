# a collection is more than one thing in a single variable
#Most of our vaariables have one value in them - when we put a
# new value in the variable - the old value is overwritten


x = 2
x = 4

print(x)

# A list is a linear collection of values that stay in order
# A dictionary is a bag of values, each with its own label

#lists index their entries based on the position in the list
#dictionaries are like bags - no order, So we index the things
#we put in the dictionary with a "Look up tag"

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)

print (purse ['candy'] )

purse ['candy'] = purse ['candy'] + 2 
print(purse)

#Comparing list and dictionaries 
#dictionaries are like list except that they syse keys instead of 
#numbers to look up values

lst = list()
lst.append(21)
lst.append(183)
print(lst)

lst[0] = 23

print(lst)




ddd = dict()
ddd ['age'] = 21
ddd ['course'] = 182 
print(ddd)

ddd['age'] = 23

print(ddd)

jjj = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
print(jjj)

ooo = {  }
print (ooo)

