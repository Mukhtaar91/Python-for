#5.2 Write a program that repeatedly prompts a user for 
# integer numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.




#The None keyword is used to define a null value, or no value at all.
#None is not the same as 0, False, or an empty string. 
 #None is a data type of its own (NoneType) and only None can be None.
 # None data type doesn't contain a value
#if the number entered is less than n (None) this will start with the large



#set a prompt to enter a series of numbers and output the largest and smallest of numbers


small = None
large = None

while True:
    input_ls = input('Enter numbers')
    if input_ls == 'done': break


    try:
        int_ls = int(input_ls)

        if large is None or large < int_ls:
            large = int_ls

        if small is None or small > int_ls:
            small = int_ls

    






    except:
        print ('Invalid')
        continue
    

    

print(large)

print(small)










#finding the average number in a list of numbers

count = 0

total = 0

value = [43,66,90,91,34,60]

for values in value:
    count = count + 1
    total = total + values

print("The average of the numbers listed is ",total/count)

