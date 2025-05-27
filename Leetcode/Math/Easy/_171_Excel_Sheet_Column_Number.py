
# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701
#AB -> 28
from _168_ExcelSheetColumnTitle import convertToTitle

def titleToNumber(columnTitle: str) -> int:
    kq = 0
    temp = list(columnTitle)
    for c in range(len(temp)):
        
        
            temp[c]=ord(temp[c])-ord('A')+1
            print(convertToTitle(temp[c]))
            kq = kq*26 + temp[c]
            

               
    return kq 
c = "ABC"
res = titleToNumber(c)
print(res)
        