def arrangeCoins( n: int) -> int:
    s = 0
    if n<=2:
        return 1
    for i in range(n):
        s+=i
        if s>n:
        
            return i-1
        elif s==n:
          
            return i
    return -1


n = 1
res = arrangeCoins(n)
print(res)