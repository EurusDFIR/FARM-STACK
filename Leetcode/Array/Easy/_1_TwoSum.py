import time

def twoSum( nums: list[int], target: int) -> list[int]:
    l = []

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                l.append(i)
                l.append(j)       
                return l
         
    

    return -1
nums = [2,5,5,11]*1000000
target = 10
start = time.time()
res = twoSum(nums,target)
end = time.time()  
excution = end - start
print(res)
print(f"Thoi gian thuc thi {excution}ms")