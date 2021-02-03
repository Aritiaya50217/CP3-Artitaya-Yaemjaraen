menuList = [] 

def showBill():
    totalPrice = 0
    print("-----My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1]) 
        totalPrice += int(menuList[number][1])# totalPrice ได้จากการ +ราคาไปเรื่อยๆตามรอบของ number ส่วน [1] คือตำแหน่งของราคาใน list ย่อย
    print("Total",totalPrice,"THB")
       
while True:
    nameMenu = input("Please Enter Menu : ")
    if (nameMenu.lower() =="exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([nameMenu,menuPrice]) 

showBill()