
def toHex(num: int) -> str:
    st = ''
    
    res =0
    if num <0:
        num = num+ 2**32
    if num==0:
        return "0"
    while num>0:
        st+=conversion_table[num%16]
        num//=16 
    
    return st[::-1].lower()

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
        

num = -2
res = toHex(num)
print(res)