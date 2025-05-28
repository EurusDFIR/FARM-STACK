input =         [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
        ]

# # output         [
#           [3, 6, 9],
#           [2, 5, 8],
#           [1, 4, 7]
#         ]'

lth = len(input)
for i in range(lth-1):
    for j in range(i+1,lth):
        input[i][j],input[j][i] = input[j][i],input[i][j]
matrix =[[]]
for index, value in enumerate(input):
    if index ==0:
        value = input[2]
    elif index==2:
        value = input[0]
    matrix.append(value)
    
print(matrix)
    
    
# print(input)

