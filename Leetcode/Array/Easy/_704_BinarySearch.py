def search( nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)
    while l < r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m
        else:

            l = m+1
    

    return -1


nums = [-1,0,3,5,9,12]
target = 2
res = search(nums, target)
print(res)