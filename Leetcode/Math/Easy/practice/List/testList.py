l1 = [1,2,3]
l2 = [4,5,6]


l4=[]


for i in range(len(l1)):
    for j in range(len(l2)):
        l3 =[]
        if i==j:
            l3.append(l1[i])
            l3.append(l2[j])
            print(l3)
            break
    l4.append(l3)
    

print(l4)    