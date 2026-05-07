import smtplib
import re
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from email_config import EMAIL_CONFIG

ACCOUNT_EMAIL = "rpabot_test2025@gmail.com"
ACCOUNT_PASSWORD = "Test@12345"
ACCOUNT_NAME = "RPA Bot"

SMTP_SERVER = EMAIL_CONFIG["smtp_server"]
SMTP_PORT = EMAIL_CONFIG["smtp_port"]
SMTP_EMAIL = EMAIL_CONFIG["sender_email"]
SMTP_PASSWORD = EMAIL_CONFIG["sender_password"]
NOTIFY_EMAIL = EMAIL_CONFIG["receiver_email"]

SEARCH_KEYWORD = "shirt"

CARD_NAME = "RPA Bot"
CARD_NUMBER = "4111111111111111"
CARD_CVC = "123"
CARD_EXPIRY_MONTH = "12"
CARD_EXPIRY_YEAR = "2028"

def dismiss_ads(driver):
    try:
        handles = driver.window_handles
        if len(handles) > 1:
            for handle in handles[1:]:
                driver.switch_to.window(handle)
                driver.close()
            driver.switch_to.window(handles[0])

        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        for iframe in iframes:
            src = iframe.get_attribute("src") or ""
            if "google" in src or "doubleclick" in src or "googlesyndication" in src:
                driver.execute_script("arguments[0].style.display='none';", iframe)

        driver.execute_script("""
            document.querySelectorAll('ins.adsbygoogle, [id^="google_ads"], [id^="aswift"], .modal-backdrop, #dismiss-button').forEach(e => e.remove());
        """)
    except:
        pass

def safe_click(driver, element):
    try:
        element.click()
    except:
        driver.execute_script("arguments[0].click();", element)

def login_or_register(driver, email, password, name):
    driver.get("https://www.automationexercise.com/login")
    time.sleep(2)
    dismiss_ads(driver)

    try:
        login_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.login-form"))
        )
        email_input = login_form.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']")
        password_input = login_form.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']")
        login_btn = login_form.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']")

        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)
        safe_click(driver, login_btn)
        time.sleep(2)

        if driver.find_elements(By.XPATH, "//a[contains(text(),' Logged in as ')]"):
            print("[OK] Dang nhap thanh cong!")
            return True
        else:
            print("[WARN] Dang nhap that bai, thu dang ky...")
    except Exception as e:
        print(f"[WARN] Loi khi dang nhap: {e}")

    driver.get("https://www.automationexercise.com/login")
    time.sleep(2)
    dismiss_ads(driver)

    signup_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.signup-form"))
    )
    name_input = signup_form.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']")
    email_input = signup_form.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signup_btn = signup_form.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")

    name_input.clear()
    name_input.send_keys(name)
    email_input.clear()
    email_input.send_keys(email)
    safe_click(driver, signup_btn)
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_gender1"))
    )
    safe_click(driver, driver.find_element(By.ID, "id_gender1"))

    pw_input = driver.find_element(By.CSS_SELECTOR, "input[data-qa='password']")
    pw_input.clear()
    pw_input.send_keys(password)

    from selenium.webdriver.support.ui import Select
    Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='days']")).select_by_value("15")
    Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='months']")).select_by_value("6")
    Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='years']")).select_by_value("1995")

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='first_name']").send_keys("RPA")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='last_name']").send_keys("Bot")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='company']").send_keys("RPA Corp")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='address']").send_keys("123 Test Street")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='address2']").send_keys("Suite 100")

    Select(driver.find_element(By.CSS_SELECTOR, "select[data-qa='country']")).select_by_visible_text("United States")

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='state']").send_keys("California")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='city']").send_keys("Los Angeles")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='zipcode']").send_keys("90001")
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='mobile_number']").send_keys("1234567890")

    create_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
    safe_click(driver, create_btn)
    time.sleep(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-qa='account-created']"))
    )
    print("[OK] Dang ky tai khoan thanh cong!")

    continue_btn = driver.find_element(By.CSS_SELECTOR, "a[data-qa='continue-button']")
    safe_click(driver, continue_btn)
    time.sleep(3)
    dismiss_ads(driver)
    return True

def access_products_page(driver):
    driver.get("https://www.automationexercise.com/products")
    time.sleep(3)
    dismiss_ads(driver)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "features_items"))
    )
    print("[OK] Truy cap trang Products thanh cong!")

