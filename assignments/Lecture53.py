totalPrice = int(input())
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculate(totalPrice))