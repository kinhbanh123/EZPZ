class Customer:
    def __init__(self,name,address):
        self.name = name
        self.address = address

class Order:
    def __init__(self,date,status):
        self.date = date
        self.status = status
        self.subTotalList = []
        self.taxList = []
        self.weightList = []
    def calcSubTotal(self,detail):
        self.subTotalList.append(detail.calcSubTotal())
        return sum(self.subTotalList)
    def calcTax(self,detail):
        self.taxList.append(detail.calcTax())  
        return sum(self.taxList)
    def calcTotal(self):
        return self.calcSubTotal() - self.calcTax()
    def calcWeight(self,detail):
        self.weightList.append(detail.calcWeight())
        return sum(self.weightList)
    def calcWeightMoney(self):
        return sum(self.weightList) * float
        
class OrderDetail:
    def __init__(self,quantity,taxStatus):
        self.quantity = quantity    
        self.taxStatus = taxStatus
    def calcSubTotal(self,item):
        if self.quantity <= item.inStock():
            return self.quantity * item.getPriceForQuantity()
        else:
            return item.inStock() * item.getPriceForQuantity
    def calcWeight(self,item):
        return item.shippingWeight * self.quantity
    def calcTax(self,item):
        return (item.getTax()/100) * self.calcSubTotal(item) * self.quantity

class Item:
    def __init__(self,shippingWeight,description):
        self.shippingWeight = shippingWeight 
        self.description = description 
    def getPriceForQuantity(self):
        a = self.description
        a = a.split(",")
        return  float(a[0])
    def getTax(self):
        a = self.description
        a = a.split(",")
        return float(a[1]) 
    def inStock(self):
        a = self.description
        a = a.split(",")
        return int(a[2]) 

class Payment:
    def __int__(self,amount):
        self.amount = amount
    def payMoney(self,order):
        a = self.amount
        b = order.calcTotal()
        if a < b:
            print("You have no enough money to pay")
        else:
            print("Thank you for paying! This is the change: ",b - a)

class Cash(Payment):
    def __init__(self,amount,cashTendered):
        super().__init__(amount)
        self.cashTendered = cashTendered

class Check(Payment):
    def __init__(self,amount,name,bankID):
        super().__init__(amount)
        self.name = name
        self.bankID = bankID
    def authorize(self):
        check_authorize = input("Authorize(press 1) or not (press 0)")
        if check_authorize == "1":
            return True
        else:
            return False
    def payMoney(self):
        if self.authorize() == True:
            super().payMoney()
        else:
            print("You must authorize")
    
class Credit(Payment):
    def __init__(self,amount,number,type,expDate):
        super().__init__(amount)
        self.number = number
        self.type = type
        self.expDate = expDate
    def authorize(self):
        check_authorize = input("Authorize(press 1) or not (press 0)")
        if check_authorize == "1":
            return True
        else:
            return False
    def payMoney(self):
        if self.authorize() == True:
            super().payMoney()
        else:
            print("Confirm")
