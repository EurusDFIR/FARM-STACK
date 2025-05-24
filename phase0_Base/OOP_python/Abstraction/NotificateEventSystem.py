from abc import abstractmethod,ABC
import random
import datetime
import uuid
class ThongBaoBase(ABC):

    def __init__(self,ma_thong_bao,noi_dung,nguoi_nhan,thoi_gian_tao,trang_thai_hien_tai,ghi_chu_loi):

        self._ma_thong_bao = ma_thong_bao
        self._noi_dung = noi_dung
        self._nguoi_nhan = nguoi_nhan
        self._thoi_gian_tao = thoi_gian_tao
        self._trang_thai_hien_tai = trang_thai_hien_tai
        self._ghi_chu_loi = ghi_chu_loi


    @abstractmethod
    def gui_thong_bao(self)->bool:
        pass
    @abstractmethod
    def lay_kieu_thong_bao(self)->str:
        pass
    
    @abstractmethod
    def hien_thi_chi_tiet_nguoi_nhan(self):
        pass

    def get_trang_thai(self)->str:
        return self._trang_thai_hien_tai
    def get_ma_thong(self)->str:
        return self._ma_thong_bao
    def get_thong_tin_co_ban(self):
        print(f'ma thong bao: {self._ma_thong_bao}')
        print(f'noi dung: {self._noi_dung}')
        print(f'thoi gian tao: {self._thoi_gian_tao}')
        print(f'trang thai hien tai: {self._trang_thai_hien_tai}')
        print(f'ghi chu loi {self._ghi_chu_loi}')

class ThongBaoSMS(ThongBaoBase):
    def __init__(self, ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi,so_dien_thoai_gui):
        super().__init__(ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi)
        self._so_dien_thoai_gui = so_dien_thoai_gui

    def gui_thong_bao(self) -> bool:
        self._trang_thai_hien_tai='SENDING'
        print(f'Dang gui SMS {self._noi_dung} toi {self._nguoi_nhan} tu {self._so_dien_thoai_gui}...')
        try:
            if random.random() <0.1:
                raise Exception("loi ket noi nha mang!")
            elif random.random()<0.2:
                self._trang_thai_hien_tai = "FAILED"
                self._ghi_chu_loi = "Loi khong xac dinh"
                return False
            else:
                self._trang_thai_hien_tai = 'SENT'
                print('Gui thanh cong!')
                return True
        except Exception as e:
            self._trang_thai_hien_tai = "FAILED"
            self._ghi_chu_loi = str(e) 
            print(f"gui that bai do loi {self._ghi_chu_loi}")
            return False
    def lay_kieu_thong_bao(self) -> str:
        return "SMS"
    def hien_thi_chi_tiet_nguoi_nhan(self):
         print(f'so dien thoai nguoi nhan: {self._nguoi_nhan}')


class ThongBaoEmail(ThongBaoBase):

    def __init__(self, ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi, dia_chi_email_gui,tieu_de_email):
        super().__init__(ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi)
        self._dia_chi_email_gui = dia_chi_email_gui
        self._tieu_de_email = tieu_de_email

    def gui_thong_bao(self) -> bool:
        self._trang_thai_hien_tai = "SENDING"
        print(f'Dang gui Email {self._tieu_de_email } toi {self._nguoi_nhan} tu {self._dia_chi_email_gui}...')
        try:
            if random.random() <0.15:
                raise Exception("Loi server mail hoac dia chi khong hop le!")
            elif random.random() < 0.27:
                self._trang_thai_hien_tai="FAILED"
                self._ghi_chu_loi="Khong ro danh tinh nguoi gui"
                return False
            else:
                self._trang_thai_hien_tai="SENT"
                print("Da gui thanh cong!")
                return True
        except Exception as e:
            self._trang_thai_hien_tai = "FAILED"
            self._ghi_chu_loi = str(e)
            return False
    def lay_kieu_thong_bao(self) -> str:
        return "EMAIL"
    def hien_thi_chi_tiet_nguoi_nhan(self):
        print(f"Dia chi email nguoi nhan: {self._nguoi_nhan}")    
        
class ThongBaoPushNotification(ThongBaoBase):
    def __init__(self, ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi, app_id,device_token):
        super().__init__(ma_thong_bao, noi_dung, nguoi_nhan, thoi_gian_tao, trang_thai_hien_tai, ghi_chu_loi)
        self._app_id = app_id
        self._device_token = device_token

    def gui_thong_bao(self) -> bool:
        self._trang_thai_hien_tai = "SENDING"
        print(f"Dang gui Push Notification toi thiet bi {self._nguoi_nhan} qua app {self._app_id}")
        try:
            if random.random() <0.05:
                raise Exception("Loi API Push NOtification")
            else:
                self._trang_thai_hien_tai="SENT"
                print("da GUI THANH CONG")
                return True
        except Exception as e:
            self._trang_thai_hien_tai = "FAILED"
            self._ghi_chu_loi = str(e)
            print(f"Loi khong xac dinh {self._ghi_chu_loi}")
    
    def lay_kieu_thong_bao(self) -> str:
        return "PUSH_NOTIFICATION"
    def hien_thi_chi_tiet_nguoi_nhan(self):
        print(f"app id: {self._app_id} va device token: {self._device_token}")


