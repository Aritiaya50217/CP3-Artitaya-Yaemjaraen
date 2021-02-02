
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "12345":
        return showMenu()
    else:
        print("Error !!!") 
        return login()
def showMenu():
    print("----Welcome to iShop----")
    print("1. Vat Caculator")
    print("2. Price Caculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input()) # ตัวแปรที่ user เลือก
    if userSelected == 1:
        return vatCalculator(int(input("Price (THB): ")))
    elif userSelected == 2 :
        return priceCalculator()
    else:
        print("Please enter the number !!")
        return menuSelect()

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat/100)
    return str(result)+" THB"

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2) #ใช้ vatCalculator เพื่อให้คิดvatแล้ว

print(login())
print("Thank you :)")   