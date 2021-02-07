class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Add to Cart",self.name,self.lastName,self.age)

Customer1 = Customer()
Customer1.name = "Artitaya"
Customer1.lastName = "Yaemjaraen"
Customer1.age = 23
Customer1.addCart()

Customer2 = Customer()
Customer2.name = "Montita"
Customer2.lastName = "Phummark"
Customer2.age = 22
Customer2.addCart()

Customer3 = Customer()
Customer3.name = "Parinya"
Customer3.lastName = "Phobai"
Customer3.age = 23
Customer3.addCart()

Customer4 = Customer()
Customer4.name = "Wanida"
Customer4.lastName = "Suwannakit"
Customer4.age = 27
Customer4.addCart()