
def function(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


a = int(input("Число первое"))
b = int(input("Число второе"))
c = int(input("Число третье"))

print("Максимум из чисел", function(a, b, c))





