# Hãy viết code python để:
# 1. Viết chương trình nhập vào họ tên, tuổi, điểm trung bình và in ra màn hình
def nhap_thong_tin():
    ho_ten = input("Nhập họ tên: ")
    tuoi = int(input("Nhập tuổi: "))
    diem_tb = float(input("Nhập điểm trung bình: "))
    print(f"Họ tên: {ho_ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Điểm trung bình: {diem_tb}")
# 2. Tính diện tích và chu vi hình chữ nhật khi biết chiều dài và chiều rộng
def tinh_dien_tich_chu_vi():
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    print(f"Diện tích hình chữ nhật: {dien_tich}")
    print(f"Chu vi hình chữ nhật: {chu_vi}")
# 3. Viết chương trình chuyển đổi nhiệt độ từ C sang F
def chuyen_doi_nhiet_do():
    do_c = float(input("Nhập nhiệt độ (°C): "))
    do_f = (do_c * 9/5) + 32
    print(f"Nhiệt độ tương đương: {do_f} °F")
# 4. Nhập vào một số nguyên, kiểm tra số đó là chẵn hay lẻ
def kiem_tra_chan_le():
    so_nguyen = int(input("Nhập một số nguyên: "))
    if so_nguyen % 2 == 0:
        print(f"Số {so_nguyen} là số chẵn.")
    else:
        print(f"Số {so_nguyen} là số lẻ.")
# 5. Tính tổng, hiệu, thương của hai số thực
def tinh_toan_hai_so():
    so_thuc_1 = float(input("Nhập số thực thứ nhất: "))
    so_thuc_2 = float(input("Nhập số thực thứ hai: "))
    tong = so_thuc_1 + so_thuc_2
    hieu = so_thuc_1 - so_thuc_2
    thuong = so_thuc_1 / so_thuc_2 if so_thuc_2 != 0 else "Không thể chia cho 0"
    print(f"Tổng: {tong}")
    print(f"Hiệu: {hieu}")
    print(f"Thương: {thuong}")

def main():
    while True:
        print("Chọn chức năng:")
        print("1. Nhập thông tin cá nhân")
        print("2. Tính diện tích và chu vi hình chữ nhật")
        print("3. Chuyển đổi nhiệt độ từ C sang F")
        print("4. Kiểm tra số chẵn hay lẻ")
        print("5. Tính tổng, hiệu, thương của hai số thực")
        print("0. thoát")
        
        choice = input("Nhập lựa chọn (1-5): ")
        
        if choice == '1':
            nhap_thong_tin()
        elif choice == '2':
            tinh_dien_tich_chu_vi()
        elif choice == '3':
            chuyen_doi_nhiet_do()
        elif choice == '4':
            kiem_tra_chan_le()
        elif choice == '5':
            tinh_toan_hai_so()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
