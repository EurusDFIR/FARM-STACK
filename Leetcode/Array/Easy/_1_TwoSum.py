import time

def twoSum( nums: list[int], target: int) -> list[int]:
    # l = []

    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j] == target:
    #             l.append(i)
    #             l.append(j)       
    #             return l
         
    l = 0
    r = len(nums)-1
 
    while l<r:
        res = nums[l] + nums[r]
        if  res== target:
            return l,r
        elif res > target:
            r-=1
        else:
            l+=1 

    return -1
nums = [2,5,5,11]
target = 10
start = time.time()
res = twoSum(nums,target)
end = time.time()  
excution = end - start
print(res)
# print(f"Thoi gian thuc thi {excution}ms")