from B1 import tachSo


def minSum7(num:int)->int:
    num = tachSo(num)

    pair1 = num[0]*100 + num[1]*10 + num[2]
    pair2 = num[3]*10 + num[5]
    pair3 = num [4]*10 + num[6]

    return pair1 + pair2 + pair3

num = 1234567
res = minSum7(num)
print(res)

