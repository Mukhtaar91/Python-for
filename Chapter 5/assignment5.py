#5.2 Write a program that repeatedly prompts a user for 
# integer numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an 
# appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None


while True:
    inp = input("Enter numbers")
    if inp == "done": break
    try:
        int_input = int(inp)
        if largest is None or largest < int_input:
            largest = int_input
        
        if smallest is None or smallest > int_input:
            smallest = int_input
        


    

    except: 
        print('Invalid')
        continue
print(smallest)
print(largest)
        
    

