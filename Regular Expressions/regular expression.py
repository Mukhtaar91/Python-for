names = ["Francois","Mike Whiteney","Sagun khatri","Nick Francesco","Pickles","K5ANR"]
for name in names:
    import re
    
    carrot = re.findall("^Fran.+",name)#^looks for first 
    print(carrot)                       

    dollar = re.findall(".+i$",name)#$ matches name with last
    print(dollar)                   #letter matching i

    digit = re.findall('\d.+',name) #\d matches 
    print("words with digits found",digit)                     #any name
                                    #with number
    
    whitespace = re.findall('\S+',name)#\S matches words with whitepsace    
    print("words with whitespace found",whitespace)

    anyword = re.findall ('\w.+',name)
    print("word characters",anyword)

    c4wsp = re.findall ("\w\w\w\w\s.+", name)
    print("4 characters followed by whitespace",c4wsp)

    #Regex Quantifiers 

    vowels = re.findall (".+[aeiou]{2}", name)
    print("Character with 2 consecutive vowels ", vowels)

    vr7 = re.findall ("^\w{7}$",name)
    print("7 consecutive word characters",vr7)

    vr72 = re.findall ("^\w{7}", name)
    print("Any name that contains 7 or more", vr72)