import pickle

f = open("peak.data","r")
data = pickle.load(f)

for line in data:
    print "".join([draw*times for (draw,times) in line])