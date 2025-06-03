
def searchInsert( nums: list[int], target: int) -> int:
    # for i in range(len((nums))):
        
    #     if target < nums[0]:
    #         return 0
    #     if nums[i] == target:
    #         return i
    #     else:
    #         maxEl = max(nums)
    #         if nums[i] == maxEl:
    #             if target > nums[i]:
    #                 return i+1
                
    #         if target - 1 == nums[i]:
    #             return i+1
    #         elif target + 1 == nums[i]:
    #             return i

    # return -1

    #Ways 2
    l = 0
    r = len(nums)
    while l <r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m+1
        else:
            r = m 
    return l





nums =[1, 3, 5, 6]
target = 7

res = searchInsert(nums,target)
print(res)