from Admin import admin
from User import user
import sys

class main:

    def execute(self,choice):
        if choice == 1:
            print("*******Add Food*******")
            obj.add_food()
        if choice == 2:
            print("*******View Food*******")
            obj.view_food()
        if choice == 3:
            print("*******Edit Food*******")
            obj.edit_food()
        if choice == 4:
            print("*******Remove Food*******")
            obj.remove_food()
        if choice == 0:
            print("Exit Successfull.")
            sys.exit()
    
    def execute1(self,choice1):
        if choice1 == 1:
            print("*******Sign Up*******")
            obj2.sign_up()
        if choice1 == 2:
            print("*******Log In*******")
            obj2.log_in()
            print('''
                  ******************* PLEASE CHOOSE FROM BELOW OPTION ******************** 
                  ------------------------------------------------------------------------- 
                  ********** --------------------> 3. New Order <-------------------- **********

                  ********** --------------------> 4. Order History  <-------------------- **********
                  
                  ********** --------------------> 5. Update Profile  <-------------------- **********
                  
                  ********** --------------------> 0. Exit  <-------------------- **********
          ''')
            choice1 = int(input(" Enter your option : "))
        if choice1 == 3:
            print("*******New Order*******")
            obj2.new_order()
        if choice1 == 4:
            print("*******Order History*******")
            obj2.order_history()
        if choice1 == 5:
            print("*******Update Profile*******")
            obj2.update_profile()
        if choice1 == 0:
            print("Exit Successfull.")
            sys.exit()
        
        
if __name__ == "__main__":
    
    obj1 = main()
    ch = 9

    while ch != 0:
        print("""
          ******************* PLEASE CHOOSE YOUR TYPE OF LOGIN ********************
          -------------------------------------------------------------------------
          ********** --------------------> 1. Admin <-------------------- **********
          
          ********** --------------------> 2. User  <-------------------- **********
          
          ********** --------------------> 0. Exit  <-------------------- **********
          """)
        
        ch = input("Please select your choice : ")
                 
        if ch == '1':
            obj = admin(1,1,1,1,1,1,1) 
            while True:
                choice = int(input("Enter \n1. Add Food \n2.View Food \n3.Edit Food \n4.Remove Food \n0.Exit : \n"))    
                obj1.execute(choice)
        if ch == '2':
            obj2 = user(1,1,1,1,1)
            while True:
                choice1 = int(input("\n1. Sign Up \n2.Log In \n0. Exit \n Enter Your Choice :  "))    
                obj1.execute1(choice1)
                while choice1 != 0:
                    print('''
                  ******************* PLEASE CHOOSE FROM BELOW OPTION ******************** 
                  ------------------------------------------------------------------------- 
                  ********** --------------------> 3. New Order <-------------------- **********

                  ********** --------------------> 4. Order History  <-------------------- **********
                  
                  ********** --------------------> 5. Update Profile  <-------------------- **********
                  
                  ********** --------------------> 0. Exit  <-------------------- **********
                    ''')
                    choice1 = int(input("Enter your option : "))
                    obj1.execute1(choice1)
                    #if choice1 == 3:
                     #   obj2.new_order()
                    #if choice1 == 4:
                     #   obj2.order_history()
                    #if choice1 == 5:
                     #   obj2.update_profile()
                            
            
        
                
                