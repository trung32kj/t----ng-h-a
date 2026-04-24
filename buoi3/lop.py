class car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year
    def display_info(self):
        print("Tên xe: ", self.name)
        print("Màu xe: ", self.color)
        print("Năm sản xuất: ", self.year)
car1 = car("Toyota Camry", "Đen", 2020)
car2 = car("Honda Civic", "Trắng", 2019)