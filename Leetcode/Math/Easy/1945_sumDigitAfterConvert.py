

# Input: s = "leetcode", k = 2

# Output: 6

# Explanation:

# The operations are as follows:
# - Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
# - Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
# - Transform #2: 33 ➝ 3 + 3 ➝ 6
# Thus the resulting integer is 6.
def getLucky( s: str, k: int) -> int:
    l = list(s)
    
    for i in range(len(l)):
        l[i] = ord(l[i]) - ord('a')+1
    
    s = "".join(str(x) for x in l)
    s= int(s)
    
    while k>0:
        t=0
        while s>0:
            t +=s%10
            
            s//=10
        s=t        
        k-=1
    return t
s = 'zbax'
k=2
res = getLucky(s,k)
print(res)
