#7.2 Write a program that prompts for a file name, 
#then opens that file and reads through the file, 
#looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point 
#values from each of the lines 
#and compute the average of those values and 
#produce an output as shown below. 
#Do not use the sum() function or a variable 
#named sum in your solution.
#mbox-short.txt

count = 0
idafa = 0
idafa = float(idafa)
fname = input("Enter file name")
if fname == "mbox":
    fo =open("mbox-short.txt")
    for line in fo:
        if line.startswith("X-DSPAM-Confidence:"):
            num =float(line[20:26])
            idafa = num + idafa
            count = count + 1
print(idafa/count)











count = 0

zael = input('enter file name')

if zael == "mbox":
    waje = open("mbox-short.txt")
    for line in waje:
        count = count + 1
        
        if line.startswith("X"):
            b = line[1:] #when the number is to the left of the colin "1:" it removes the first character and begins the rest till the end of the line
            c = line[:5] #when the number is the the right of the colin":5" it prints out the first 5 characters
            print(line.strip().upper())

print("test", b)
print("test 2" , c )
print(count)


