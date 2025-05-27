class Solution: 
    def binary_to_dec(self,x:int)->int:
        
        temp = x
        #1010 -> 10
        res=0
        i=0
        while(temp!=0):
            
            
            res += (temp %10)* (2**i) 
            i=i+1
            temp//=10
        return res
    def dec_to_binary(self,x: int)-> int:
        
        temp = x
        l = []
        if temp ==0:
            return "0"
        while(temp >0):
            r = temp % 2
            l.append(r)
            temp //=2
        l.reverse()
        return "".join(map(str,l))



    def addBinary(self,a:str,b:str)->str:

        res1= self.binary_to_dec(int(a)) + self.binary_to_dec(int(b))
        res1= str(self.dec_to_binary(res1))
        return res1

def main():
    a= "1010"
    b="1011"
    test = 17

    sl = Solution()
    res = sl.addBinary(a,b)
    print(res)
if __name__ == '__main__':
    main()