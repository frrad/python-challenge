import re

#read data from file
f = open('equality.data', 'r')
inputdata = ""
for letter in f.read():
    if letter != '\n':
        inputdata+= letter
f.close()

#find relevant letters with a regex 
cans = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',inputdata)
# print cans

#join the middle letter of all instances for answer
print "".join([mean[4] for mean in cans])