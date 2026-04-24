# HỆ THỐNG QUẢN LÝ TÀI KHOẢN NGÂN HÀNG
from abc import ABC, abstractmethod
from datetime import datetime

# Lớp cơ sở trừu tượng cho tài khoản
class TaiKhoan(ABC):
    def __init__(self, so_tk, chu_tk, so_du_ban_dau=0):
        self.so_tk = so_tk
        self.chu_tk = chu_tk
        self.so_du = so_du_ban_dau
        self.lich_su_gd = []
    
    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
            self._ghi_lich_su(f"Nạp tiền: +{so_tien:,.0f} VNĐ")
            print(f"✓ Nạp {so_tien:,.0f} VNĐ thành công!")
            return True
        print("✗ Số tiền không hợp lệ!")
        return False
    
    @abstractmethod
    def rut_tien(self, so_tien):
        pass
    
    @abstractmethod
    def tinh_lai(self):
        pass
    
    def chuyen_tien(self, tk_nhan, so_tien):
        if self.rut_tien(so_tien):
            tk_nhan.nap_tien(so_tien)
            print(f"✓ Chuyển {so_tien:,.0f} VNĐ đến TK {tk_nhan.so_tk} thành công!")
            return True
        return False
    
    def xem_so_du(self):
        print(f"\n{'='*50}")
        print(f"Số TK: {self.so_tk} | Chủ TK: {self.chu_tk}")
        print(f"Loại TK: {self.__class__.__name__}")
        print(f"Số dư: {self.so_du:,.0f} VNĐ")
        print(f"{'='*50}")
    
    def xem_lich_su(self):
        print(f"\n--- LỊCH SỬ GIAO DỊCH TK {self.so_tk} ---")
        if not self.lich_su_gd:
            print("Chưa có giao dịch nào")
        else:
            for gd in self.lich_su_gd[-10:]:  # Hiển thị 10 giao dịch gần nhất
                print(gd)
    
    def _ghi_lich_su(self, noi_dung):
        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.lich_su_gd.append(f"[{thoi_gian}] {noi_dung} | Số dư: {self.so_du:,.0f} VNĐ")


# 1. Tài khoản Tiết kiệm - Lãi suất cao, hạn chế rút tiền
class TKTietKiem(TaiKhoan):
    def __init__(self, so_tk, chu_tk, so_du_ban_dau=0, lai_suat=0.05):
        super().__init__(so_tk, chu_tk, so_du_ban_dau)
        self.lai_suat = lai_suat  # 5% mặc định
        self.so_lan_rut = 0
        self.gioi_han_rut = 3  # Chỉ được rút 3 lần/tháng
    
    def rut_tien(self, so_tien):
        if self.so_lan_rut >= self.gioi_han_rut:
            print(f"✗ Đã vượt quá giới hạn rút tiền ({self.gioi_han_rut} lần/tháng)")
            return False
        
        if so_tien > self.so_du:
            print("✗ Số dư không đủ!")
            return False
        
        if so_tien > 0:
            self.so_du -= so_tien
            self.so_lan_rut += 1
            self._ghi_lich_su(f"Rút tiền: -{so_tien:,.0f} VNĐ")
            print(f"✓ Rút {so_tien:,.0f} VNĐ thành công! (Còn {self.gioi_han_rut - self.so_lan_rut} lần rút)")
            return True
        return False
    
    def tinh_lai(self):
        lai = self.so_du * self.lai_suat
        self.so_du += lai
        self._ghi_lich_su(f"Lãi suất {self.lai_suat*100}%: +{lai:,.0f} VNĐ")
        print(f"✓ Tính lãi: +{lai:,.0f} VNĐ")
        return lai


# 2. Tài khoản Thanh toán - Linh hoạt, phí giao dịch
class TKThanhToan(TaiKhoan):
    def __init__(self, so_tk, chu_tk, so_du_ban_dau=0):
        super().__init__(so_tk, chu_tk, so_du_ban_dau)
        self.phi_rut = 1100  # Phí rút tiền ATM
        self.phi_chuyen = 2200  # Phí chuyển khoản
    
    def rut_tien(self, so_tien):
        tong_tien = so_tien + self.phi_rut
        if tong_tien > self.so_du:
            print(f"✗ Không đủ tiền! (Cần {tong_tien:,.0f} VNĐ bao gồm phí {self.phi_rut:,.0f} VNĐ)")
            return False
        
        if so_tien > 0:
            self.so_du -= tong_tien
            self._ghi_lich_su(f"Rút tiền: -{so_tien:,.0f} VNĐ (Phí: {self.phi_rut:,.0f} VNĐ)")
            print(f"✓ Rút {so_tien:,.0f} VNĐ thành công! (Phí: {self.phi_rut:,.0f} VNĐ)")
            return True
        return False
    
    def chuyen_tien(self, tk_nhan, so_tien):
        tong_tien = so_tien + self.phi_chuyen
        if tong_tien > self.so_du:
            print(f"✗ Không đủ tiền! (Cần {tong_tien:,.0f} VNĐ bao gồm phí {self.phi_chuyen:,.0f} VNĐ)")
            return False
        
        self.so_du -= tong_tien
        tk_nhan.nap_tien(so_tien)
        self._ghi_lich_su(f"Chuyển tiền: -{so_tien:,.0f} VNĐ đến TK {tk_nhan.so_tk} (Phí: {self.phi_chuyen:,.0f} VNĐ)")
        print(f"✓ Chuyển {so_tien:,.0f} VNĐ thành công! (Phí: {self.phi_chuyen:,.0f} VNĐ)")
        return True
    
    def tinh_lai(self):
        print("Tài khoản thanh toán không có lãi suất")
        return 0


