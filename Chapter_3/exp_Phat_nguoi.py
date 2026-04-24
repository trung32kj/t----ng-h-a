from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select # Thêm thư viện chuyên dụng cho dropdown
import time
driver = webdriver.Chrome()
url = "https://phatnguoi.com/"
driver.get(url)

# 1. Chọn loại xe là "Xe máy"
# Cách dùng thư viện Select sẽ chính xác và ổn định hơn click/send_keys thông thường
dropdown_element = driver.find_element(By.XPATH,'//*[@id="loaixe"]/option[2]')
dropdown_element.click() # Click vào dropdown để mở ra các lựa chọn
# 2. Nhập biển số xe
# Dựa trên cấu trúc trang phatnguoi.com, ID của ô nhập biển số thường là "bs" hoặc "bienso"
# Ở đây mình giả định ID là "bienso" (bạn hãy kiểm tra lại bằng F12 nhé)
bien_so_input = driver.find_element(By.ID, "bsxinput") 
bien_so_input.clear() # Xóa trắng ô nhập trước khi điền
bien_so_input.send_keys("29A1-12345") # Thay bằng biển số bạn muốn tra

# 3. bỏ qua ifreame
driver.switch_to.frame("cf-chl-widget-xc74g") # Thay "iframeResult" bằng ID hoặc tên của iframe chứa nút Tra cứu

# 3. Nhấn nút Tra cứu (Thường có class hoặc ID cụ thể)
# Ví dụ: btn_search = driver.find_element(By.XPATH, "//button[@type='submit']")
# btn_search.click()

print("Đã nhập thông tin thành công!")
time.sleep(5) # Tạm dừng để bạn quan sát kết quả
driver.quit()