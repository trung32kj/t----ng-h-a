import pandas

name = ["An", "Hòa", "Bình", "Tiến"]
data_Series = pandas.Series(data = name, name= "Name")
print(data_Series)

Age = ["22","23","21" ,"15"]
data_Series_Age = pandas.Series(data = Age, name= "tuổi")
print(data_Series_Age)
data_Frame = pandas.DataFrame(data = {"Name": name, "Age": Age})
print(data_Frame)