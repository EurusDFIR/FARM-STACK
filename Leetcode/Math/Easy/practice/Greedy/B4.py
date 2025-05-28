from B1 import tachSo


def minSub8(num : int)->int:
    num = tachSo(num)

    pair1 = num[3]*1000 + num[2]*100 + num[1]*10+num[0]
    pair2 = num[4]*1000 + num[5]*100 +num[6]*10 + num[7]


    return abs(pair2 - pair1)

num = 12345678
res = minSub8(num)
print(res)