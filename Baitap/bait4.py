# 1. Viết chương trình giải phương trình bậc 2
import math
def giai_pt_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")

# 2. Viết chương trình in ra bảng cửu chương từ 2 đến 9
def bang_cuu_chuong(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# 3. Tính tổng các số chẵn từ 1 đến 100
def tong_so_chan(n):
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            tong += i
    return tong

# 4. Viết chương trình kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 5. In ra hình tam giác so với chiều cao n
def in_hinh_tam_giac(n):
    for i in range(1, n+1):
        print("*" * i)

# 6. Viết chương trình tìm ƯCLN và BCNN của hai số
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)

# 7. Viết chương trình đếm số lượng chữ số của một số nguyên
def dem_chu_so(n):
    return len(str(abs(n)))

def main():
    while True:
        print("\n" + "="*30)
        print("DANH SÁCH BÀI TẬP")
        print("1. Giải phương trình bậc 2")
        print("2. In bảng cửu chương (2-9)")
        print("3. Tính tổng số chẵn (1-100)")
        print("4. Kiểm tra số nguyên tố")
        print("5. In hình tam giác")
        print("6. Tìm ƯCLN và BCNN")
        print("7. Đếm số chữ số")
        print("0. Thoát")
        print("="*30)
        
        chon = input("Mời bạn chọn bài tập (0-7): ")

        match chon:
            case "1":
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                c = float(input("Nhập hệ số c: "))
                giai_pt_bac_2(a, b, c)
            case "2":
                n = int(input("Nhập số để in bảng cửu chương (2-9): "))
                if 2 <= n <= 9:
                    bang_cuu_chuong(n)
                else:
                    print("Vui lòng nhập số từ 2 đến 9.")
            case "3":
                print(f"Tổng các số chẵn từ 1 đến 100 là: {tong_so_chan(100)}")
            case "4":
                n = int(input("Nhập số để kiểm tra nguyên tố: "))
                if kiem_tra_so_nguyen_to(n):
                    print(f"{n} là số nguyên tố.")
                else:
                    print(f"{n} không phải là số nguyên tố.")
            case "5":
                n = int(input("Nhập chiều cao của hình tam giác: "))
                in_hinh_tam_giac(n)
            case "6":
                a = int(input("Nhập số thứ nhất: "))
                b = int(input("Nhập số thứ hai: "))
                print(f"ƯCLN của {a} và {b} là: {ucln(a, b)}")
                print(f"BCNN của {a} và {b} là: {bcnn(a, b)}")
            case "7":
                n = int(input("Nhập số để đếm chữ số: "))
                print(f"Số lượng chữ số của {n} là: {dem_chu_so(n)}")
            case "0":
                print("Thoát chương trình. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
if __name__ == "__main__":
    main()