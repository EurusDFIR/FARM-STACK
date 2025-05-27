import math
def mySqrt(x:int)->int:
   # 8
   #sqrt 8 -> 2
   # 1,2,3,4,5,6,7,8
    low = 0
    high = x #8
    while low <= high:
    
        mid= (low + high)//2
        #4
        dble = mid *mid
        
        if dble > x:
                high = mid-1
        else:
                low = mid +1

    return high


x=8
res = mySqrt(x)
print(res)  