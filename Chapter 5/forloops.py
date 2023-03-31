#A simple Definite Loop
#to loop over somthing in a for loop, that something is called a Iterable
#the process of looping over the elements is called iterating



# A sequence is and iterable, with a clear order to the components
#commoon sequences : list, tuples, , strings, bytes

        #iterable                                                                              #Everything between the for look iteration
                                                                                        #and the deidented , is aprt of the iteration process 
for i in [5, 4, 3, 2, 1] :    #makes contract for the iteration variable i
    print (i)           # goes through the contracts and prints it
    
print('Blastoff')


kids = ['Zahir', 'Zubayr', 'Zakai', 'Zuleikha', ] #makes a variable called kids containing a list

                                                              #makes a contract called kid from the above variable "kids"
for kid in kids:
    if kid == (input):


        print('8/2/2014') 


for L in ('Zahir'):  # the word 'Zahir' alone is iterable by letter 
    print(L)       #this prints the letters vertically from top to bottom

        #b outputs the bytes of the string 
for byte in b'Binary':
    print(byte)  #will print out the ASCII codes for each letter


#for digits in 96693: # intergers are not a iterable object
    #print (digits)    # this will not execute you will get a error message

c = 96693             #assigns numbers to a variable
    #assigns int to (d)   for d (d is the iterable) in the ieration of the string (c) this entire argument is assinged to digits (variable)
digits = [int(d) for d in str(c) ]

for digit in digits:           #for variable iterable "digit" in digits iteration process
    print(digit)                #print digit



#finding the largest number in a list


largest_so_far = -1

print ('Before' , largest_so_far)
                   #iterable
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:   #if the iteration process of "the_num" determines the iterable to be larger than "largest_so_far" -1
        largest_so_far = the_num   #because the above statement is true, the_num os assigned to largest_so_far

    print (largest_so_far, the_num)  

print ('after' , largest_so_far)


#counting in a loop

zork = 0 

print ('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :  
    zork = zork + 1   # this is apart of the iteration process    
    print (zork, thing)
print ('After' , zork)



#Summing in a loop

zork = 0                    #zork = 0
print ('Before' , zork)     #print zork= 0
for thing in [9, 42, 12, 3, 74, 15] :  
    zork = zork + thing       #zork = 0 + each iterable element^
    print (zork, thing)      # 0+9 zork is now 9, 9 + 42 , zork is now 51, the iteration process ends at 15

print ('After' , zork)



kids_birthday = ("8/2/2014", "4/17/2016", "8/5/2018", "4/22/2022")  

#for kid in kids_birthday:
    #print(kid)


looper = iter(kids_birthday)

while True:
    try:
        kid = next (looper)
        print(kid)
    except StopIteration:
        break


        
#counting in a loop



#Summing in a loop, totalling up all the iterable objects in a list

total = 0

tickets = [566, 523, 678, 903, 533, 1056, 7642, 109]

for ticket in tickets:
    total = total + ticket
    

print ('the total of all number added is' ,total)


#finding the average number in a list of numbers

count = 0

sum = 0 

values = [567, 332, 23, 5, 7, 8, 44, 33, 108, 678, 16, 1089]

print ('Before' , count, sum)

for value in values:
    count = count + 1
    sum = sum + value

print("The sum of total values is ", sum/count)


#filtering in a loop looking for a particular number in a loop

kids = [8, 6, 4, 2,]

for kid in kids:
    if kid >= 3:

        print (kid)



#


    
