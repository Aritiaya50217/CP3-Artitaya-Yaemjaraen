systemMenu = {'ข้าวหมกไก่':35,'ข้าวไก่ทอด':40,'ข้าวหมูทอด':35}
menuList = [] 

def showBill():
    totalPrice = 0
    print("-----My Food ----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("Total",totalPrice,"THB")
    
while True:
    nameMenu = input("Please Enter Menu : ")
    if (nameMenu.lower() =="exit"):
        break
    else:
        menuList.append([nameMenu,systemMenu[nameMenu]]) 

print(menuList)
showBill()  