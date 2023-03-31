#count how many items in a list

large = None
small = None


while True:
    inp = input("Enter number here")
    
 
    if inp == "done":
        break
    

    try:
        int_inp = int(inp)

        if large is None or large < int_inp:
            large = int_inp
        

        if small is None or small > int_inp:
            small = int_inp

    except:
        print("Invalid")
        continue

print("The largest number is ", large)
print("The smallest number is", small)
    





#set a prompt to enter a series of numbers and output the largest and smallest of those numbers


