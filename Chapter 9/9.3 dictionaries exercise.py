fname = input("Enter file:")
if len(fname) < 1 : fname = 'clown.txt'
hand = open (fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:

        #if the key is not there the  count is 0
        di[w] = di.get(w,0) + 1
        #print(w, 'new', di[w])


#print(di)

largest = - 1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k

print('Done', theword,largest)

