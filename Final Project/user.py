import json as js

class User:
    def __init__(self,Full_Name,Phone_Number,Email,Address,Password):
        self.Full_Name = Full_Name
        self.Phone_Number = Phone_Number
        self.Email = Email
        self.Address = Address
        self.Password = Password
        self.User_Details = {}
        
    def Sign_Up(self):
        
        self.Full_Name = input("Enter your Full Name : ")
        self.Phone_Number = input("Enter your Phone Number : ")
        self.Email = input("Enter your Email Address : ")
        self.Address = input("Enter your complete Address : ")
        self.Password = input("Please create a Password : ")
        self.User_Details = [{"Full Name":self.Full_Name,"Phone Number":self.Phone_Number,"Email":self.Email,"Address":self.Address,"Password":self.Password}]
        
        print(self.User_Details)
        
        with open("user.json",'a') as f:
            js.dump(self.User_Details,f)
            
    def login(self):
        Email = input("Enter your login Email Address : ")
        Password = input("Enter your Login Password : ")
        with open("user.json") as f:
            data =js.load(f)
        for i in data["Email","Password"]:
            if (i["Email" == Email and "Password" == Password]):
               # self.Email == Email and self.Password == Password
                print("Login Successsfull")
            else:
                print("Invalid Login Credentials")
        
        
        
obj1 = User(1,1,1,1,1)
#obj1.Sign_Up()
obj1.login()