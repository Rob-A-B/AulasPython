import math
def getSqrt(n):
    return math.sqrt(float(n))

s = input("Enter a numerical value: ")

try:
    for i in s:
        if (i.isdigit() or i == "."):
            sType = "nonstr"

    if (sType =="nonstr"):
        print(getSqrt(s))

    else:
        s = "Non numberical value..."


except ValueError as ex:
    print(ex)


else:
    print(s)