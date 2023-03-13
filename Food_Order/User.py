import json as js
import datetime as dt

class user:
    profile = {}
    def __init__(self,full_name,phone_number,address,email,password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.password = password
        

                
    
    
    
    
    
    def sign_up(self):
        self.full_name = input("Please Enter your first name : ")
        print(f"""
              <-><-><-><-><-> ********** Welcome to A and C Cafe Restaurant ********** <-><-><-><-><->
              ----------------------------------------------------------------------------------------
            
              ********** Hello {self.full_name} Please complete creating your profile below **********
              ________________________________________________________________________________________
              ----------------------------------------------------------------------------------------
              <-><-><-><-><-><-><-><-> ************************************** <-><-><-><-><-><-><-><->
               
              """)        
        self.phone_number = input("Enter your Phone Number : ")
        self.address = input("Enter your complete Address : ")
        self.email = input("Enter your Email Addres : ")
        self.password = input("Please create a log in password : ")
        self.profile[self.full_name] = [self.phone_number,self.address,self.email,self.password]
        print(self.profile)
        file_name = self.full_name +".json"
        f = open(file_name,'a')
        data = js.dump(self.profile,f)
        print(data)
        print("Your profile is now created")
        f.close()
            
    
    
    
    
    
    
    def log_in(self):
        self.full_name = input("Please Enter your first name : ")
        file_name = self.full_name + ".json"
        password = input("Enter your password : ")
        with open(file_name) as f:
            data = js.load(f)
        
        for (k,v) in data.items():
            if str(k) == self.full_name and (v)[3] == password:
                print("login Successfull")
                print(f"""
              <-><-><-><-><-> ********** Welcome to A and C Cafe Restaurant ********** <-><-><-><-><->
              ----------------------------------------------------------------------------------------
            
              Hello {k} You have now successfully Logged Into our system 
              
              ________________________________________________________________________________________
              ----------------------------------------------------------------------------------------
              <-><-><-><-><-><-><-><-> ************************************** <-><-><-><-><-><-><-><->
               
              """)
                #print("key: " + k)
                #print("value: "+ str(v))
            else:
               print("Invalid Credentials")
       
   
    
    
    

    
    def new_order(self):
        name = input("Enter your first name : ")
        self.file_name = name + "_order_history.json"
        cart = []
        self.total = []
        self.foodid = []
        with open('Menu.json', 'r') as f:
            data = js.load(f)
            for (k,v) in data.items():
                self.foodid.append(k)
                print("Food ID: " + k)
                print((v)[0],(v)[1],(v)[2])

        with open('Menu.json', 'r') as f:
            data = js.load(f)
        user = list(map(int,input("Enter Food ID to be added to the cart : ").split()))
        for i in user:
            for (k,v) in data.items():
                p = ((v)[0],(v)[1],(v)[2])
                if str(k) == str(i):
                    cart.append(p)
        print(cart)
        
        for j in cart:
            self.total.append((j)[2])
        print(self.total)
        sum = 0
        for k in self.total:
            sum+=k
        print("Total price of item is : ", sum)
        
        history =[]
        for (k,v) in data.items():
            for j in self.foodid:
                if j == k:
                    p = ((v)[0],(v)[1],(v)[2])
                    history.append(p)
        
        
        with open(self.file_name,'a') as f:
            js.dump(history,f)
            
            
    
    
    
    
    
    
    def order_history(self):
        name = input("Enter your firstname : ")
        password = input("Enter your password : ")
        file_name2 = name + ".json"
        file_name = name + "_order_history.json"
        with open(file_name2) as f:
            data = js.load(f)
        
        for (k,v) in data.items():
            if str(k) == name and str((v)[3]) == password:
                with open(file_name,'r') as f:
                    data = js.load(f)
                    print("Your Order History is")
                    print(data, end = " ")
            else:
                print("Invalid Credentials")
        
    
    



            
    def update_profile(self):
        self.full_name = input("Please Enter your first name : ")
        password = input("Please Enter your Password : ")
        file_name = self.full_name + ".json"
        f = open(file_name)
        data = js.load(f)
        f.close()
        
        for (k,v) in data.items():
                if str(k) == self.full_name and (v)[3] == password:
                    (v)[0] = input("Please Enter Updated Phone Number : ")
                    (v)[1] = input("Please Enter updated Address : ")
                    (v)[2] = input("Please Enter updated Email Address : ")
                    (v)[3] = input("Please Enter updated Password : ")
                    with open(file_name,'w') as f:
                        js.dump(data,f)
                    print(f"Update Successfull")
                else:
                    print("Incorrect details provided. Please try again")
                    

