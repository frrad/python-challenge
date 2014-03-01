#read data from file
f = open('ocr.data', 'r')
inputdata = ""
for letter in f.read():
    inputdata+= letter
f.close()


#compute frequency table
dictionary = dict()
for letter in inputdata:
    if not letter in dictionary:
        dictionary[letter] =1
    else:
        dictionary[letter]+=1
# print dictionary

#compute set of low freq letters
match = set()
for (key,val) in dictionary.items():
    if val < 10:
        match.add(key)
# print match

#build string in order from original data
answer = ""
for letter in inputdata:
    if letter in match:
        answer += letter

print answer