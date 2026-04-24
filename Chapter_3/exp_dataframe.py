import pandas as pd

data_dict = {
    'ten': ['Trung', 'Hùng', 'Lan'],
    'lop': ['23CT5', '23CT6', '23CT7'],
    'diem': [8.5, 9.0, 7.5],
    'tuoi': [21, 22, 20],
}

df_input = pd.DataFrame(data_dict)
print(df_input)
print()

# thêm một cột địa chỉ
df_input['dia_chi'] = ['Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng']

#truy xuất cột tên
print(df_input['ten'])
print("------------------")

#truy xuất cột điểm
print(df_input['diem'])
print("------------------")

#truy xuất hàng
print(df_input.loc[0])
print("------------------")
print(df_input.loc[1])
print("------------------")
print(df_input.loc[1, "ten"])
print("------------------")
print(df_input.loc[2, "diem"])

#lấy ra giá trị 

#lọc ra những học sinh có điểm >=8.0 và lớp 23CT5
df_input_filtered = df_input[(df_input['diem'] >= 8.0) & (df_input['lop'] == '23CT5')]
print(df_input_filtered)
#so sánh None (null) với ""
my_var = None
my_str = ""
my_name = "Trung"
print()

#xóa dữ liệu hàng NaN
print(df_input.dropna())

# điền giá trị NaN
print(df_input.fillna("0"))

print("------------------------")
#groupby: cột lớp - lấy bảng điểm theo lớp
df_group_by = df_input.groupby('lop')
print(df_group_by)
for i_group in df_group_by:
    print(i_group)
    print("------------------")
print() 
