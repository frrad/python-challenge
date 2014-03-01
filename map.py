from string import maketrans

#my way
def fix(input):
    if len(input)==0:
        return ""
    head, tail = input[0],input[1:]
    
    new = ord(head)+2

    if new > 121:
        new -= 26 

    return chr(new) + fix(tail)

#their way
table = maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")

#data
given ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#print [ fix(word) for word in given.split(" ") ]

#print given.translate(table)

#next level
print "map".translate(table)