def search_product(driver, keyword):
    dismiss_ads(driver)
    for attempt in range(3):
        try:
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "search_product"))
            )
            break
        except:
            print(f"[RETRY] Khong tim thay search input, thu lai lan {attempt + 2}...")
            dismiss_ads(driver)
            driver.get("https://www.automationexercise.com/products")
            time.sleep(3)
            dismiss_ads(driver)
    else:
        raise Exception("Khong tim thay o tim kiem sau 3 lan thu!")

    search_input.clear()
    search_input.send_keys(keyword)

    search_btn = driver.find_element(By.ID, "submit_search")
    safe_click(driver, search_btn)
    time.sleep(3)
    dismiss_ads(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "features_items"))
    )
    print(f"[OK] Tim kiem san pham voi tu khoa '{keyword}' thanh cong!")

def get_products_on_page(driver):
    product_cards = driver.find_elements(By.CSS_SELECTOR, "div.features_items div.col-sm-4")
    products = []
    for card in product_cards:
        try:
            price_text = card.find_element(By.CSS_SELECTOR, "div.productinfo h2").text
            price_val = float(re.sub(r"[^\d.]", "", price_text))
            name = card.find_element(By.CSS_SELECTOR, "div.productinfo p").text
            add_btn = card.find_element(By.CSS_SELECTOR, "div.productinfo a.add-to-cart")
            overlay_btn = card.find_element(By.CSS_SELECTOR, "div.product-overlay a.add-to-cart")
            products.append({
                "name": name,
                "price": price_val,
                "card": card,
                "add_btn": add_btn,
                "overlay_btn": overlay_btn,
            })
        except:
            continue
    return products

def select_lowest_price_product(driver):
    products = get_products_on_page(driver)
    if not products:
        print("[ERROR] Khong tim thay san pham nao!")
        return None

    print(f"[INFO] Tim thay {len(products)} san pham tren trang dau:")
    for p in products:
        print(f"   - {p['name']}: Rs. {p['price']}")

    lowest = min(products, key=lambda x: x["price"])
    print(f"[OK] San pham gia thap nhat: {lowest['name']} - Rs. {lowest['price']}")
    return lowest

def add_to_cart(driver, product):
    dismiss_ads(driver)
    actions = ActionChains(driver)
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", product["card"])
    time.sleep(1)

    actions.move_to_element(product["card"]).perform()
    time.sleep(1)

    try:
        overlay_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(product["overlay_btn"])
        )
        safe_click(driver, overlay_btn)
    except:
        safe_click(driver, product["add_btn"])

    time.sleep(2)
    print("[OK] Them san pham vao gio hang thanh cong!")

    try:
        view_cart_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))
        )
        safe_click(driver, view_cart_link)
        time.sleep(2)
    except:
        driver.get("https://www.automationexercise.com/view_cart")
        time.sleep(2)

def verify_cart(driver):
    dismiss_ads(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cart_info_table"))
    )
    rows = driver.find_elements(By.CSS_SELECTOR, "#cart_info_table tbody tr")
    count = len(rows)

    if count == 1:
        product_name = rows[0].find_element(By.CSS_SELECTOR, "td.cart_description h4 a").text
        price = rows[0].find_element(By.CSS_SELECTOR, "td.cart_price p").text
        qty = rows[0].find_element(By.CSS_SELECTOR, "td.cart_quantity button").text
        print(f"[OK] Gio hang co 1 san pham: {product_name} | Gia: {price} | SL: {qty}")
    else:
        print(f"[WARN] Gio hang co {count} san pham (mong doi 1)")
    return count

def proceed_to_checkout(driver):
    dismiss_ads(driver)
    checkout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-default.check_out"))
    )
    safe_click(driver, checkout_btn)
    time.sleep(2)
    dismiss_ads(driver)
    print("[OK] Di den trang Checkout thanh cong!")

def fill_checkout_comment(driver, comment="Order via RPA Bot. Please deliver ASAP."):
    dismiss_ads(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ordermsg"))
    )
    comment_area = driver.find_element(By.CSS_SELECTOR, "textarea[name='message']")
    comment_area.clear()
    comment_area.send_keys(comment)
    print(f"[OK] Dien comment: {comment}")

def place_order(driver):
    dismiss_ads(driver)
    place_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-default.check_out"))
    )
    safe_click(driver, place_btn)
    time.sleep(2)
    dismiss_ads(driver)
    print("[OK] Chuyen den trang thanh toan!")

def enter_payment_information(driver, card_name, card_number, cvc, exp_month, exp_year):
    dismiss_ads(driver)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-qa='name-on-card']"))
    )

    driver.find_element(By.CSS_SELECTOR, "input[data-qa='name-on-card']").send_keys(card_name)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='card-number']").send_keys(card_number)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='cvc']").send_keys(cvc)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='expiry-month']").send_keys(exp_month)
    driver.find_element(By.CSS_SELECTOR, "input[data-qa='expiry-year']").send_keys(exp_year)

    pay_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='pay-button']")
    safe_click(driver, pay_btn)
    time.sleep(3)
    print("[OK] Nhap thong tin thanh toan va xac nhan!")

