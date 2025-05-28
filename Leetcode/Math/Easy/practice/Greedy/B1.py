# Cho số nguyên dương gồm 6 chữ số.
# Hãy chia các chữ số này thành 2 số mới (mỗi số 3 chữ số, không được bỏ chữ số nào,
#  các số có thể có số 0 ở đầu), sao cho tổng của hai số là nhỏ nhất.
# Ví dụ:
# Input: 123456
# Output: 246 + 135 = 381 (chỉ là ví dụ, bạn hãy tìm tổng nhỏ nhất thực sự)

def tachSo(num: int)->list:
    l = []
    while num>0:
        l.append(num%10)

        num//=10
    l.sort()    
    return l

def tach3(num: int)-> list:
    
    #1 2 3 4 5 6
    num = tachSo(num)
    a = num[0]
    b=num[2]
    c=num[4]
    d = num[1]
    e = num[3]
    f=num[5]

    kq1 = a*100+b*10+c
    kq2= d*100+e*10+f
    print(kq1,kq2)
    return kq1+kq2
if __name__ == "__main__":
    num = 123456
    res = tach3(num)
    print(res)