# 3. Tài khoản VIP - Ưu đãi đặc biệt
class TKVIP(TaiKhoan):
    def __init__(self, so_tk, chu_tk, so_du_ban_dau=0):
        super().__init__(so_tk, chu_tk, so_du_ban_dau)
        self.lai_suat = 0.08  # 8% lãi suất cao
        self.han_muc_tin_dung = 50000000  # 50 triệu hạn mức
    
    def rut_tien(self, so_tien):
        # VIP có thể rút vượt số dư trong hạn mức tín dụng
        if so_tien > self.so_du + self.han_muc_tin_dung:
            print(f"✗ Vượt quá hạn mức! (Tối đa: {(self.so_du + self.han_muc_tin_dung):,.0f} VNĐ)")
            return False
        
        if so_tien > 0:
            self.so_du -= so_tien
            self._ghi_lich_su(f"Rút tiền VIP: -{so_tien:,.0f} VNĐ (Miễn phí)")
            print(f"✓ Rút {so_tien:,.0f} VNĐ thành công! (Miễn phí)")
            return True
        return False
    
    def chuyen_tien(self, tk_nhan, so_tien):
        # VIP miễn phí chuyển khoản
        if so_tien > self.so_du + self.han_muc_tin_dung:
            print(f"✗ Vượt quá hạn mức!")
            return False
        
        self.so_du -= so_tien
        tk_nhan.nap_tien(so_tien)
        self._ghi_lich_su(f"Chuyển tiền VIP: -{so_tien:,.0f} VNĐ đến TK {tk_nhan.so_tk} (Miễn phí)")
        print(f"✓ Chuyển {so_tien:,.0f} VNĐ thành công! (Miễn phí)")
        return True
    
    def tinh_lai(self):
        if self.so_du > 0:
            lai = self.so_du * self.lai_suat
            self.so_du += lai
            self._ghi_lich_su(f"Lãi suất VIP {self.lai_suat*100}%: +{lai:,.0f} VNĐ")
            print(f"✓ Tính lãi VIP: +{lai:,.0f} VNĐ")
            return lai
        return 0


# Hệ thống quản lý ngân hàng
class NganHang:
    def __init__(self, ten_ngan_hang):
        self.ten = ten_ngan_hang
        self.danh_sach_tk = {}
    
    def tao_tai_khoan(self, loai_tk, so_tk, chu_tk, so_du_ban_dau=0):
        if so_tk in self.danh_sach_tk:
            print(f"✗ Số tài khoản {so_tk} đã tồn tại!")
            return None
        
        if loai_tk == "tietkiem":
            tk = TKTietKiem(so_tk, chu_tk, so_du_ban_dau)
        elif loai_tk == "thanhtoan":
            tk = TKThanhToan(so_tk, chu_tk, so_du_ban_dau)
        elif loai_tk == "vip":
            tk = TKVIP(so_tk, chu_tk, so_du_ban_dau)
        else:
            print("✗ Loại tài khoản không hợp lệ!")
            return None
        
        self.danh_sach_tk[so_tk] = tk
        print(f"✓ Tạo tài khoản {loai_tk.upper()} thành công cho {chu_tk}!")
        return tk
    
    def tim_tai_khoan(self, so_tk):
        return self.danh_sach_tk.get(so_tk)
    
    def hien_thi_tat_ca_tk(self):
        print(f"\n{'='*60}")
        print(f"NGÂN HÀNG {self.ten.upper()} - DANH SÁCH TÀI KHOẢN")
        print(f"{'='*60}")
        if not self.danh_sach_tk:
            print("Chưa có tài khoản nào")
        else:
            for tk in self.danh_sach_tk.values():
                print(f"STK: {tk.so_tk} | {tk.chu_tk} | {tk.__class__.__name__} | Số dư: {tk.so_du:,.0f} VNĐ")
        print(f"{'='*60}")


# CHƯƠNG TRÌNH DEMO
def main():
    # Tạo ngân hàng
    ngan_hang = NganHang("Vietcombank")
    
    print("\n🏦 CHÀO MỪNG ĐÉN HỆ THỐNG NGÂN HÀNG 🏦\n")
    
    # Tạo các loại tài khoản
    tk1 = ngan_hang.tao_tai_khoan("tietkiem", "TK001", "Nguyễn Văn A", 10000000)
    tk2 = ngan_hang.tao_tai_khoan("thanhtoan", "TK002", "Trần Thị B", 5000000)
    tk3 = ngan_hang.tao_tai_khoan("vip", "TK003", "Lê Văn C", 100000000)
    
    print("\n" + "="*60)
    print("DEMO CÁC CHỨC NĂNG")
    print("="*60)
    
    # Demo tài khoản tiết kiệm
    print("\n--- TÀI KHOẢN TIẾT KIỆM ---")
    tk1.xem_so_du()
    tk1.tinh_lai()
    tk1.rut_tien(1000000)
    tk1.xem_so_du()
    
    # Demo tài khoản thanh toán
    print("\n--- TÀI KHOẢN THANH TOÁN ---")
    tk2.xem_so_du()
    tk2.rut_tien(500000)
    tk2.chuyen_tien(tk1, 1000000)
    tk2.xem_so_du()
    
    # Demo tài khoản VIP
    print("\n--- TÀI KHOẢN VIP ---")
    tk3.xem_so_du()
    tk3.tinh_lai()
    tk3.chuyen_tien(tk2, 5000000)
    tk3.xem_so_du()
    
    # Hiển thị tất cả tài khoản
    ngan_hang.hien_thi_tat_ca_tk()
    
    # Xem lịch sử giao dịch
    print("\n")
    tk2.xem_lich_su()


if __name__ == "__main__":
    main()
    
