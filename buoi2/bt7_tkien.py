tien_goc = 1000000
lai_suat = 0.05
#nam
thoi_gian = 5  

# Tính lãi đúng
lai_hang_nam = tien_goc * lai_suat  # Lãi 1 năm
tong_lai_5_nam = lai_hang_nam * thoi_gian  # Tổng lãi 5 năm
lai_hang_thang = lai_hang_nam / 12  # Lãi 1 tháng
tong_so_tien = tien_goc + tong_lai_5_nam

print("Lãi hàng năm là: ", lai_hang_nam)
print("Lãi hàng tháng là: ", lai_hang_thang)
print("Tổng lãi trong ", thoi_gian, " năm là: ", tong_lai_5_nam)
print("Tổng số tiền sau ", thoi_gian, " năm là: ", tong_so_tien)  
