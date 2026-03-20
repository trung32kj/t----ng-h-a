# Một người gửi tiết kiệm với:
# Số tiền ban đầu: 100,000,000 VND
# Lãi suất: 5%/năm
# Thời gian: 5 năm
# Tính:
# 1.Tiền lãi sau 3 năm (lãi đơn)
# 2.Tổng
# tiền nhận được
# 3.Tiền
# lãi trung bình mỗi tháng
# Công thức lãi đơn: Lãi = Vốn × Lãi suất × Số năm
# tài liệu: Chương II
# Python cơ bản
so_tien_goc = 100000000 
lai_suat_nam = 0.05
thoi_gian_tong = 5
thoi_gian_3_nam = 3
print(f"--- KẾT QUẢ TÍNH TOÁN TIẾT KIỆM ---")
print(f"Vốn ban đầu: {so_tien_goc:,} VND")
print(f"Lãi suất: {lai_suat_nam * 100}%/năm")
print(f"Thời gian gửi: {thoi_gian_tong} năm")
print("------------------------------")

tien_lai_3_nam = so_tien_goc * lai_suat_nam * thoi_gian_3_nam
tien_lai_5_nam = so_tien_goc * lai_suat_nam * thoi_gian_tong
tong_tien_nhan_duoc = so_tien_goc + tien_lai_5_nam

tong_so_thang = thoi_gian_tong * 12
lai_trung_binh_thang = tien_lai_5_nam / tong_so_thang

print(f"--- KẾT QUẢ TÍNH TOÁN TIẾT KIỆM ---")
print(f"Vốn ban đầu: {so_tien_goc:,} VND")
print(f"Lãi suất: {lai_suat_nam * 100}%/năm")
print(f"Thời gian gửi: {thoi_gian_tong} năm")
print("------------------------------")

print(f"1. Tiền lãi sau 3 năm là: {tien_lai_3_nam:,} VND")
print(f"2. Tổng tiền nhận được sau {thoi_gian_tong} năm là: {tong_tien_nhan_duoc:,} VND")
print(f"3. Tiền lãi trung bình mỗi tháng là: {lai_trung_binh_thang:,.2f} VND")