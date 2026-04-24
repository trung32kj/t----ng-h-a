import pandas
data_dict = {
    'maSV': ['SV001', 'SV002', 'SV003', 'SV004', 'SV005', 'SV006', 'SV007', 'SV008', 'SV009', 'SV010'],
    'HoTen': ['Nguyen Van A', 'Le Thi B', 'Tran Van C', 'Pham Thi D', 'Hoang Van E', 'Do Thi F', 'Vu Van G', 'Phan Thi H', 'Bui Van I', 'Ngo Thi K'],
    'lop': ['23CT5', '23CT5', '23CT6', None, '23CT7', '23CT7', '23CT8', '23CT8', '23CT9', '23CT9'],
    'diemPython': [8.5, 9.0, 7.5, 6.0, 8.0, 7.0, 9.5, 8.0, 6.5, 7.5],
    'diemWeb': [7.0, 8.5, 6.0, None, 7.5, 8.0, 6.5, 9.5, 8.0, 7.0],
    'diemDatabase': [8.0, 7.5, 9.0, 6.5, 8.5, 7.0, 9.5, None, 6.0, 7.5],
}
#2. đọc file và kiểm tra du liệu null
df_input = pandas.DataFrame(data_dict)
print(df_input)
print()
#3. điền giá trị null bằng 0
df_input_filled = df_input.fillna(0)
print(df_input_filled)
#4. tạo cột diemTB = (diemPython + diemWeb + diemDatabase)/3
df_input_filled['diemTB'] = (df_input_filled['diemPython'] + df_input_filled['diemWeb'] + df_input_filled['diemDatabase']) / 3
print(df_input_filled)
#5. tạo cột xepLoai dựa trên diemTB: >=8.0: Giỏi, >=6.5 Khá, 5: Trung bình, <5: Yếu
def xep_loai(diem_tb):
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"
df_input_filled['xepLoai'] = df_input_filled['diemTB'].apply(xep_loai)
print(df_input_filled)
#6. thống kê dư liệu theo cột lớp
lop_counts = df_input_filled['lop'].value_counts()
print(lop_counts)
#7. tính điểm trung bình của từng lớp
lop_diemTB_mean = df_input_filled.groupby('lop')['diemTB'].mean()
print(lop_diemTB_mean)
#8. tạo 1 bảng thông tin lớp với các cột: lop, giaovien, PhongHoc
class_info_dict = {
    'lop': ['23CT5', '23CT6', '23CT7', '23CT8', '23CT9'],
    'giaovien': ['GV A', 'GV B', 'GV C', 'GV D', 'GV E'],
    'PhongHoc': ['P101', 'P102', 'P103', 'P104', 'P105']
}
df_class_info = pandas.DataFrame(class_info_dict)
print(df_class_info)
#9. ghép bảng dũ liệu sinh viên với bảng thông tin lớp dựa trên cột lop
df_merged = pandas.merge(df_input_filled, df_class_info, on='lop', how='left')
print(df_merged)