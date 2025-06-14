# print("hello")


# a = 3 
# b = 5
# # kieu so thuc
# diem_toan = 8.6
# diem_ly = 9.0

# print(f"kieu nguyen: a ={a}")
# print(f"kieu nguyen: b ={b}")
# print(f"kieu thuc: toan ={diem_toan}")

# tien = 100.00


# def napTien(tien):
#     nganHang = 200.000
#     if tien < nganHang:
#         nganHang+=tien 
#     return nganHang

# traVe =napTien(tien)
# print(f"toi co {traVe}{a} nghin")
# # print("toi co",traVe, "nghin",sep = "/",end = "\n\n\n\n")
# # print("hello")

# # tinh diem trung binh 3 mon hoc toan ly hoa

# # for i in range(65,92):
# #     c = chr(i)
# #     print(f"so thu tu {i} {c}")

# tuAoQuan = ["ao",1,"quan",2.5, False]
# #  type()
# print(type(tuAoQuan)) # list
# print(type(1))# int -> integer
# print(type("hello"))# str -> string
# print(type(5.3)) # float
# print(type(False)) #bool

# x = ("apple", "banana", "cherry")
# print(type(x))
# y = {"name" : "John", "age" : 36}
# # print(type(y)) #dictionary -> tu dien

# d = 5
# print(d)
# conver to float

# print(float(d))
# print(str(d), type(str(d)))

# st = "hello world 2"

# print(len(st))
# print(st.lower())
# print(st.upper())
# print(st.strip())
# print(st.replace("l","b"))

# print(st.split(sep =","))

# print(st.count('l'))
# 
# 
# print(f"vi tri {st.find('ello')}")


# s= "[python]"
# print(s)
# s = list(s)
# s[0], s[-1] = "", ""

# s = '   '.join(s)

# # s2 = ''.join(s)
# print(s)
# def tim_min_va_vi_tri(danh_sach: list[int]) -> list[int, int]:
#     ds =[]
#     minValue = min(danh_sach)
#     ds.append(minValue)
#     viTri =0
#     for i in range(0,len(danh_sach)-1):
#         # 0 - > 5 - 1 = 4 -> 0,1,2,3,4
#         print(i)
#         if danh_sach[i] ==minValue:

#             viTri =i
#             ds.append(viTri)
   
#     return  ds 

# danh_sach = [5, 2, 9, 1, 7]

# res = tim_min_va_vi_tri(danh_sach)
# tp =tuple(res)
# print(res)


# for i in listHoaQua:
#     # print(i)
# for i in range(0,len(listHoaQua)):
#     print(listHoaQua[i])    

# for i in [1,2,3,4,5]:
#     # print(i)
#     # if i == 'dua hau':
#     #     continue
#     #     print("hello")
#     pass 
# ket qua = 'dua hau'


# listCopy = listHoaQua
# # print(listCopy)
# listHoaQua.append("qua chanh")
# listHoaQua.insert(1,'qua buoi')
# print(listHoaQua)

# listHoaQua.append("qua chanh")
# print(len(listHoaQua))

# print(type(listHoaQua))

# del listHoaQua[4]
# listHoaQua.clear()
# print(listHoaQua)

# in bang cuu chuong 7

# for i in range(1,10+1):
#     for j in range(1,10+1):
#         print(f'{i} x {j} = {j*i}')
#     print()    


# listHoaQua = ["qua tao", 'qua cam', 'dua hau', 99, True, 5.2]

# # for i in listHoaQua:
# #     print(i)

# listTamThoi = [print(i, type(i)) for i in listHoaQua]
# print(listTamThoi)
# temp = None

# x^n

# b1: Khoi tao
# x , n = int(input()), int(input())

# tich = 1
# #b2 Vong lap 
# for i in range(1, n+1):
# #b3 Nhan don
#     tich=tich  * x
#     print(tich)

# print(tich)


# for i in range(0,5):
#     print(i)
# i=0
# while i<5:
#     print(i)
#     i+=1



# Bang cuu chuong 5x5

# n = 5

# for i in range(1,11):
#     for j in range(1,11):
#         print(f'{i} * {j} = {i*j}')
#     print('---------------------------------------')

# n= int(input("Nhap so phan luong tu: "))

# min_t = 999999999999999999 # 1,2,3,4,5
# max_t = -999999999999999999999999 # 1,2,3,4,5
# for i in range(0,n):
#     t =int(input("Nhap pha tu thu "))
#     if t < min_t:
#         min_t =t
# [::-1]
# s = input()
# check = True
# for c in range(len(s)):
#     if s[0] !=s[-1]:
#         # check=False
#         break
#     else:
#         check=True
# print(True if check ==True else False)

# max_t = 0
# # for i in range(0,n):
   
# #     t = int(input("Nhap phan tu thu "))
# #     if  t > max_t:
# #         max_t = t
# i = 0

# while i< n:
#     t = 4
#     int(input("Nhap phan tu: "))
#     if t > max_t:
#         max_t = t
#     i+=1    
# print(max_t)