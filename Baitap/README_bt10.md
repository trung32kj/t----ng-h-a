# RPA Bot Kiểm Tra Phạt Nguội

## 📋 Mô tả
Bot RPA tự động kiểm tra phạt nguội từ website https://www.phatnguoixe.com/ và gửi email cảnh báo khi phát hiện vi phạm.

## 🚀 Cách sử dụng

### 1. Cấu hình Email
```bash
# Copy file template
cp email_config_template.py email_config.py

# Chỉnh sửa email_config.py với thông tin của bạn
```

### 2. Chuẩn bị dữ liệu
Tạo file `bien_so_xe_new.xlsx` với 2 cột:
- `bien_so`: Biển số xe (VD: 51F-777.77)
- `loai_xe`: Loại xe (Ô Tô / Xe Máy / Xe Máy Điện)

### 3. Chạy chương trình
```bash
python bt10.py
```

## 📧 Cấu hình Gmail

1. **Bật 2-Step Verification:**
   - Đăng nhập Gmail → Quản lý tài khoản Google
   - Bảo mật → Xác minh 2 bước → Bật

2. **Tạo App Password:**
   - Bảo mật → Mật khẩu ứng dụng
   - Chọn "Mail" và thiết bị
   - Copy mật khẩu 16 ký tự

3. **Cập nhật email_config.py:**
   ```python
   EMAIL_CONFIG = {
       "sender_email": "your_email@gmail.com",
       "sender_password": "abcdefghijklmnop",  # App Password
       "receiver_email": "recipient@gmail.com"
   }
   ```

## 🔒 Bảo mật
- File `email_config.py` đã được thêm vào `.gitignore`
- Không chia sẻ App Password với ai
- Sử dụng `email_config_template.py` để chia sẻ code

## 📦 Yêu cầu
```bash
pip install pandas selenium openpyxl
```

## 🚗 Loại xe hỗ trợ
- **Ô Tô** (value="1")
- **Xe Máy** (value="2") 
- **Xe Máy Điện** (value="3")