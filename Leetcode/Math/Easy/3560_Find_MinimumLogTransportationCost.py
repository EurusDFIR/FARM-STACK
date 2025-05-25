

def minCuttingCost(n:int,m:int,k:int)->int:
    len1 =0
    len2 =0
    cost =0

    if n <= k or m <=k:
        # n=6 m=5 , k=6
        # 1,2,3
        # 2,3,2 -> 2
        if n<m:
            len1=k
            len2=m-k
            if len2 <0:
                len2=0
                cost = len1 * len2
            else:
                cost = len1*len2
        
        elif n==m and n<k:
            cost = 0
            
        else:
            if n>m:
                len1 = n-k
                len2 = k
                if len1 <0:
                    len1=0
                cost= len1*len2
              
    else:
        len1 = n-k
        len2 = k
        cost = len1*len2            
    return cost 


n= int(input())
m=int(input())
k = int(input())
res = minCuttingCost(n,m,k)
print(res)