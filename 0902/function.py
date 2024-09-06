#無參數的函式
def novar():
   print("AWS")


novar()

#有參數的函式
def var(x,y):
    print(x+y)

var(3,2)

#有參數、有return的python def
def find_max():
    numbers = [10, 20, 30, 40, 50,60]
    return max(numbers)

max_value = find_max()
print(max_value)


