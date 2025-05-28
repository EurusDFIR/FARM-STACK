import math
def isPowerOfTwo( n: int) -> bool:
    
    return True if n & (n-1)==0 else False
n = 3
res = isPowerOfTwo(n)
print(res )
