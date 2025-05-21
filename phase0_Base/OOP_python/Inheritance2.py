class KhoaHoc:

    def __init__(self, ma_khoa_hoc, ten_khoa_hoc, hoc_phi, so_tin_chi):
        self.ma_khoa_hoc = ma_khoa_hoc
        self.ten_khoa_hoc = ten_khoa_hoc
        self.hoc_phi = hoc_phi
        self.so_tin_chi = so_tin_chi


    def tinh_tong_hoc_phi(self):
        return self.hoc_phi
    
    def hien_thi_thong_tin_khoa_hoc(self):
        print(f'ma khoa hoc: {self.ma_khoa_hoc}')
        print(f'ten khoa hoc {self.ten_khoa_hoc}')
        print(f'hoc phi: {self.hoc_phi}')
        print(f'so tin chi: {self.so_tin_chi}')

class KhoaHocTrucTuyen(KhoaHoc):
    def __init__(self, ma_khoa_hoc, ten_khoa_hoc, hoc_phi, so_tin_chi,link_truc_tuyen,giam_gia_online):
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, hoc_phi, so_tin_chi)
        self.link_truc_tuyen = link_truc_tuyen
        self.giam_gia_online= giam_gia_online

    # override tinh_tong_hoc_phi()

    def tinh_tong_hoc_phi(self):
         
         hoc_phi_giam_gia = self.hoc_phi * (1-self.giam_gia_online)
         return (f'hoc phi giam gia: {hoc_phi_giam_gia}')

    def hien_thi_thong_tin_khoa_hoc(self):
        super().hien_thi_thong_tin_khoa_hoc()
        print(f"link truc tuyen: {self.link_truc_tuyen}")
        print(f'giam gia online: {self.giam_gia_online}')

class KhoaHocThucHanh(KhoaHoc):
    def __init__(self, ma_khoa_hoc, ten_khoa_hoc, hoc_phi, so_tin_chi,dia_diem_thuc_hanh, phu_phi_vat_lieu):
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, hoc_phi, so_tin_chi)
        self.dia_diem_thuc_hanh= dia_diem_thuc_hanh
        self.phu_phi_vat_lieu = phu_phi_vat_lieu

    def tinh_tong_hoc_phi(self):
         tong_hoc_phi = self.hoc_phi + self.phu_phi_vat_lieu
         return tong_hoc_phi

    def hien_thi_thong_tin_khoa_hoc(self):
         super().hien_thi_thong_tin_khoa_hoc()
         print(f"dia diem thuc hanh: {self.dia_diem_thuc_hanh}")
         print(f"phu phi vat lieu {self.phu_phi_vat_lieu}")

class SinhVien:
    
    def __init__(self, ma_sinh_vien, ten_sinh_vien):
        self.ma_sinh_vien = ma_sinh_vien
        self.ten_sinh_vien = ten_sinh_vien
        self.cac_khoa_hoc_dang_ky = []
       

    def dang_ky_khoa_hoc(self, khoa_hoc):
        self.cac_khoa_hoc_dang_ky.append(khoa_hoc)
        print(f"{self.ten_sinh_vien} da dang ky khoa hoc {khoa_hoc.ten_khoa_hoc}")

    def tinh_tong_hoc_phi_da_dang_ky(self):
        tong=0
        for i in self.cac_khoa_hoc_dang_ky:
            tong+=i.tong_hoc_phi()
        return tong 


khTrucTuyen = KhoaHocTrucTuyen('PY01','lap trinh python',150000,2,'https://laptrinh.com',0.15)
khThucHanh = KhoaHocThucHanh('py02','thuc hanh python nang cao', 30000,3,'C-104',5000 )

sinhvien = SinhVien('sv01',"Nguyen Van A")
sinhvien.dang_ky_khoa_hoc(khThucHanh)
