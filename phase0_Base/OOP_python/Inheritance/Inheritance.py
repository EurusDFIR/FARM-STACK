class PhuongTien:

    def __init__(self, ten, so_banh):
        self.ten = ten
        self.so_banh = so_banh

    def di_chuyen(self):
        print(f'{self.ten} dang di chuyen')
    
    def hien_thi_thong_tin(self):
        print(f'ten phuong tien {self.ten}')
        print(f'so banh cua phuong tien {self.so_banh}')


class XeMay(PhuongTien):
    def __init__(self, ten, so_banh,dung_tich_xy_lanh):
       super().__init__(ten, so_banh)
       self.dung_tich_xy_lanh = dung_tich_xy_lanh
    def di_chuyen(self):
        print(f'xe may {self.ten} dang phong nhanh')

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f'Dung tich xy lanh {self.dung_tich_xy_lanh}')

class Oto(PhuongTien):
    def __init__(self, ten, so_banh, so_cho_ngoi):
        super().__init__(ten, so_banh)
        self.so_cho_ngoi = so_cho_ngoi

    def bam_coi(self):
        print("Bip Bip!")
    
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f'so cho ngoi {self.so_cho_ngoi}')

xemay = XeMay('Wave Alpha',2, 'dung tich 110cc')
xeoto= Oto('Toyota Camry', 4,'5 cho ngoi' )

xemay.di_chuyen()
xemay.hien_thi_thong_tin()
print('---------------------------\n')
xeoto.di_chuyen()
xeoto.hien_thi_thong_tin()
