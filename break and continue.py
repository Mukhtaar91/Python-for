
#unconditional gem statement break and continue
#used in interative control statements

av = 5
x = int(input("How many candies you want?"))

i = 1
while i <= x:

    if i >av:
        print("We don't have that much I gave you what we have")
        break

    else:
        print("Candy")
        i=i+1


print('Bye')



for i in range(100):
    print(i)
    if i > 5:
        continue
    else:
        print("Hello")
    print("Please come here, I am lonely")


for item in range(1,8):
    if item == 4:
        break #breaks out the loop and returns to the iterative statment
    print (item)



print ("Program finished")


count = 0

inf = input("Enter file name")
if inf == "mbox":
    fo = open("mbox-short.txt")

    count = 0

    for line in fo:
        
        if line.startswith("From "):
            space = line.strip()
            lst = line.split()
            email = lst[1]
            count+=1
            print (email)
            if count == 6:
                print("first 6 lines found")
                break
            

        
        
                
              


print(count)
