# Đề: Có một đoạn đường dài n bước.
#  Mỗi lần bạn có thể đi 1, 2 hoặc 3 bước. Hỏi có bao nhiêu cách để đi hết đoạn đường?

def wayToCoVer(x: int)->int:
    f = [0] * (x+1)
    f[1]=1
    f[2]=2
    f[3]=4

    for i in range(4,x+1):
        f[i] = f[i-3] +f[i-2]+ f[i-1]
    
    return f[x]

x = 4
res = wayToCoVer(x)
print(res)
