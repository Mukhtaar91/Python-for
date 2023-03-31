
#returns a handle use to manipulate the file
#a handle is a portgole between your program and this file
#that's sitting on the disk.
#filename is a string
#mode is optional and should b "r" if we are planning to
#read the file and "w" if we are going to write to the file









aws = open('Arabic.tx',"r" , encoding='utf_8')

for line in aws:
    if line.startswith('1889'):#startswith()
        line = line.strip() #strip remove whitespaces
        print(line)




count = 0
for line in aws:
    count = count + 1

print('Line Count:' , count)

inp = aws.read()

print (inp)







#A file handle open for read can be treated as a sequence of strings
#where each line in the file is a string in the sequence
#we can use the for statement to iterate through a sequence 
#Remember a sequence is an ordered set







#We use a special character called the "newline" to indicate
#when a line ends we represent it as \n in strings
#Newline is still one character not two within python program

stuff = 'Hello\nWorld!'

print (stuff)

size = len(stuff)

print(size)




aws = open('Arabic.tx', 'r', encoding='utf_8')

for aw in aws:
    aw = aw.strip()
    if not aw.startswith('1999')  :
        continue

    print(aw)

#if not 

aws = open('Arabic.tx', encoding='utf_8')
for aw in aws:
    aw.strip()

    if not '1500' in aw: # if 3000 is not in the line skip
        continue
    print(aw)



#Prompt for file name


fname = input('Enter language')
if fname == 'Arabic':

  fhand =  open('Arabic.tx', encoding='utf_8')
count = 0
for line in fhand:
    line.strip()
    if line.startswith('3000'):
        count = count + 1

print ('There were', count, 'subject lines in' , fname)

fname = input ('Enter language')

try:
    if fname == 'Arabic':

        fhand = open('Arabic.tx', encoding='utf_8')
except:
    print('File cannot be opened', fname)
    quit()

count = 0
for ilne in fhand:
    
    if line.startwith('19'):
        count = count + 1
print('There were', count, 'subject line in', fname)


