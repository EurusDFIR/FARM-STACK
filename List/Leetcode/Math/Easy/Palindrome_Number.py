#121 -> 121 true
# -121 -> false

# 10 -> false
class Solution:
    def isPalindrome(self, x:int)->bool:
        
        t=0
        s=x
        if s <=0:
            return False
        else:

            while s>0:
                t=t*10 + s%10
                s//=10
        return False if x!=t else True

def main():
    sl = Solution()
    x = int(input())
    res = sl.isPalindrome(x)
    print(res)
if __name__ == '__main__':
    main()
    