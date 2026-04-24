import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PhatNguoiScanner:
    def __init__(self):
        self.driver = None
        self.website_url = "https://www.phatnguoixe.com/"
        self.found_violation = False
        self.violation_license_plate = None
        
        # Danh sách mã tỉnh thành phổ biến
        self.province_codes = [
            "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",  # TP.HCM
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",        # Hà Nội
            "43", "47", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "92", "93", "94", "95", "97", "98", "99"
        ]
        
        # Chữ cái sử dụng trong biển số
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "K", "L", "M", "N", "P", "S", "T", "U", "V", "X", "Y", "Z"]
        
    def setup_driver(self):
        """Khởi tạo WebDriver"""
        try:
            from selenium.webdriver.chrome.options import Options
            chrome_options = Options()
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            # Thêm option để chạy nhanh hơn
            chrome_options.add_argument("--disable-images")
            chrome_options.add_argument("--disable-javascript")
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.maximize_window()
            print("✅ Khởi tạo WebDriver thành công")
            return True
        except Exception as e:
            print(f"❌ Lỗi khởi tạo WebDriver: {e}")
            return False
    
    def generate_license_plate(self, province_code, letter, number):
        """Tạo biển số theo định dạng Việt Nam: 29A-475.88"""
        # Format: XX[A-Z]-XXX.XX
        number_str = f"{number:05d}"
        return f"{province_code}{letter}-{number_str[:3]}.{number_str[3:]}"
    
    def open_website(self):
        """Mở website phạt nguội"""
        try:
            print(f"🌐 Đang truy cập: {self.website_url}")
            self.driver.get(self.website_url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            print("✅ Mở website thành công")
            time.sleep(1)
            return True
        except Exception as e:
            print(f"❌ Lỗi mở website: {e}")
            return False
    
    def select_vehicle_type(self, vehicle_type="Ô Tô"):
        """Chọn loại phương tiện"""
        try:
            vehicle_mapping = {"Ô Tô": "1", "Xe Máy": "2", "Xe Máy Điện": "3"}
            
            if vehicle_type not in vehicle_mapping:
                vehicle_type = "Ô Tô"
            
            value = vehicle_mapping[vehicle_type]
            radio_element = self.driver.find_element(By.XPATH, f"//input[@name='loaixe' and @value='{value}']")
            radio_element.click()
            print(f"✅ Đã chọn loại phương tiện: {vehicle_type}")
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"❌ Lỗi chọn loại phương tiện {vehicle_type}: {e}")
            return True
    
    def input_license_plate(self, license_plate):
        """Nhập biển số xe"""
        try:
            input_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "bienso96"))
            )
            input_element.clear()
            input_element.send_keys(license_plate)
            time.sleep(0.5)
            return True
        except Exception as e:
            print(f"❌ Lỗi nhập biển số {license_plate}: {e}")
            return False
    
    def click_check_button(self):
        """Click nút kiểm tra"""
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit99"))
            )
            button.click()
            time.sleep(3)
            return True
        except Exception as e:
            print(f"❌ Lỗi click nút kiểm tra: {e}")
            return False
    
    def check_violation_result(self, license_plate):
        """Kiểm tra kết quả vi phạm"""
        try:
            time.sleep(2)
            
            # Danh sách text cho trường hợp không có vi phạm
            no_violation_texts = [
                "Không tìm thấy vi phạm", 
                "Không có vi phạm", 
                "No violation found", 
                "Không có dữ liệu",
                "không tìm thấy",
                "không có dữ liệu"
            ]
            
            page_text = self.driver.page_source.lower()
            
            # Kiểm tra không có vi phạm
            for text in no_violation_texts:
                if text.lower() in page_text:
                    return False
            
            # Kiểm tra có bảng vi phạm
            tables = self.driver.find_elements(By.TAG_NAME, "table")
            violation_found = False
            
            for table in tables:
                rows = table.find_elements(By.TAG_NAME, "tr")
                if len(rows) > 1:  # Có dữ liệu ngoài header
                    for row in rows[1:]:
                        cells = row.find_elements(By.TAG_NAME, "td")
                        if len(cells) >= 3:
                            # Có dữ liệu vi phạm thực sự
                            cell_text = " ".join([cell.text.strip() for cell in cells])
                            if cell_text and not any(no_text.lower() in cell_text.lower() for no_text in no_violation_texts):
                                violation_found = True
                                break
                
                if violation_found:
                    break
            
            return violation_found
            
        except Exception as e:
            print(f"❌ Lỗi kiểm tra kết quả cho {license_plate}: {e}")
            return False
    
    def check_single_license_plate(self, license_plate):
        """Kiểm tra một biển số"""
        try:
            if not self.open_website():
                return False
            
            self.select_vehicle_type("Ô Tô")
            
            if not self.input_license_plate(license_plate):
                return False
            
            if not self.click_check_button():
                return False
            
            has_violation = self.check_violation_result(license_plate)
            
            if has_violation:
                print(f"🚨 PHÁT HIỆN VI PHẠM: {license_plate}")
                self.found_violation = True
                self.violation_license_plate = license_plate
                return True
            else:
                print(f"✅ {license_plate}: Không có vi phạm")
                return False
            
        except Exception as e:
            print(f"❌ Lỗi kiểm tra {license_plate}: {e}")
            return False
    
    def scan_license_plates(self, start_number=0, end_number=99999):
        """Dò biển số từ start_number đến end_number"""
        print("🚀 BẮT ĐẦU DÒ BIỂN SỐ VI PHẠM")
        print("=" * 60)
        print(f"📋 Phạm vi dò: {start_number:05d} -> {end_number:05d}")
        print(f"🎯 Mục tiêu: Tìm biển số có vi phạm đầu tiên")
        print("=" * 60)
        
        try:
            if not self.setup_driver():
                return None
            
            checked_count = 0
            
            for number in range(start_number, end_number + 1):
                license_plate = self.generate_license_plate(number)
                checked_count += 1
                
                print(f"🔍 [{checked_count}] Đang kiểm tra: {license_plate}")
                
                if self.check_single_license_plate(license_plate):
                    # Tìm thấy vi phạm - dừng ngay
                    print("\n" + "=" * 60)
                    print("🎯 KẾT QUẢ DÒ BIỂN SỐ")
                    print("=" * 60)
                    print(f"🚨 Tìm thấy vi phạm tại: {self.violation_license_plate}")
                    print(f"� Đã kiểm tra: {checked_count} biển số")
                    print(f"⏱️ Dừng tại biển số thứ: {number + 1}")
                    print("🔚 KẾT THÚC QUÉT")
                    return self.violation_license_plate
                
                # Nghỉ ngắn giữa các lần kiểm tra
                time.sleep(1)
                
                # Hiển thị tiến độ mỗi 100 biển số
                if checked_count % 100 == 0:
                    print(f"📈 Đã kiểm tra {checked_count} biển số...")
            
            # Không tìm thấy vi phạm nào
            print("\n" + "=" * 60)
            print("📊 KẾT QUẢ DÒ BIỂN SỐ")
            print("=" * 60)
            print(f"✅ Đã kiểm tra hết {checked_count} biển số")
            print("❌ Không tìm thấy vi phạm nào")
            print("🔚 KẾT THÚC QUÉT")
            return None
            
        except KeyboardInterrupt:
            print("\n⚠️ Người dùng dừng chương trình")
            print(f"📊 Đã kiểm tra: {checked_count} biển số")
            return None
            
        except Exception as e:
            print(f"❌ Lỗi trong quá trình dò: {e}")
            return None
            
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 Đã đóng WebDriver")

