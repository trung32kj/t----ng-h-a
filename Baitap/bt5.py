from abc import ABC, abstractmethod

# 1. Class Employee (Lớp trừu tượng)
class Employee(ABC):
    def __init__(self, employee_id, name, salary):
        self.id = employee_id
        self.name = name
        self.__salary = salary  # Thuộc tính private (Encapsulation)

    # Getter cho salary
    def get_salary(self):
        return self.__salary

    # Setter cho salary
    def set_salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Lương không thể là số âm!")

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng buộc các lớp con phải định nghĩa lại"""
        pass

    def display_info(self):
        print(f"ID: {self.id} | Tên: {self.name} | Lương cơ bản: {self.get_salary()}")

# 2. Class Developer kế thừa từ Employee
class Developer(Employee):
    def __init__(self, employee_id, name, salary, programming_language, overtime_hours):
        super().__init__(employee_id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        # Lương = salary + overtime_hours * 200
        return self.get_salary() + (self.overtime_hours * 200)

    def display_info(self):
        super().display_info()
        print(f"Chuyên môn: {self.programming_language} | Tăng ca: {self.overtime_hours}h")
        print(f"==> Tổng thu nhập: {self.calculate_salary()}")

# 3. Class Manager kế thừa từ Employee
class Manager(Employee):
    def __init__(self, employee_id, name, salary, bonus):
        super().__init__(employee_id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        # Lương = salary + bonus
        return self.get_salary() + self.bonus

    def display_info(self):
        super().display_info()
        print(f"Tiền thưởng: {self.bonus}")
        print(f"==> Tổng thu nhập: {self.calculate_salary()}")

# --- CHƯƠNG TRÌNH CHÍNH (DEMO) ---
if __name__ == "__main__":
    print("--- QUẢN LÝ NHÂN VIÊN ---")
    
    # Tạo đối tượng Developer
    dev = Developer("D001", "Nguyễn Văn A", 1000, "Python", 10)
    dev.display_info()
    
    print("-" * 30)
    
    # Tạo đối tượng Manager
    mgr = Manager("M001", "Trần Thị B", 2000, 500)
    mgr.display_info()