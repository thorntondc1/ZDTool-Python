import re

def GrabURL():
    url = input("Please enter URL for parsing:")
    id1 = re.findall("\d+",url)
    print(id1)

GrabURL()