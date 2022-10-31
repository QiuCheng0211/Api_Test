
def zhijiao():
    for i in range(1,6):
        for j in range(1,i+1):
            print("*",end="")
        print()
    print()

def dengyao():
    for A in range(1,6):
        for B in range(1,6-A):
            print(" ",end="")
        for C in range(1,A+1):
            print("* ",end="")
        print()

def chengfabiao():
    for A1 in range(1,10):
        for B1 in range(1,A1+1):
            print("{0}*{1}={2}".format(A1, B1, A1 * B1),end=" ")
        print("")
def maopao():
    MP=[10,9,8,4,6,9,11,3,5]
    for i in range(1,len(MP)):
        for j in  range(0,len(MP)-1):
            if MP[j]>MP[j+1]:
                MP[j],MP[j + 1]=MP[j + 1],MP[j]
        print(MP)
    print(MP)


zhijiao()
dengyao()
chengfabiao()
maopao()