
def countOperations(num1: int, num2: int) -> int:
    cnt=0
    temp = num2+num1
    while temp >0:
        if num1 < num2:
            if num1==0:
                 break
            num1 = num1
            num2= num2 - num1
            cnt+=1
            # print(num1,num2,cnt)
        elif num1>num2:
            if num2==0:
                 break
            num1 = num1 - num2
            num2 = num2
            cnt+=1
            # print(num1,num2,cnt)
        if num1==num2:
                num1 = num2-num1
                if num1 ==0:
                    cnt+=1
                    # print(num1,num2,cnt)
                    break
        temp-=1
    return cnt
num1 = 1
num2 =0
res = countOperations(num1,num2)
print(res)
                
        