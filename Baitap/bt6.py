from abc import ABC, abstractmethod

# --- Lop cha truuu tuong Account ---
class Account(ABC):
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance  # Thuoc tinh protected

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Nap thanh cong: {amount}. So du hien tai: {self._balance}")
        else:
            print("Loi: So tien nap phai lon hon 0.")

    @abstractmethod
    def withdraw(self, amount):
        """Phuong thuc rut tien phai duoc dinh nghia o lop con"""
        pass

    def display_info(self):
        print("-" * 20)
        print(f"STK: {self.account_number}")
        print(f"Chu tai khoan: {self.owner}")
        print(f"So du: {self._balance}")

# --- Tai khoan Tiet kiem (Co lai suat) ---
class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"Da cong lai suat: {interest}. So du moi: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Rut tien thanh cong: {amount}")
        else:
            print("Loi: So du khong du hoac so tien khong hop le.")

# --- Tai khoan Thanh toan (Co phi giao dich) ---
class CheckingAccount(Account):
    def __init__(self, account_number, owner, balance, fee=5):
        super().__init__(account_number, owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        total = amount + self.fee
        if 0 < total <= self._balance:
            self._balance -= total
            print(f"Rut tien thanh cong: {amount} (Phi: {self.fee})")
        else:
            print("Loi: Khong du so du de thanh toan ca tien rut va phi.")

# --- He thong quan ly ---
class BankSystem:
    def __init__(self):
        self.accounts = {}

    def run(self):
        while True:
            print("\n--- HE THONG NGAN HANG ---")
            print("1. Tao tai khoan")
            print("2. Nap tien")
            print("3. Rut tien")
            print("4. Xem thong tin")
            print("0. Thoat")
            
            choice = input("Chon chuc nang: ")

            if choice == "0":
                print("Ket thuc chuong trinh.")
                break
            
            if choice == "1":
                acc_num = input("Nhap STK: ")
                name = input("Nhap ten chu the: ")
                type_acc = input("Loai (1: Tiet kiem, 2: Thanh toan): ")
                
                if type_acc == "1":
                    self.accounts[acc_num] = SavingsAccount(acc_num, name, 0)
                else:
                    self.accounts[acc_num] = CheckingAccount(acc_num, name, 0)
                print("Tao tai khoan thanh cong.")

            elif choice in ["2", "3", "4"]:
                acc_num = input("Nhap STK: ")
                acc = self.accounts.get(acc_num)
                
                if not acc:
                    print("Loi: Khong tim thay tai khoan.")
                    continue
                
                if choice == "2":
                    val = float(input("So tien nap: "))
                    acc.deposit(val)
                elif choice == "3":
                    val = float(input("So tien rut: "))
                    acc.withdraw(val)
                elif choice == "4":
                    acc.display_info()
            else:
                print("Loi: Lua chon khong hop le.")

if __name__ == "__main__":
    bank = BankSystem()
    bank.run()