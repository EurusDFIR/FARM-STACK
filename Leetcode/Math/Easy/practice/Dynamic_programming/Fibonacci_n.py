def fibo(n:int)->int:
    # 0,1,1,2,3,5,8
    f = [0] * (n+1)
    if n==0:
        return 0
    if n==1:
        return 1
    
    f[0]=0
    f[1]=1

    for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
        print(f'{f[i]} = {f[i-1]} + {f[i-2]}')
    return f[n]

x=6
res = fibo(x)
print(res)