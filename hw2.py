age = int(input("eneter your age "))

def Calc(sum):
    global age
    if (age > 1):
        f1 = 0
        f2 = 1
        sm = 0
        while (age > f2):
            t = f1 + f2
            sm = sm + f2
            f1 = f2
            f2 = t
    elif (age == 1):
        sm = 1
    else:
        print ("no negative numbers, 0 accepted or other symbols then integers accepted")
        age = int(input("enter valid age"))
        sm= (Calc(age))
    return (sm)
print ("sum of Fibbonaci numbers smaller than your age is", Calc(age))

def PCheck(check):
    for i in range (2,int( (check/2)+1)):
        if check%i == 0:
            return True
        else:
            return False

PCheck(age)
if PCheck(age) == True:
    print ("your age is not a prime number")
else:
    print ("your age is a prime number")

def Bin(age):
    print ("your age in binary representation looks like this", end = " -> ")
    binlst = [0,0,0,0,0,0,0,0]
    i = len(binlst)
    while (i != 0):
        if  (age%2 == 0):
            binlst[i-1] = 0
            print (binlst [i-1], end = " ")
        else:
            binlst [i-1] = 1
            print (binlst [i-1], end = " ")
        i += -1
        age = age//2
    
Bin(age)
