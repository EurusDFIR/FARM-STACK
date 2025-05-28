from B1 import tachSo


def minMulty(num : int)->int:
    num = tachSo(num)
    pair1 = num[0]*100 + num[2] * 10 + num[4]
    pair2 = num[1]*100 + num[3]*10 + num[5]



    return pair1 * pair2

num = 324561

res = minMulty(num)
print(res)
