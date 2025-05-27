
def climbStairs( n: int) -> int:
        
# 2->2 , 3->3 , 4-> 5 , 5-> 8
    if n==1:
        return 1
    if n==2:
        return 2
    f = [0] * (n+1)
    f[1] =1
    f[2]=2
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]
x=6
res= climbStairs(x)
print(res)
                
