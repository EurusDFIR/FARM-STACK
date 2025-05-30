
def fizzBuzz( n: int) -> list[str]:
    l = []
    a=''    
    for i in range(1,n+1):
        if  i %3 ==0 and i%5==0:
            a='FizzBuzz'
        elif i % 3==0:
            a="Fizz"
        elif i%5==0:
            a="Buzz"
        else:
            a=(str(i))
        l.append(a)


    return (l)
print("")


n = 5
res = fizzBuzz(n)
print(res)