han = open('mbox-short.txt')

print('Program skipped')

while False:   
    for line in han:
    
        line = line.rstrip()
        print('Line:' , line)
        wds = line.split() #turns each line into a list
        print('Words:', wds)
        #Guardian pattern
    if len(wds) < 1: #if the length or wds is less than 1
        print('No words on this line')
        continue    #skip and or ignore
    if wds[0] != 'From ':

        print('Ignore')
        continue
        (wds[2])






while False:    
    for line in han:
    
        line = line.rstrip()
        print('Line:' , line)

        if line == " ":
            print('skip blank')
            continue
        wds = line.split() #turns each line into a list
        print('Words:', wds)
    
      
        if wds[0] != 'From ':

            print('Ignore')
            continue
        print (wds[2])






while True:
    for line in han:
        line = line.rstrip()
        wds = line.split()
        #guardian in a compound statement, short circuit evaluation
        if len(wds) < 3 or wds [0] != 'From':
            continue
        print(wds[2])