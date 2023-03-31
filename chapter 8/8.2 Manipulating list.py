#Concatenating list Using +
#We can create a new list by adding two existing lists together

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#list can be sliced using ":"

t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#Building a list from scratch
#We can create and empty list and then add elements
#using the append method
#The list stays in ordeer and new elements are added at 
#the end of the list

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

#Is something in a list?
#Python provides two operators that let you 
#check if an item is in a list, These are logical operators
#that return True or False, they do not modify the list

some = [1,9,21,10,16]
if 9 in some:
    print("We found 9")

if 15 in some:
    print("We found 15")
elif 15 not in some:
    print("15 Not found")
some.append(20)
print("20 was added to the list")
some.append(15)
print("15 was added to the list")
if 20 not in some:
    print("20 was not found in the list")

elif 20 in some:
    print("20 found in the list")

print(some)

#Lists are in Order
#A list can hold many items and keeps those items in the order
#until we do something to change the order
#A list can be sorted(change its order) , the 
# "sort" method means sort yourself

friends = ['Joseph' , 'Glenn' , 'Sally']
friends.sort()
print(friends)

print(friends[1])

#built in Functions and lists, there are a number
#of functions built into Python that take lists as parameters


nums = [3, 41, 12, 9, 74, 15]
print (len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print (sum(nums)/len(nums))

numlist = list()  #creates a empty list
while  True:
    inp = input("Enter a number:")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)
    print(numlist)

average = sum(numlist) / len(numlist)
print('Average' ,average)


total = sum(numlist)
minimum = min(numlist)

print (total)
print (minimum)