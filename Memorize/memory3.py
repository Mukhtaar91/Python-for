#use a for loop to prompt each child to enter their name which will return their birth date

    













#Summing in a loop, totalling up all the iterable objects in a list






#5.2 Write a program that repeatedly prompts a user for 
# integer numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number.







#put a set of numbers in order

saka = 0

oranges = [23, 34,66, 91, 44, 1034,]

for orange in oranges:
    saka = saka +1

    print(saka, orange)

print("Counting has fisnished")


smallest = None

largest = None

sl_input = input('Enter Numbers')


while True:

    try:

        int_large_small = int(sl_input)

        if largest == None:
            largest = int_large_small
            break
            continue
        
        elif largest < int_large_small:
            largest = int_large_small
            break
            continue
        if smallest == None:
            smallest = int_large_small

            break
            continue

        elif smallest > int_large_small:
            smallest = int_large_small

            break
            continue
        print(largest, smallest)

        






    except:
        print('invalid input')
