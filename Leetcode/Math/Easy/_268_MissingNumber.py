
def missingNumber( nums: list[int]) -> int:
    # ln = len(nums)
    # nums.sort()
    # temp=0
    # if nums[0] ==0:
    #     temp = nums[-1]+1
    # elif nums[0] !=0:
    #     if nums[0]==1:
    #         return 0
    #     temp = sum(nums)//2 -1
    # for i in range(ln-1):
    #     if nums[i] +2 ==nums[i+1]:
    #         print(nums[i],nums[i+1])
    #         temp = (nums[i+1]+ nums[i])//2

#ways2
    v = [-1] * (len(nums)+1)
    for num in nums:
        v[num]=num
    for i in range(len(v)):
        if v[i] ==-1:
            return i    

    return 0
# [3,0,1]
l = [3,0,1]
res = missingNumber(l)
print(res)