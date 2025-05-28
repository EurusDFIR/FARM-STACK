# Bài 3:
# Chia 8 chữ số thành 4 số (mỗi số 2 chữ số) sao cho số lớn nhất trong 4 số là nhỏ nhất.
# Input 1: 12345678
# Một số cách chia: (12, 34, 56, 78), (13, 24, 57, 68), (14, 23, 56, 78), ...
# Testcase mẫu:
# 12, 34, 56, 78 → max = 78
# 18, 23, 45, 67 → max = 67
# Bạn hãy tìm max nhỏ nhất thực sự!
# Input 2: 99887766
# Một số cách chia: (66, 77, 88, 99), (68, 76, 87, 99), ...
# Bạn hãy tìm max nhỏ nhất thực sự!

from B1 import tachSo

def phanDeu (num: int)->int:
    num = tachSo(num)
    pair1 = num[0] * 10 + num[7]
    pair2 = num[1] * 10 + num[6]
    pair3 = num[2] * 10 + num[5]
    pair4 = num[3] * 10 + num[4]

    st = {pair1,pair2,pair3,pair4}
    


    return max(st)

num = 12345678
res = phanDeu(num)
print(res)