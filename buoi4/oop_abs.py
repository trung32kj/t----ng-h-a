# Bài toán hệ thống thanh toán 
# ví dụ 
#1.Chuyển tiền từ ngân hàng: stk - stk
#2. Chuyển tiền trong thẻ tín dụng 

#Quy tắc :
# 1. Kiểm tra stk hộp lệ
# 2. Kiểm trs số dư
# 3. Chuyển tiền
# 4. Tính phi(Free)

# Giải quyết : Tạo ra các quy tắc để hệ thống con tuân theo
from abc import ABC, abstractmethod

class Payment(ABC):
    # 1. Kiểm tra stk hộp lệ
    def check_account_number(self):
        pass
    # 2. Kiểm tra số dư
    def check_balance(self):
        pass
    # 3. Chuyển tiền
    def transfer(self):
        pass
    # 4. Tính phi(Free)
    def calculate_fee(self):
        pass

#1.Chuyển tiền từ ngân hàng: stk - stk
class PaymentVietcombank(Payment):
    def __init__(self, account_number):
        super().__init__()
        self.acccount_number = account_number
        self.balance = 0
    def check_account_number(self):
        if self.acccount_number == "00000000":
            return True
        elif len(self.acccount_number) < 8:
            return False
        elif len(self.acccount_number) > 13:
            return False
        else:
            return True

    # 2. Kiểm tra số dư
    def check_balance(self):
        if self.balance > 2000:
            return True
        else:
            return False

    # 3. Chuyển tiền
    def transfer(self, amount):
        print(" Chuyển tiền; ", amount)
        self.balance -= amount
        return self.balance        
    # 4. Tính phi(Free)
    def calculate_fee(self):
        pass

class PaymentCredit(Payment):
    def __init__(self, account_number):
        super().__init__()
        self.acccount_number = account_number
        self.balance = 0
    # 1. Kiểm tra stk hộp lệ
    def check_balance(self):
        if self.balance > 150000:
            return True
        else:
            return False

    # 3. Chuyển tiền
    def transfer(self, amount):
        print(" Chuyển tiền; ", amount)
        self.balance -= amount
        return self.balance
    # 3. Chuyển tiền
    def transfer(self):
        pass
    # 4. Tính phi(Free)
    def calculate_fee(self):
        print(" Tính phí theo % tiền giao dịch : 1%")
        number_fee = (self.balance / 100) *0.1
        return number_fee


#2. Chuyển tiền trong thẻ tín dụnga