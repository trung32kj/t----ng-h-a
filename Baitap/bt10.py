import pandas as pd
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Import cấu hình email
try:
    from email_config import EMAIL_CONFIG
except ImportError:
    print("❌ Không tìm thấy file email_config.py")
    print("💡 Vui lòng tạo file email_config.py với thông tin email của bạn")
    EMAIL_CONFIG = {
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "sender_email": "your_email@gmail.com",
        "sender_password": "your_app_password",
        "receiver_email": "recipient@gmail.com"
    }

class PhatNguoiRPA:
    def __init__(self):
        self.driver = None
        self.website_url = "https://www.phatnguoixe.com/"
        self.smtp_server = EMAIL_CONFIG["smtp_server"]
        self.smtp_port = EMAIL_CONFIG["smtp_port"]
        self.email_user = EMAIL_CONFIG["sender_email"]
        self.email_password = EMAIL_CONFIG["sender_password"]
        self.email_to = EMAIL_CONFIG["receiver_email"]
        
    def setup_driver(self):
        try:
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
            print("✅ Khởi tạo WebDriver thành công")
            return True
        except Exception as e:
            print(f"❌ Lỗi khởi tạo WebDriver: {e}")
            return False
    
    def read_license_plates(self, file_path="bien_so_xe_new.xlsx"):
        try:
            if not os.path.exists(file_path):
                print(f"❌ Không tìm thấy file: {file_path}")
                print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
                return []
            
            df = pd.read_excel(file_path)
            
            if df.empty or 'bien_so' not in df.columns:
                print("❌ File Excel không hợp lệ hoặc thiếu cột 'bien_so'")
                print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
                return []
            
            if 'loai_xe' not in df.columns:
                df['loai_xe'] = 'Ô Tô'
            
            df = df.dropna(subset=['bien_so'])
            
            if len(df) == 0:
                print("❌ Không có biển số hợp lệ trong file")
                print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
                return []
            
            vehicles = df[['bien_so', 'loai_xe']].to_dict('records')
            print(f"📋 Đọc được {len(vehicles)} xe từ {file_path}")
            return vehicles
            
        except Exception as e:
            print(f"❌ Lỗi đọc file Excel: {e}")
            print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
            return []
    
    def open_website(self):
        try:
            print(f"🌐 Đang truy cập: {self.website_url}")
            self.driver.get(self.website_url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("✅ Mở website thành công")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"❌ Lỗi mở website: {e}")
            return False
    
    def select_vehicle_type(self, vehicle_type="Ô Tô"):
        try:
            vehicle_mapping = {"Ô Tô": "1", "Xe Máy": "2", "Xe Máy Điện": "3"}
            
            if vehicle_type not in vehicle_mapping:
                vehicle_type = "Ô Tô"
            
            value = vehicle_mapping[vehicle_type]
            radio_element = self.driver.find_element(By.XPATH, f"//input[@name='loaixe' and @value='{value}']")
            radio_element.click()
            print(f"✅ Đã chọn loại phương tiện: {vehicle_type}")
            time.sleep(1)
            return True
        except Exception as e:
            print(f"❌ Lỗi chọn loại phương tiện {vehicle_type}: {e}")
            return True
    
    def input_license_plate(self, license_plate):
        try:
            input_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "bienso96"))
            )
            input_element.clear()
            input_element.send_keys(license_plate)
            print(f"✅ Đã nhập biển số: {license_plate}")
            time.sleep(1)
            return True
        except Exception as e:
            print(f"❌ Lỗi nhập biển số {license_plate}: {e}")
            return False
    
    def click_check_button(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit99"))
            )
            button.click()
            print("✅ Đã click nút 'KIỂM TRA PHẠT NGUỘI'")
            time.sleep(5)
            return True
        except Exception as e:
            print(f"❌ Lỗi click nút kiểm tra: {e}")
            return False
    
    def get_violation_result(self, license_plate):
        try:
            time.sleep(3)
            
            no_violation_texts = ["Không tìm thấy vi phạm", "Không có vi phạm", "No violation found", "Không có dữ liệu"]
            page_text = self.driver.page_source.lower()
            
            for text in no_violation_texts:
                if text.lower() in page_text:
                    print(f"✅ {license_plate}: Không có vi phạm")
                    return {"license_plate": license_plate, "has_violation": False, "details": "Không có vi phạm"}
            
            tables = self.driver.find_elements(By.TAG_NAME, "table")
            violation_details = []
            
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                if len(rows) > 1:
                    for row in rows[1:]:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 3:
                            violation_details.append({
                                "time": cells[0].text if len(cells) > 0 else "N/A",
                                "location": cells[1].text if len(cells) > 1 else "N/A", 
                                "violation": cells[2].text if len(cells) > 2 else "N/A"
                            })
            
            if violation_details:
                print(f"⚠️ {license_plate}: Có {len(violation_details)} vi phạm")
                return {"license_plate": license_plate, "has_violation": True, "details": violation_details}
            
            print(f"❓ {license_plate}: Không xác định được kết quả")
            return {"license_plate": license_plate, "has_violation": False, "details": "Không xác định được kết quả"}
            
        except Exception as e:
            print(f"❌ Lỗi lấy kết quả cho {license_plate}: {e}")
            return {"license_plate": license_plate, "has_violation": False, "details": f"Lỗi: {e}"}
    
    def send_violation_email(self, result):
        try:
            vehicle_type = result.get('vehicle_type', 'Không xác định')
            
            text = f"""🚨 CẢNH BÁO PHẠT NGUỘI 🚨

Thông báo vi phạm giao thông:

📋 Biển số: {result['license_plate']}
🚗 Loại xe: {vehicle_type}
⚠️ Trạng thái: Có vi phạm

Chi tiết vi phạm:
"""
            
            if isinstance(result['details'], list):
                for i, detail in enumerate(result['details'], 1):
                    text += f"""
Vi phạm {i}:
- ⏰ Thời gian: {detail.get('time', 'N/A')}
- 📍 Địa điểm: {detail.get('location', 'N/A')}
- 🚫 Lỗi vi phạm: {detail.get('violation', 'N/A')}
"""
            else:
                text += f"\n{result['details']}"
            
            text += f"""

---
🤖 Email được gửi tự động bởi RPA Bot
📅 Thời gian: {time.strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            message = MIMEText(text, "plain")
            message["Subject"] = f"🚨 Cảnh báo phạt nguội - {result['license_plate']}"
            message["From"] = self.email_user
            message["To"] = self.email_to
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.email_user, self.email_password)
                server.sendmail(self.email_user, self.email_to, message.as_string())
            
            print(f"📧 Đã gửi email cảnh báo cho: {result['license_plate']} ({vehicle_type})")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi gửi email: {e}")
            return False
    
    def process_vehicle(self, vehicle):
        license_plate = vehicle['bien_so']
        vehicle_type = vehicle['loai_xe']
        
        print(f"\n🔍 Đang kiểm tra: {license_plate} ({vehicle_type})")
        print("-" * 50)
        
        try:
            if not self.open_website():
                return None
            
            self.select_vehicle_type(vehicle_type)
            
            if not self.input_license_plate(license_plate):
                return None
            
            if not self.click_check_button():
                return None
            
            result = self.get_violation_result(license_plate)
            result['vehicle_type'] = vehicle_type
            
            if result['has_violation']:
                print(f"⚠️ Phát hiện vi phạm cho {license_plate} ({vehicle_type})")
                self.send_violation_email(result)
            else:
                print(f"✅ {license_plate} ({vehicle_type}): Không có vi phạm")
            
            return result
            
        except Exception as e:
            print(f"❌ Lỗi xử lý {license_plate}: {e}")
            return None
    
    def run_rpa(self, excel_file="bien_so_xe_new.xlsx"):
        print("🚀 BẮT ĐẦU RPA KIỂM TRA PHẠT NGUỘI")
        print("=" * 60)
        
        try:
            vehicles = self.read_license_plates(excel_file)
            
            if not vehicles or len(vehicles) == 0:
                return []
            
            if not self.setup_driver():
                return []
            
            results = []
            violations_found = 0
            
            for vehicle in vehicles:
                result = self.process_vehicle(vehicle)
                if result:
                    results.append(result)
                    if result['has_violation']:
                        violations_found += 1
                time.sleep(2)
            
            print("\n" + "=" * 60)
            print("📊 KẾT QUẢ TỔNG KẾT")
            print("=" * 60)
            print(f"📋 Tổng số xe kiểm tra: {len(vehicles)}")
            print(f"⚠️ Số xe có vi phạm: {violations_found}")
            print(f"✅ Số xe không vi phạm: {len(vehicles) - violations_found}")
            
            if violations_found > 0:
                print(f"\n📧 Đã gửi {violations_found} email cảnh báo")
            
            print("\n🎉 HOÀN THÀNH RPA KIỂM TRA PHẠT NGUỘI")
            print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
            
            return results
            
        except Exception as e:
            print(f"❌ Lỗi chạy RPA: {e}")
            print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
            return []
            
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 Đã đóng WebDriver")

def main():
    print("🚀 KHỞI ĐỘNG RPA KIỂM TRA PHẠT NGUỘI")
    print(f"📧 Email: {EMAIL_CONFIG['sender_email']} → {EMAIL_CONFIG['receiver_email']}")
    print("=" * 50)
    
    # Kiểm tra cấu hình email
    if EMAIL_CONFIG["sender_email"] == "your_email@gmail.com":
        print("⚠️ CẢNH BÁO: Chưa cấu hình email!")
        print("💡 Vui lòng chỉnh sửa file email_config.py với thông tin email của bạn")
        print("🔚 KẾT THÚC CHƯƠNG TRÌNH")
        return
    
    bot = PhatNguoiRPA()
    bot.run_rpa()

if __name__ == "__main__":
    main()