input=  [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

  #-->      # [
        #   [7, 4, 1],
        #   [8, 5, 2],
        #   [9, 6, 3]
        # ]
lth = len(input)
for i in range(lth-1):
    for j in range(i+1,lth):
        input[i][j],input[j][i] = input[j][i],input[i][j]
      
    
print(input)
for i in input:
    i=i.reverse()
print(input)