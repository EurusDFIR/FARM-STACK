class ThongBao:
    def __init__(self,nguoi_nhan, noi_dung, thoi_gian_gui):
        self.nguoi_nhan = nguoi_nhan
        self.noi_dung = noi_dung
        self.thoi_gian_gui = thoi_gian_gui

    def gui_thong_bao(self):
        print("Dang gui thong bao chung: ")

    def hien_thi_chi_tiet(self):
        print(f'nguoi nhan: {self.nguoi_nhan}')
        print(f'noi dung: {self.noi_dung}')
        print(f'thoi gian gui: {self.thoi_gian_gui}')

    
class EmailThongBao(ThongBao):
    def __init__(self, nguoi_nhan, noi_dung, thoi_gian_gui, tieu_de_email, dia_chi_cc):
        super().__init__(nguoi_nhan, noi_dung, thoi_gian_gui)
        self.tieu_de_email = tieu_de_email
        self.dia_chi_cc = dia_chi_cc

    # override gui_thong_bao()
    def gui_thong_bao(self):
         print(f'Dang gui Email den {self.nguoi_nhan} voi tieu de {self.tieu_de_email}')

    def hien_thi_chi_tiet(self):
         super().hien_thi_chi_tiet()
         print(f'tieu de email: {self.tieu_de_email} ')
         print(f'dia chi cc: {self.dia_chi_cc}')
class SMSThongBao(ThongBao):
    def __init__(self, nguoi_nhan, noi_dung, thoi_gian_gui, so_dien_thoai_gui,chi_phi_sms):
        super().__init__(nguoi_nhan, noi_dung, thoi_gian_gui)      
        self.so_dien_thoai_gui = so_dien_thoai_gui
        self.chi_phi_sms = chi_phi_sms

    # override gui_thong_bao()
    def gui_thong_bao(self):
        print(f"dang gui SMS den {self.nguoi_nhan} tu {self.so_dien_thoai_gui}")

    # override hien thi chi tiet()
    def hien_thi_chi_tiet(self):
        super().hien_thi_chi_tiet()
        print(f'so dien thoai {self.so_dien_thoai_gui}')
        print(f'chi phi sms {self.chi_phi_sms}')
class PushThongBao(ThongBao):
    def  __init__(self, nguoi_nhan, noi_dung, thoi_gian_gui, nen_tang_thiet_bi,icon_thong_bao):
        super().__init__(nguoi_nhan, noi_dung, thoi_gian_gui)
        self.nen_tang_thiet_bi = nen_tang_thiet_bi
        self.icon_thong_bao =icon_thong_bao

    def gui_thong_bao(self):
        print(f'Dang day thong bao den thiet bi {self.nen_tang_thiet_bi} cua {self.nguoi_nhan}')
    def hien_thi_chi_tiet(self):
        super().hien_thi_chi_tiet()
        print(f'nen tang thiet bi {self.nen_tang_thiet_bi}')
        print(f'icon thong bao {self.icon_thong_bao}')
         
hang_doi_thong_bao= [

]
emailthongbao = EmailThongBao('eurus', 'Nghi Le 30/04/2025 cho toan cong ty','17:05 25/05/2025','nghi le','abc@gmail.com')
smsthongbao = SMSThongBao('eurus', 'Nghi Le 30/04/2025 cho toan cong ty','17:05 25/05/2025','0399355222',1500)
pushthongbao = PushThongBao('eurus','Nghi Le 30/04/2025 cho toan cong ty','17:05 25/05/2025','iphone','notiIcon')

hang_doi_thong_bao.append(emailthongbao)
hang_doi_thong_bao.append(smsthongbao)
hang_doi_thong_bao.append(pushthongbao)

for tb in hang_doi_thong_bao:
    tb.gui_thong_bao()
    tb.hien_thi_chi_tiet()
    print('---------------------------\n')
