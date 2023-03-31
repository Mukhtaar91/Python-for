#Tuples are anotehr kind of sequence that fucntions
#much like a list they have elements which are indexed
#starting at 0

x = ('Gleen', 'Sally ', 'Joseph')

print(x[2])

y = (1,9, 2)

print(y)

print(max(y))

for iter in y:
    print(iter)

#unlike a list, once you create a tuple, you cannot 
#alter its conetent-similar to a string

x = [9,8,7]

x[2] = 6

print(x)

try:
    y = 'ABC'
    y[2] = "D"

    z = (5,4,3)
    z[2] = 0
    
except:
    print("Tuples are immutable")


#Tuples and assignment
#we can also put a tuple on the left-hand side of an 
#assignment statement , we can even omit the parentheses

(x,y) = (4, 'fred')
print(x,y)

(a,b) = (99, 98)
print(a)

#tuples and dictionaries
#the items() method in dictionaries returns a list of 
#(key, value)tuples

d = dict()
d ['csev'] = 2
d['cwen'] = 4 
for (k,v ) in d.items():
    print(k,v)

tups = d.items()
print(tups)

#Sorting list of tuples, We can take advantage of the 
#to sort a list of tuples to get a sorted version of a dictionary
#first we sort the dictionary by the key using the items() method
#and sorted()function


d = {'a': 10, 'b':1, 'c':22}

d.items()
#dict_items([('a', 10)('c', 22) ('b',1)])

sorted(d.items())


#using sorted()
#we can do this even more directly using the built-in-function sorted
#that takes a sequence as a parameter and returns a sorted sequence

d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t)

for k,v in sorted(d.items()):
    print(k,v)

#sort by values instead of key
#if we could construct a list of tuples of the form
#(value,key) we could sort by value, we do this with a for
#loop that creates list of tuples


c = {'a':10, 'b':1, 'c':22}
tmp = list()

for k, v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse = True)
print(tmp)

#the top 10 most common words

fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()

for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted (lst, reverse = True)

for val, key in lst[:10]:
    print(key,val)

#^ done in one line of code

c = {'a':10, 'b':1, 'c':22}

print(sorted([(v,k) for k,v in c.items()]))

#list comprehension creates a dynamic list. in this case
# we make a list of reversed tuples and then sort it.


