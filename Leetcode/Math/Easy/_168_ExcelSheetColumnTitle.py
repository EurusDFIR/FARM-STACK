

# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnNumber = 1
# Output: "A"
# Example 2:

# Input: columnNumber = 28
# Output: "AB"
# Example 3:

# Input: columnNumber = 701
# Output: "ZY"
 
def convertToTitle(columnNumber: int) -> str:
    s=""
    while columnNumber >0:
        #28 AB
        columnNumber= columnNumber-1
        phanDu = columnNumber % 26 # 1 B
        s+=chr(phanDu+65) 
        columnNumber//=26
    
    return s[::-1]
c =199999


res = convertToTitle(c)

print(res)


        