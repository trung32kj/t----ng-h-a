from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
Url = "https://sinhvien.dau.edu.vn/sinh-vien-dang-nhap.html"
driver.get(Url)

#UserName
UserName = driver.find_element(By.ID,"UserName")
UserName.click()
UserName.send_keys("2351220236")
#Password
Password = driver.find_element(By.ID,"Password")
Password.click()
Password.send_keys("trung123456")
#Captcha <img border="0" class=" captcha-input imgcaptcha_43277" float="left" href="javascript:void(0)" id="newcaptcha" src="/WebCommon/GetCaptcha" style="padding-right: 5px; max-height: 35px">
Captcha = driver.find_element(By.ID,"Captcha")
Captcha.click()
Captcha.send_keys(input("Nhập Captcha: "))
#click button (<input type="submit" class="button" value="Đăng nhập">)
Login = driver.find_element(By.XPATH,"//input[@type='submit']")
Login.click()

print()
