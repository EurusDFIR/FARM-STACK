
def countEven( num: int) -> int:
    cnt=0
    for i in range(2,num+1):
        s=0
        while i >0:
            s+=i%10
            i//=10
            
        if s%2==0:
            cnt+=1

    return cnt

num = 4
res = countEven(num)
print(res)