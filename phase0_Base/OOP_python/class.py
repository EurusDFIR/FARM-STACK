class Sach():
  

    def __init__(self, tieu_de, tac_gia,nam_xuat_ban, so_luong_con_lai):
        self.tieu_de = tieu_de
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.so_luong_con_lai= so_luong_con_lai
        print(f" sach {self.tieu_de} da duoc them vao thu vien")
    
    def hien_thi_thong_tin(self):
        print(f"Ten sach {self.tieu_de}")
        print(f"tac gia {self.tac_gia}")
        print(f"nam xb: {self.nam_xuat_ban}")
        print(f'so luong con lai: {self.so_luong_con_lai}')
    
    def muon_sach(self):
        if self.so_luong_con_lai > 1:
            self.so_luong_con_lai -=1
            print(f"ban da muon sach {self.tieu_de} thanh cong")
        else:
            print(f"sach {self.tieu_de} da het")

class nguoiDung():
    def __init__(self, UserId, ten, namSinh, NgayMuon):
        self.Userid = UserId
        self.ten = ten
        self.namSinh = namSinh
        self.NgayMuon = NgayMuon

    
    

sach = Sach('Vu an Lerouge', 'Leblanc', 1885, 2)
sach_Light_novel = Sach('Hyoka', 'otoko',2011,5)

sach.hien_thi_thong_tin()
sach.muon_sach()

sach_Light_novel.hien_thi_thong_tin()
sach_Light_novel.muon_sach()