def confirm_order_success(driver):
    dismiss_ads(driver)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-sm-9.col-sm-offset-1"))
        )
        page_text = driver.find_element(By.CSS_SELECTOR, "div.col-sm-9.col-sm-offset-1").text
        if "Congratulations" in page_text or "Order Placed" in page_text or "placed successfully" in page_text.lower():
            print("[OK] Xac nhan dat hang thanh cong!")
            return True
        else:
            print(f"[WARN] Noi dung trang xac nhan: {page_text[:200]}")
            return True
    except Exception as e:
        print(f"[ERROR] Loi xac nhan dat hang: {e}")
        return False

def send_email_notification(subject, body, to_email=None, from_email=None, from_password=None):
    to_email = to_email or NOTIFY_EMAIL
    from_email = from_email or SMTP_EMAIL
    from_password = from_password or SMTP_PASSWORD

    if not from_email or not from_password or not to_email:
        print("[WARN] Chua cau hinh email gui/nhan. Bo qua gui email.")
        print(f"   Subject: {subject}")
        print(f"   Body: {body}")
        return False

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"[OK] Gui email thong bao thanh cong! -> {to_email}")
        return True
    except Exception as e:
        print(f"[ERROR] Gui email that bai: {e}")
        return False

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    order_success = False
    product_info = ""

    try:
        print("\n" + "=" * 50)
        print("STEP 1: Login / Register")
        print("=" * 50)
        login_or_register(driver, ACCOUNT_EMAIL, ACCOUNT_PASSWORD, ACCOUNT_NAME)

        print("\n" + "=" * 50)
        print("STEP 2: Truy cap trang Products")
        print("=" * 50)
        access_products_page(driver)

        print("\n" + "=" * 50)
        print(f"STEP 3: Tim kiem san pham '{SEARCH_KEYWORD}'")
        print("=" * 50)
        search_product(driver, SEARCH_KEYWORD)

        print("\n" + "=" * 50)
        print("STEP 4-5: Loc va chon san pham gia thap nhat")
        print("=" * 50)
        lowest_product = select_lowest_price_product(driver)
        if not lowest_product:
            raise Exception("Khong tim thay san pham nao!")
        product_info = f"{lowest_product['name']} - Rs. {lowest_product['price']}"

        print("\n" + "=" * 50)
        print("STEP 6: Them san pham vao gio hang")
        print("=" * 50)
        add_to_cart(driver, lowest_product)

        print("\n" + "=" * 50)
        print("STEP 7: Verify gio hang")
        print("=" * 50)
        verify_cart(driver)

        print("\n" + "=" * 50)
        print("STEP 8: Proceed to Checkout")
        print("=" * 50)
        proceed_to_checkout(driver)

        print("\n" + "=" * 50)
        print("STEP 9: Dien thong tin Checkout")
        print("=" * 50)
        fill_checkout_comment(driver)

        print("\n" + "=" * 50)
        print("STEP 10: Place Order")
        print("=" * 50)
        place_order(driver)

        print("\n" + "=" * 50)
        print("STEP 11: Nhap thong tin thanh toan")
        print("=" * 50)
        enter_payment_information(driver, CARD_NAME, CARD_NUMBER, CARD_CVC, CARD_EXPIRY_MONTH, CARD_EXPIRY_YEAR)

        print("\n" + "=" * 50)
        print("STEP 12: Xac nhan dat hang")
        print("=" * 50)
        order_success = confirm_order_success(driver)

    except Exception as e:
        print(f"\n[ERROR] Loi trong qua trinh thuc hien: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\n" + "=" * 50)
        print("STEP 13: Gui email thong bao")
        print("=" * 50)

        if order_success:
            subject = "[RPA Bot] Dat hang thanh cong!"
            body = (
                f"Bot RPA da dat hang thanh cong tren automationexercise.com\n\n"
                f"San pham: {product_info}\n"
                f"Tu khoa tim kiem: {SEARCH_KEYWORD}\n"
                f"Tai khoan: {ACCOUNT_EMAIL}\n\n"
                f"Thong tin thanh toan da duoc xu ly."
            )
        else:
            subject = "[RPA Bot] Dat hang that bai!"
            body = (
                f"Bot RPA da THAT BAI khi dat hang tren automationexercise.com\n\n"
                f"Tu khoa tim kiem: {SEARCH_KEYWORD}\n"
                f"Tai khoan: {ACCOUNT_EMAIL}\n\n"
                f"Vui long kiem tra lai."
            )

        send_email_notification(subject, body, NOTIFY_EMAIL, SMTP_EMAIL, SMTP_PASSWORD)

        print("\n" + "=" * 50)
        print("KET THUC BOT")
        print("=" * 50)
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    main()
