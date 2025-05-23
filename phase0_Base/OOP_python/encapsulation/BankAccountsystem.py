class TaiKhoanNganHang:
    def __init__(self,so_tai_khoan,ten_chu_tai_khoan, so_du,ma_pin):
        self.__so_tai_khoan = so_tai_khoan
        self.__ten_chu_tai_khoan = ten_chu_tai_khoan
        self.__so_du= so_du
        self.__ma_pin = ma_pin

    def nap_tien(self,so_tien):
        if so_tien >0:
            self.__so_du+=so_tien
            print(f'nap tien thanh cong! Voi so du hien tai: {self.__so_du}$')
        else:
            print("so tien nap vao khong hop le") 
    def rut_tien(self, so_tien, ma_pin_nhap_vao):
        if ma_pin_nhap_vao == self.__ma_pin:
            if so_tien >0:
                if so_tien <= self.__so_du:
                    self.__so_du-=so_tien
                    print(f'rut tien thanh cong. So du hien tai: {self.__so_du}')
                else:
                    print("so du khong du, vui long nhap lai!")
            else:
                print("So tien rut khong hop le!")
        else:
            print("ma pin khong dung. Vui long nhap lai!") 

    def xem_so_du(self, ma_pin_nhap_vao):
        if ma_pin_nhap_vao==self.__ma_pin:
              print(f"so du hien tai {self.__so_du}")
        else:
            print("ma pin khong dung!")
            return None

    def doi_ma_pin(self,ma_pin_cu, ma_pin_moi):
        if ma_pin_cu ==self.__ma_pin:
            self.__ma_pin = ma_pin_moi
            print("Doi ma PIN thanh cong")
        else:
            print("ma PIN cu khong dung!")
    
    def hien_thi_thong_tin_tai_khoan(self):
        print(f"so tai khoan: {self.__so_tai_khoan}")
        print(f'ten chu tai khoan: {self.__ten_chu_tai_khoan}')

taikhoanNh = TaiKhoanNganHang('144499','NGUYEN VAN A', 1000,'123456')
taikhoanNh.hien_thi_thong_tin_tai_khoan()
taikhoanNh.nap_tien(100)
taikhoanNh.rut_tien(5,'123456')
taikhoanNh.xem_so_du('123456')
taikhoanNh.doi_ma_pin('123456','222222')


        