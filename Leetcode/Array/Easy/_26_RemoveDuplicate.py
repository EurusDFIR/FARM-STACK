
def removeDuplicates(nums: list[int]) -> int:
    cntFirst = len(nums)

    if len(nums) <=1:
        return 1
    for i in range(len(nums)-1,0,-1):
        if nums[i]== nums[i-1]:
            print(i,nums[i])
            del nums[i]
      
    cntSecond = len(nums)
    cnt = cntFirst - cntSecond
    # print(cntFirst,cntSecond,cnt)
    while cnt >0:
        nums.append('_')
        cnt-=1
    return cntSecond 


nums = [1,1]

res = removeDuplicates(nums)
print(res)

