
fname = input('Enter file name')
if len(fname) < 1 : fname = 'mbox-short.txt'
handle = open(fname)
d = dict()
lst = list()
try:
    for line in handle:
        line.strip()
        if line.startswith("From "):
            words = line.split()
            times = words[5]
            hours = times[0:2]
            d[hours] = d.get(hours, 0) + 1
    
    for key,value in d.items():
        
        lst.append((key,value))
    lst = sorted(lst)

    for key,value in lst:
        print(key,value)
        
except:
    print('Invalid')