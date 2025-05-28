# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:

# Input: n = 2
# Output: false
 

# Constraints:

# 1 <= n <= 231 - 1


def sumDigitSquare(n:int)->int:
    s=0
    while n>0:
    
        t=n%10
        k = t**2
        s+=k
        n//=10
    return s
def isHappy (n:int )->bool:
    st = set()
    while sumDigitSquare(n)!=1:
        next_n = sumDigitSquare(n)
        if next_n in st:
            break
        else:
            st.add(next_n)
        n=next_n
    return True if sumDigitSquare(n) ==1 else False

n = 2
res = isHappy(n)
print(res)
