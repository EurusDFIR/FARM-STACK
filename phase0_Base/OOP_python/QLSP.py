class SanPham:
    def __init__(self,ten,gia,ma_san_pham):
        self.ten = ten
        self.gia = gia
        self.ma_san_pham = ma_san_pham

    
    def mo_ta_chung(self):
        print(f"mo ta chung")
       

    def hien_thi_thong_tin(self):
        print(f"ten san pham: {self.ten}")
        print(f"gia san pham: {self.gia}")
        print(f"ma_san pham: {self.ma_san_pham}")

class DienThoai(SanPham):
    def __init__(self, ten, gia, ma_san_pham,he_dieu_hanh,kich_thuoc_man_hinh):
        super().__init__(ten, gia, ma_san_pham)
        self.he_dieu_hanh = he_dieu_hanh
        self.kich_thuoc_man_hinh = kich_thuoc_man_hinh
    # override motachung()
    def mo_ta_chung(self):
        print(f"Dien thoai {self.ten} la thiet bi di dong thong minh")
    # override hien_thi_thong_tin()
    def hien_thi_thong_tin(self):
         super().hien_thi_thong_tin()
         print(f'he dieu hanh {self.he_dieu_hanh}')
         print(f'kich thuoc man hinh {self.kich_thuoc_man_hinh}')

class Laptop(SanPham):
    def __init__(self, ten, gia, ma_san_pham, ram, cpu, card_do_hoa):
        super().__init__(ten, gia, ma_san_pham)
        self.ram = ram
        self.cpu = cpu
        self.card_do_hoa = card_do_hoa

    # override motachung()
    def mo_ta_chung(self):
        print(f'Laptop {self.ten} la mot may tinh xach tay manh me')
    # override hien thi thong tin()
    def hien_thi_thong_tin(self):
         super().hien_thi_thong_tin()
         print(f'ram: {self.ram}')
         print(f'cpu {self.cpu}')
         print(f'card do hoa: {self.card_do_hoa}')

class PhuKien(SanPham):
    def __init__(self, ten, gia, ma_san_pham,loai_phu_kien, tuong_thich_voi):
        super().__init__(ten, gia, ma_san_pham)
        self.loai_phu_kien = loai_phu_kien
        self.tuong_thich_voi = tuong_thich_voi

    # override mo_ta_chung()
    def mo_ta_chung(self):
        print(f'phu kien {self.ten} giup nang cao trai nghiem su dung')

    # override hien_thi_thong_tin()
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f'loai phu kien: {self.loai_phu_kien}')
        print(f'tuong thich voi: {self.tuong_thich_voi}')

kho_hang = []
dt = DienThoai('iphone17' ,3000000, 'ip17','ios21','17.32 x 14.17 x 1.61 inches')
lt = Laptop('Acer nitro 5',2600000,'ac5','16gb','i7core','rtx-3084')
pk = PhuKien('sac_du_phong',40000,'scp15','sac','iphone')

kho_hang.append(dt)
kho_hang.append(lt)
kho_hang.append(pk)

# polymophism đa hình -> one activity can excute in many ways
for sanpham in kho_hang:
    sanpham.mo_ta_chung()
    sanpham.hien_thi_thong_tin()
    print("------------------------\n")