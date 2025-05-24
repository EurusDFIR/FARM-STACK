from abc import ABC,abstractmethod
import datetime

class PhuongThucThanhToan(ABC):
    def __init__(self,ma_giao_dich,so_tien,ngay_giao_dich):
        self.ma_giao_dich = ma_giao_dich
        self.so_tien = so_tien
        self.ngay_giao_dich = datetime.datetime.now()

    @abstractmethod
    def thuc_hien_thanh_toan(self)->bool:
        pass
    @abstractmethod
    def lay_trang_thai_thanh_toan(self)->str:
        pass 
    @abstractmethod
    def hien_thi_chi_tiet_phuong_thuc(self):
        pass

    def hien_thi_thong_tin_giao_dich_co_ban(self):
        print(f'Ma giao dich: {self.ma_giao_dich}')
        print(f'so tien: {self.so_tien}')
        print(f'ngay giao dich: {self.ngay_giao_dich}')

class ThanhToanTheTinDung(PhuongThucThanhToan):
    def __init__(self, ma_giao_dich, so_tien, ngay_giao_dich,so_the,ten_chu_the,ngay_het_han):
        super().__init__(ma_giao_dich, so_tien, ngay_giao_dich)
        
        self.so_the = so_the
        self.ten_chu_the = ten_chu_the
        self.ngay_het_han = ngay_het_han

    def thuc_hien_thanh_toan(self) -> bool:
        print('Dang xu ly thanh toan the... \n')
        print('Thanh cong!')
        return True
        
    def lay_trang_thai_thanh_toan(self) -> str:
        return "thanh cong"
    def hien_thi_chi_tiet_phuong_thuc(self):
        print(f'so the: {self.so_the[-4:]}')
        print(f'ten chu the: {self.ten_chu_the}')
        print(f'ngay het han: {self.ngay_het_han}')
class ThanhToanChuyenKhoanNganHang(PhuongThucThanhToan):
    def __init__(self, ma_giao_dich, so_tien, ngay_giao_dich,ten_ngan_hang,so_tai_khoan_nhan):
        super().__init__(ma_giao_dich, so_tien, ngay_giao_dich)
        self.ten_ngan_hang = ten_ngan_hang
        self.so_tai_khoan_nhan = so_tai_khoan_nhan

    def thuc_hien_thanh_toan(self) -> bool:
        print("Dang xu ly chuyen khoan... That bai!")
        return False

    def lay_trang_thai_thanh_toan(self) -> str:
        return "That bai"

    def hien_thi_chi_tiet_phuong_thuc(self):
        print(f'ten ngan hang: {self.ten_ngan_hang}')
        print(f'so tai khoan: {self.so_tai_khoan_nhan}')

class ThanhToanViDienTu(PhuongThucThanhToan):
    def __init__(self, ma_giao_dich, so_tien, ngay_giao_dich,ten_vi,so_dien_thoai_vi):
        super().__init__(ma_giao_dich, so_tien, ngay_giao_dich)
        self.ten_vi = ten_vi
        self.so_dien_thoai_vi = so_dien_thoai_vi

    def thuc_hien_thanh_toan(self) -> bool:
        print("Dang xu ly chuyen bang vi... Thanh cong!")
        return True
    
    def lay_trang_thai_thanh_toan(self) -> str:
        return "Thanh cong!"

    def hien_thi_chi_tiet_phuong_thuc(self):
        print(f'ten vi: {self.ten_vi}')
        print(f'so dien thoai vi: {self.so_dien_thoai_vi}')
    


danh_sach_thanh_toan = []
theTinDung = ThanhToanTheTinDung('mgd12',5000,'12/05/2025','at0005','Nguyen A','20/07/2027')
chuyenKhoan = ThanhToanChuyenKhoanNganHang('ck22',10000,'22/05/2025','vietcombank','at73')
viDienTu = ThanhToanViDienTu('vdt22',99999,'22/05/2025','MOMO','0399354603') 
danh_sach_thanh_toan.append(theTinDung)
danh_sach_thanh_toan.append(chuyenKhoan)
danh_sach_thanh_toan.append(viDienTu)

for phuongThuc in danh_sach_thanh_toan:
        phuongThuc.hien_thi_thong_tin_giao_dich_co_ban()
        phuongThuc.hien_thi_chi_tiet_phuong_thuc()
        phuongThuc.thuc_hien_thanh_toan()
        phuongThuc.lay_trang_thai_thanh_toan()
        print('------------------------\n')   
