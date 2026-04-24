# def serch(a):
#     
# serch(10)
# 2
# def serch(a):
#     return [i for i in range(1, a+1) if i%2==0]
# print(serch(10))

#3
# def tong(a, b):
#     tong = a+b
#     # return tong, "abc"

# retult1 = tong(5, 10)
# print("type result: ", type(retult1))
# result2,mystr = serch(5, 10)
# print("type result: ", type(result2))
# print("type mystr: ", type(mystr))

#4
def serch(a):
   return sum(i for i in range(1, a+1) if i%2==0)
print(serch(10))