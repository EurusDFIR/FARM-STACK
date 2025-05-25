

def isThree(x:int)->bool:
    cnt =0
    l = []
    for i in range(1,x+1):
        if x %i==0:
            cnt+=1
            l.append(i)
    return True if len(l) ==3 else False
x = int(input())
res = isThree(x)
print(res)