def main():
    print("� CHƯƠNG TRÌNH DÒ BIỂN SỐ VI PHẠM")
    print("📋 Mô tả: Dò biển số từ 00000->99999 đến khi tìm thấy vi phạm đầu tiên")
    print("⚠️ Lưu ý: Không gửi email, chỉ kiểm tra và dừng khi có vi phạm")
    print("=" * 60)
    
    scanner = PhatNguoiScanner()
    
    # Tùy chọn: có thể thay đổi phạm vi dò
    start_num = 0
    end_num = 99999
    
    # Hỏi người dùng có muốn thay đổi phạm vi không
    try:
        user_input = input(f"Nhấn Enter để dò từ {start_num:05d}->{end_num:05d} hoặc nhập phạm vi mới (vd: 0-1000): ").strip()
        if user_input:
            if '-' in user_input:
                start_str, end_str = user_input.split('-')
                start_num = int(start_str.strip())
                end_num = int(end_str.strip())
                print(f"✅ Sẽ dò từ {start_num:05d} đến {end_num:05d}")
    except:
        print("⚠️ Sử dụng phạm vi mặc định")
    
    result = scanner.scan_license_plates(start_num, end_num)
    
    if result:
        print(f"\n🎉 Hoàn thành! Tìm thấy vi phạm tại: {result}")
    else:
        print(f"\n✅ Hoàn thành! Không tìm thấy vi phạm nào trong phạm vi đã dò")

if __name__ == "__main__":
    main()