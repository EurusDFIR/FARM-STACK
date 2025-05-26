# 4. Staircase Problem (biến thể)
# Đề: Bạn có thể bước 1, 3 hoặc 5 bậc mỗi lần. Có bao nhiêu cách để leo lên bậc n?

def stairCase(n:int)->int:
     
    f = [0]*(n+1)
    f[1] = 1
    f[3] = 2
    f[5] = 5

    for i in range(6,n+1):
          f[i] = f[i-5]+f[i-3]+f[i-1]
    return f[n]

n  = 5
res = stairCase(n)
print(res)