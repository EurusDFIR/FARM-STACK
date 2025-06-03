
def isPalindrome(s: str) -> bool:
    s = [x.lower() for x in s if x.isalnum()]

    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
       
        left+=1
        right-=1
       
            
    return True

    # s = ''.join(s)



s = "0P"
res = isPalindrome(s)
print(res) 