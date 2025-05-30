
def isPowerOfThree( n: int) -> bool:
#    return 1162261467%n==0
    if n<=0: return False
    while n%3==0:
        n//=3

    return n==1
n = 27
res = isPowerOfThree(n)
print(res)
