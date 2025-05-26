# Đề: Có một sàn kích thước 2 x n, 
# bạn có các viên gạch kích thước 2 x 1. Hỏi có bao nhiêu cách để lát kín sàn?

def tiling_prob(x: int)->int:
    
    f= [0] * (x+1)

    f[1]=1
    f[2]=2
    for i in range(3, x+1):
        f[i]=  (f[i-2] + f[i-1])
    return f[x]

x = 3
res = tiling_prob(x)
print(res)
