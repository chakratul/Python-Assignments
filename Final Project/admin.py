from numpy import random
import json as js

class admin:
    def __init__(self,FoodID,Name,Quantity,Price,Discount,Stock):
        self.FoodID = FoodID
        self.Name = Name
        self.Quantity = Quantity
        self.Price= Price
        self.Discount = Discount
        self.Stock = Stock        
        self.menu = {}

        
    def add_food(self): 
        p = input("Please Enter the Login Password to access the data base : ") 
        if p =="12345":
            ch= 0
            while ch != '2':
                ch = input("ENTER A CHOICE EITHER 1 OR 2 : ")
                if ch == '1':
                    self.FoodID = []
                    x = random.randint(1,100,1)
                    while self.FoodID != x:
                        self.FoodID.append(x)
                        x+=1
                        break
                    self.Name = input("Enter Food Name : ")
                    self.Quantity = input("Enter Food Quantity : ")
                    self.Price = int(input("Enter Food Price : "))
                    self.Discount = int(input("Enter Discount for the Food : "))
                    self.Stock = int(input("Enter Stock of Food : "))        
                    self.menu = {self.FoodID:[self.Name,self.Quantity,self.Price,self.Discount,self.Stock]}
        
                    f = open("Menu.json",'a')
                    c = str(self.menu)
                    js.dump(c,f)
                    f.close
                    print(self.menu)
                if ch == '2':
                    print("Data entry successfully please chack Menu.txt")
        else:
            print("SORRY YOU TYPED IN AN INCORRECT PASSWORD. PLEASE TRY AGAIN LATTER. THANKS.")
                
                
        
    def view_list(self):
        with open('Menu.json') as f:
            data = f.read()
        for i in data:
            print(i,end = "")
        print("")
        
    def remove_food(self):
        id = input("Enter the Food ID to be removed : ")
        obj = js.loads(open('Menu.json'))
        
        for i in obj['Food ID'][:]:
            if (i['Food ID'] == id):
                obj['Food ID'].remove(i)



obj = admin(1,'a',1,1,1,1)
obj.add_food()
#obj.view_list()
#obj.remove_food()