def main():
    DanhSachThongBao = []
    
    print("--- Tạo Thông báo SMS ---")
    # SMS 1
    sms1 = ThongBaoSMS(
        ma_thong_bao=str(uuid.uuid4()), # de tu sinh ra ma id ko can viet chay
        noi_dung="Ma OTP cua ban la 123456",
        nguoi_nhan="0901234567",
        thoi_gian_tao = '25/05/2025',
        trang_thai_hien_tai='NUll',
        ghi_chu_loi='khong loi',
        so_dien_thoai_gui="0881234567"
    )
    DanhSachThongBao.append(sms1)

    # SMS 2
    sms2 = ThongBaoSMS(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Don hang #DH789 da duoc giao thanh cong.",
        nguoi_nhan="0918765432",
        thoi_gian_tao = '25/05/2025',
        trang_thai_hien_tai='NUll',
        ghi_chu_loi='khong loi',
        so_dien_thoai_gui="0887654321"
    )
    DanhSachThongBao.append(sms2)

    # SMS 3  -> sms loi de test
    sms3 = ThongBaoSMS(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Canh bao: Tai khoan cua ban co dau hieu bat thuong.",
        nguoi_nhan="0971234567",
        thoi_gian_tao = '25/05/2025',
        trang_thai_hien_tai='NUll',
        ghi_chu_loi='khong loi',
        so_dien_thoai_gui="0883334445"
    )
    DanhSachThongBao.append(sms3)


   # --- 2. Tạo các đối tượng ThongBaoEmail ---
    print("\n--- Tạo Thông báo Email ---")
    # Email 1
    email1 = ThongBaoEmail(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Cam on ban da mua hang tai cua hang chung toi!",
        nguoi_nhan="nguyenvana@example.com",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        dia_chi_email_gui="noreply@cuahang.com",
        tieu_de_email="Xac nhan don hang #ABCD123"
    )
    DanhSachThongBao.append(email1)

    # Email 2
    email2 = ThongBaoEmail(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Tai lieu huong dan su dung san pham moi.",
        nguoi_nhan="tranb@example.com",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        dia_chi_email_gui="support@dichvu.net",
        tieu_de_email="Tai lieu quan trong cho ban"
    )
    DanhSachThongBao.append(email2)

    # Email 3
    email3 = ThongBaoEmail(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Reset mat khau tai khoan cua ban.",
        nguoi_nhan="lethic@example.com",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        dia_chi_email_gui="security@hethong.org",
        tieu_de_email="Yeu cau reset mat khau"
    )
    DanhSachThongBao.append(email3)


        # --- 3. Tạo các đối tượng ThongBaoPushNotification ---
    print("\n--- Tạo Thông báo Push Notification ---")
    # Push 1
    push1 = ThongBaoPushNotification(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Ban co thong bao moi tu ung dung!",
        nguoi_nhan="user_001_id",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        app_id="com.my_app.mobile",
        device_token="abc123def456ghi789jkl"
    )
    DanhSachThongBao.append(push1)

    # Push 2
    push2 = ThongBaoPushNotification(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Vuot qua muc tieu di bo hang ngay! Ban that tuyet voi.",
        nguoi_nhan="user_002_id",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        app_id="com.fitness.tracker",
        device_token="mno098pqr765stu432vwx109"
    )
    DanhSachThongBao.append(push2)

    # Push 3
    push3 = ThongBaoPushNotification(
        ma_thong_bao=str(uuid.uuid4()),
        noi_dung="Uu dai dac biet chi danh cho ban!",
        nguoi_nhan="user_003_id",
        thoi_gian_tao='25/05/2025',
        trang_thai_hien_tai='NEW',
        ghi_chu_loi='',
        app_id="com.shopping.app",
        device_token="yza012bcd345efg678hij901"
    )
    DanhSachThongBao.append(push3)

    for index, value in enumerate(DanhSachThongBao):
        value.get_thong_tin_co_ban()
        value.hien_thi_chi_tiet_nguoi_nhan()
        value.gui_thong_bao()
        value.get_thong_tin_co_ban()
        print("-----------------------------------\n")

if __name__ == '__main__':
    main()