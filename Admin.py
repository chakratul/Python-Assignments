import json as js
import datetime
import os.path

class admin:
    
    def __init__(self,food_id,food_name,food_price,food_quantity,food_discount,x,menu,food_stock,dt):
        self.food_id = food_id
        self.food_name = food_name
        self.food_price = food_price
        self.food_quantity = food_quantity
        self.food_discount = food_discount
        self.food_stock = food_stock
        self.dt = dt
        self.x = x
        self.menu = menu
        self.menu = {}
    
    def add_food(self):
        self.x = '100'
        y = int(self.x)
        if os.path.isfile('Menu.json'):
            f = open("Menu.json",'r')
            data = js.load(f)
            for (k,v) in data.items():
                if str(k) == str(self.x):
                    print(k)
                (y)+=1
            print(y)
                    
        else:
            print(self.x)
    
        n = input("Please Type in your Full Name :  ") 
        p = input("Please Enter the Admin Password to access the data base : ") 
        if p =="12345":
           print("LOGIN SUCCESSFULLY")
           print(f"""
                 >>>>>>>>>> ********** ---------- Welcome {n} ------------ ********** <<<<<<<<<<
                 
                 >>>>>>>>>> ********** ---------- To A and C Cafe Restaurant ******** <<<<<<<<<< 
                 """)
           ch = '0'
           #x = 100
           while ch != '2':
               print("""
                      *********Choose Below Option to Continue*************** 
                        Option 1 to Add Food 
                        Option 2 to Exit
                      *******************************************************
                      """)
               ch = input("Please enter the option from above : ")
               if ch == '1':
                   self.food_id = y
                   while self.food_id < 100000:
                       if self.food_id == y:
                           print(y)
                           y += 1
                       break
                   self.Name = input("Enter Food Name : ")
                   self.Quantity = input("Enter Food Quantity : ")
                   self.Price = int(input("Enter Food Price : "))
                   self.Discount = int(input("Enter Discount for the Food : "))
                   self.Stock = int(input("Enter Stock of Food : "))
                   self.dt = datetime.date.today()
                   self.menu[self.food_id] = [self.Name,self.Quantity,self.Price,self.Discount,self.Stock,str(self.dt)]           
                    
                   f = open("Menu.json",'w')
                   js.dump(self.menu,f)
                   print(self.menu)
                   f.close()  
                            
                    
               if ch == '2':
                   print("Data entry successfully")
        else:
           print("SORRY YOU TYPED IN AN INCORRECT PASSWORD. PLEASE TRY AGAIN LATTER. THANKS.")
           
           
    
    
    
    
    
    
    
    def edit_food(self):
        id = input("Enter the Food ID to be Updated : ")
        f = open('Menu.json')
        data = js.load(f)
        f.close()
        
        for (k,v) in data.items():
            #for v in k:
                if str(k) == id:
                    (v)[0] = input("Please Enter Updated Food Name : ")
                    (v)[1] = input("Please Enter updated Quatity : ")
                    (v)[2] = int(input("Please Enter updated Price : "))
                    (v)[3] = int(input("Please Enter updated Discount : "))
                    (v)[4] = int(input("Please Ente updated Stock : "))
                    (v)[5] = str(datetime.date.today())
                
                with open("Menu.json",'w') as f:
                    js.dump(data,f)
                print(f"Update Successfull")
                
                
            
    
    
    
    
    
    
    
    
    def view_food(self):
        f = open("Menu.json",'r')
        data = js.load(f)
        f.close()
        
        for (k,v) in data.items():
            print("Food ID: " + k)
            print(str(v))
        
        
    
    
    
    
    
    
    
    def remove_food(self):
        id = input("Enter the Food ID to be removed : ")
        f = open('Menu.json')
        data = js.load(f)
        f.close()
        
        for k in list(data):
            if str(k) == id:
                del data[k]


                with open("Menu.json",'w') as f:
                    js.dump(data,f)
                print(f"Food ID {id} has now been deleted from Menu. Thanks.")
            elif str(k) != id:
                print("Food ID not found. Please try a different Food ID. Thanks.")
                
    
    
obj = admin(1,1,1,1,1,1,1,1,1)
obj.add_food()
#obj.edit_food()
#obj.view_food()
#obj.remove_food()