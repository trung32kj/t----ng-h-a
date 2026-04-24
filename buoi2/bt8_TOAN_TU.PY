print("=== CHƯƠNG TRÌNH TÍNH TOÁN ===")

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print(f"\nKết quả với số {a} và {b}:")
print("-" * 40)

tong = a + b
print(f"Tổng: {a} + {b} = {tong}")

hieu = a - b
print(f"Hiệu: {a} - {b} = {hieu}")

tich = a * b
print(f"Tích: {a} × {b} = {tich}")

if b != 0:
    thuong = a / b
    print(f"Thương: {a} ÷ {b} = {thuong}")
else:
    print("Thương: Không thể chia cho 0")

if b != 0:
    phan_du = a % b
    print(f"Chia lấy phần dư: {a} % {b} = {phan_du}")
else:
    print("Chia lấy phần dư: Không thể chia cho 0")

if b != 0:
    phan_nguyen = a // b
    print(f"Chia lấy phần nguyên: {a} // {b} = {phan_nguyen}")
else:
    print("Chia lấy phần nguyên: Không thể chia cho 0")

luy_thua = a ** b
print(f"Lũy thừa: {a} ^ {b} = {luy_thua}")