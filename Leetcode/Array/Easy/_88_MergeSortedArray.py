
def merge( nums1: list[int], m: int, nums2: list[int], n: int):
    
    nums1 = [x for x in nums1 if x!=0]
    nums1 = (nums1 + nums2)
    nums1.sort()
    return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


res = merge(nums1, m, nums2, n)
print(res)