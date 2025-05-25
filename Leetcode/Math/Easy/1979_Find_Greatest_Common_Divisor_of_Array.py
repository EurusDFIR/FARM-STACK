
def findGCD(nums: list[int])->int:
    x = max(nums) # 10
    y = min(nums) #2

    while y!=0:
        x,y = y,x%y 
    return abs(x)

l = [48,55,56,57,60]
res = findGCD(l)
print(res)
            