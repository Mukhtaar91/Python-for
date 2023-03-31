#list constants
#List constants are surrounded by square
#brackets and the elements in the list are
#seperated by commas, A list element can be any python 
#object - even another list, A list can be empty


print([1, 24, 76])

print(["red", "yellow", "blue"])

print(["red", 24, 98.6]) # different kinds of elements in a list

print([1, [5,6], 7])  #list within a list

print ([])

#looking inside list, just like string, we can get at any
#element in a list using an index specified in square brackets

#looking inside a list
friends = ['Joseph', 'Glenn', 'Sally' ]
print(friends[1])


#list are mutable(meaning you can changle whats inside the list)


#fruit = "Banana"  #strings are not mutable
#fruit [0] = "b"
        

#mutable list
lotto = [2,14,26,41,63]
print(lotto)

lotto[2] = 28  #[2,24,28,41,63]
print(lotto)

#how long is a list?

greet = "Hello bob"
print(len(greet))

x = [1,2, "joe", 99]
print(len(x))

#Using the range function,the range function returns a list 
#of numbers that range from zero to one less than the parameter
#We can construct an index loop using for and an iteger iterator


print(range(4))

friends = ["Joseph", "Glenn", "Sally"]
print(len(friends))

print(range(len(friends)))


friends =["Josepsh", "Glenn", "Sally"]
for friend in friends:

    print("Happy New Year:", friend.lower())
print("example 1^")
for i in range(len(friends)):
    friend = friends[i]
    
    print("Happy New Year:", friend.upper())

print ("example 2^")


for i in range(10):
    print(i)

for i in range(1, 10):
    print(i, end = " ")




