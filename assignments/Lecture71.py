menuList = [] 
priceList = []

def showBill():
    totalPrice = 0  # เอาไว้ใน function เพราะมีการเรียกใช้ภายใน
    print("-----My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number]) # totalPrice ได้จากการ +ราคาไปเรื่อยๆตามรอบของ number
    print("Total",totalPrice,"THB")

while True:
    nameMenu = input("Please Enter Menu : ")
    if (nameMenu.lower() =="exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(nameMenu)
        priceList.append(menuPrice)

showBill()


   