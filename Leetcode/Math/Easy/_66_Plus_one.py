def plusOne(digits:list[int])->list:
    

    for i in range(len(digits)-1, -1,-1):
        # 1,2,3,9 -> 1,2,3,10
        if digits[i]<9:
            digits[i]=digits[i]+1
            break
        
        elif digits[i]==9:
            digits[i]=0
    if all(i==0 for i in digits):
        digits.insert(0,1)
            

    return digits
#9,9 -> reverse iterative 9,9 check =9 digits[i] =0 -> 0,0 append 1 -> 0,0,1
#reverse 1,0,0
# 1,2,4,9 -> reverse iterative 9,4,2,1 -> 9 ->10
        
      
    
               
   

digits = [8,9,9]
res = plusOne(digits)

print(res)

