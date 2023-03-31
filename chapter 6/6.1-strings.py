fruit = "banana"

lenfruit = len(fruit)

print(lenfruit)


#looping through strings

fruit = "banana"
for letter in fruit:
    print(letter)

fruit = "banana"
index = 0

while index < len (fruit):   #as long as index is less than the len of fruit
    letter = fruit[index]    #this is saying put index[]is a iterable , connect the iterable fruit with the iterable index
    print(index, letter)
    index = index + 1     #add 1 to the index iterable

print ('finish')


city = 'Baltimore'

block = 0

while block < len(city):
    element = city[block]

    block = block + 1

    print(element, block)




#looping and counting 

word = 'banana'
count = 0 
for letter in word:
    if letter == 'a':
        count = count + 1

print (count)


#looking deeper into 'in'




s = 'Monty Python'

print (s[0:4])
print (s[6:8])



#Using in as a logical operator 


plane = "southwest airlines"

"f" in plane
if False:
    print("letter not found")

"p" in plane 
if True:
    print ("letter found")



Marriage = "I'm in love with two women their names are Haoua and Khayriyyah, I believe InshAllah I'll have 4 wives"

ring = 10

while ring < len(Marriage):
    wives = Marriage[ring]
    ring = ring + 1
    print(ring, wives)

