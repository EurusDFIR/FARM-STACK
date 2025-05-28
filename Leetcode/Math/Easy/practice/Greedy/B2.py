

from B1 import tachSo

def hieuNhoNhat(num: int)->int:
    num = tachSo(num)

    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    e = num[4]

    res1 = a*100 + b*10 +c 
    res2 = d*10 + e


    return res1 - res2

num = 12345
res = hieuNhoNhat(num)
print(res)