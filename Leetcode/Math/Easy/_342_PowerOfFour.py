
def isPowerOfFour( n: int) -> bool:
    
    if n<=0:
        return False
    while n%4==0:
        n//=4
    
    return n==1


     


n = 5
res = isPowerOfFour (n)
print(res)