
def removeElement( nums: list[int], val: int) -> int:
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == val:
            del nums[i]


    return len(nums)


nums = [0,1,2,2,3,0,4,2]
val = 2

res = removeElement(nums,val)
print(res)