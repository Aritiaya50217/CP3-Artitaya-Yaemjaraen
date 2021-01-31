Username = input("username : ")
Password = input("password : ")
if Username == "oil" and Password == "50217" :
    print("Welcome !!")
    print("1. Water 10 THB")
    print("2. Pepsi 15 THB")
    userSelection = int(input())
    if userSelection == 1 :
        quantityWater = int(input("QuantityWater : "))
        priceWater = 10
        result = quantityWater * priceWater
        print(result,"THB")
    elif userSelection == 2 :
        quantityPepsi = int(input("Quantity : "))
        pricePepsi = 15
        total = quantityPepsi * pricePepsi
        print(total,"THB")
else:
    print("Error !!")


