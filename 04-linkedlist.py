import urllib, re

site = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php")
page = site.read()

next = re.findall('nothing=([0-9]*)',page)[0]

print next

for index in range(1,401):
    site = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+next)
    page = site.read()

    nextCans = re.findall('[0-9]+',page)

    if len(nextCans) == 1:
        next = nextCans[0]
    elif page == "Yes. Divide by two and keep going.":
        next = str(int(next)/2)
    elif page == "There maybe misleading numbers in the \ntext. One example is 82683. Look only for the next nothing and the next nothing is 63579":
        next = "63579"
    else:
        print page
        break

    print next
