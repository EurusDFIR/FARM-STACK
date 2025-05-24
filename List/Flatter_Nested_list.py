Input=[1, [2, 3, [4, 5]], 6, [7, 8]]
res =[]
for i in Input:
    if type(i) ==list:
        for j in i:
            if type(j) ==list:
                for k in j:
                    if type(k) ==list:
                        res.append(k)
                    else:
                        res.append(k)
            else:
                res.append(j)
    else:
        res.append(i)
print(res)