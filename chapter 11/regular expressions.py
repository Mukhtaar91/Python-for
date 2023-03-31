names = ["Francois","Mike Whiteney","Sagun Khatri","Nick Francesco","Pickles","K5ANR"]

print('start of progam')

for name in names:
    import re

    #if name is None: continue
    print(name)

    carrot = re.findall("^Fran.+",name)#^looks for first
    dollar = re.findall(".+i$",name)#$ matches name with last
    digit = re.findall('\d.+',name) #\d matches 
    whitespace = re.findall('\S+',name)#\S matches words with whitepsace    
    anyword = re.findall ('\w.+',name)
    c4wsp = re.findall ("\w\w\w\w\s.+", name)
    for statement, result in [("words with digits found", digit),
                              ("words with whitespace found", whitespace),
                              ("word characters", anyword),
                              ("4 characters followed by whitespace", c4wsp)]:
        if result:
            print(statement, result)