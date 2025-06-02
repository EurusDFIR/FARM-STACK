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

st = "hello world 2"

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


s= "[python]"
print(s)
s = list(s)
s[0], s[-1] = "", ""

s = '   '.join(s)

# s2 = ''.join(s)
print(s)
