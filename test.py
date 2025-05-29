

# tuoi =int(input("Nhap tuoi: "))
# diem = int(input("Nhap diem: "))

# if tuoi >=18 and diem >=70:
#     print("Du dieu kien tham gia: \n")
# else:
#     print("KHong du dieu kien tham gia\n")


# num = int(input())
# if num % 2 != 0:
#     print("So le")
# else:
#     print("So chan")

def dem_nguyen_am(chuoi:str)->int:
    #a,i,u,e,o | A, I,U,E,O
    dem =0
    for c in chuoi:
        c=c.lower()
        if c == 'a' or c=='i' or c=='u'or c=='e' or c =='o':
            dem+=1
    return dem

st = "hellO aei"
res = dem_nguyen_am(st)
print(res)