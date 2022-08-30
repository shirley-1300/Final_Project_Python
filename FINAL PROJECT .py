#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import datetime

# Design a Food Ordering app for a restaurant

def user_registration(user_json,name,age,email,ph_no,password):
    user_details = {
        "id" :1,
        "name" : name,
        "age" : age,
        "email" : email,
        "ph_no" : ph_no,
        "password" : password,
        "order history" : {}
    }
    try:
        user_file = open(user_json,"r+")
        user_file2=json.load(user_file)
        for i in range(len(user_file2)):
            if user_file2[i]["email"] == email:
                user_file.close()
                return "This user is already Registered"
        else:
            user_details["id"] =len(user_file2)+1
            user_file2.append(user_details)
    except json.JSONDecodeError:
        user_file2 = []
        user_file2.append(user_details)
    user_file.seek(0)
    user_file.truncate()
    json.dump(user_file2,user_file,indent = 4)
    user_file.close()
    return "you have successfully registered ,Now you can order a delicious food"    

def order_history_of_user(user_json,user_id):
    user_file = open(user_json,"r+")
    user_file2=json.load(user_file)
    for i in range(len(user_file2)):
        if user_file2[i]["id"]==user_id:
            print("   Date  |  order item ")
            for i,j in user_file2[i]["order history"].items():
                print(f"{i} | {j}")
                user_file.close()
                return True
    user_file.close()
    return False

def placing_order(user_json,food_json, user_id,name_of_food,quantity =0): 
    date = datetime.datetime.today().strftime("%d/%m/%y")
    user_file = open(user_json,"r+")
    user_file2=json.load(user_file)
    food_file = open(food_json,"r+")
    food_file2=json.load(food_file)
    for i in range(len(food_file2)):
        if food_file2[i]["name"] == name_of_food:
            if food_file2[i]["no of orders"] == quantity:
                for i in range(len(user_file2)):
                    if user_file2[i]["id"]== user_id:
                        food_file2[i]["no of orders"] -= quantity
                        if date not in user_file2[j]["order history"]:
                            user_file2[i]["order history"][date] = [food_file2[i]["name"]]
                        else:
                            user_file2[i]["order history"][date].append(food_file2[i]["name"])
            else:
                print("Enter less quantity")
                break
        else:
            print("Food is not available!!!")
            break
    user_file.seek(0)
    user_file.truncate()
    json.dump(user_file2,user_file,indent = 4)
    user_file.close()
    
    food_file.seek(0)
    food_file.truncate()
    json.dump(food_file2,food_file,indent = 4)
    food_file.close()
def user_details_update(user_json,name,age,email,ph_no,password):
    user_file = open("user.json","r+")
    user_file2=json.load(user_file)
    for i in range(len(user_file2)):
        if user_file2[i]["id"]==int(input("Enter your user id : ")):
            while True:
                user_file2[i]["id"]==user_file2[i]["id"]
                user_file2[i]["name"]==input("Enter your name to change : ")
                user_file2[i]["age"]==input("Enter your age : ")          
                user_file2[i]["email"]==input("Enter your email to update : ")
                user_file2[i]["ph_no"]==input("Enter your phone number : ")
                if user_file2[i]["password"]==input("Enter old password : "):
                    user_file2[i]["password"]==input("Enter new password : ")
                    break

                else:
                     print("your old password is incorrect")
        else:
            print("invalid details")
    user_file.seek(0)
    user_file.truncate()
    json.dump(user_file2,user_file,indent=4)
    user_file.close()
    print()
    print("your profile is updated successfully")
    print("------------------------------------")
                                     
    
    
#CRUD(CREATE,READ,UPDATING,DELETE) OPERATIONS ON FOOD function

def adding_food_items(food_json,food_name,no_of_orders=1,):
    food_details = {
        "id"   : 1,
        "name" : food_name,
        "no of orders" : no_of_orders,
        "price"  : 0,
        "discount" : 0,
         
    }
    try:
        food_file  = open(food_json,"r+")
        food_file2 = json.load(food_file)
        for i in range(len(food_file2)):
            if food_file2[i]["name"] == food_name:
                food_file.close()
                return " Your ordered is already placed "
            food_details["id"] = (len(food_file2))+1
            food_file2.append(food_details)
    except json.JSONDecodeError:
        food_file2 = []
        food_file2.append(food_details)
    food_file.seek(0)
    food_file.truncate()
    json.dump(food_file2,food_file,indent = 4)
    food_file.close()
    return "your order  placed successfully"
      
      
def updating_food_items(food_json,food_id,no_of_orders=1,price=0,discount=0):
    food_file = open(food_json,"r+")
    food_file2 = json.load(food_file)
    for i in range(len(food_file2)):
        if (food_file2[i]["id"] == food_id):
            food_file2[i]["no of orders"]+= no_of_orders
            food_file2[i]["price"]  == len(food_file2) +price
            food_file2[i]["discount"] == len (food_file2) -discount_coupon       #this discount applicable for the first order
             #this discount applicable for the after first order
            break
    else:
        print("No changes have been made")
            
    food_file.seek(0)
    food_file.truncate()
    json.dump(food_file2,food_file,indent = 4)
    food_file.close()
    return "you updated the food items successfully"

def read_food_items(food_json):
    food_file = open(food_json,"r+")
    food_file2 = json.load(food_file)
    for i in range(len(food_file2)):
        print(f" Id : {food_file2[i]['id']}")
        print(f" name of food : {food_file2[i]['name']}")
        print(f" number of plates available : {food_file2[i]['no of orders']}")
        print(f" price : {food_file2[i]['price']}")
        print(f" discount coupon : {food_file2[i][ 'discount']}")
        print('------------------------------------------')
    else:
        print( "No more food items available")
        return "-----------------------"
    food_file.close()
read_food_items("food_items.json")

def removing_food_items(food_json,food_id):
    food_file = open(food_json,"r+")
    food_file2 = json.load(food_file)
    for i in range(len(food_file2)):
        if food_file2[i]["id"]==food_id:
            del food_file2[i]
            food_file.seek(0)
            food_file.truncate()
            json.dump(food_file2,food_file,indent =4)
            food_file.close()
            return "you successfully removed the food item"
    return "Enter valid id"


u1 = input("Enter 'yes' to open the FoodOrderingApp : ")
while u1.lower()== "yes" :
    print("     Home page      ")
    print("Press '1' to open Register ")
    print("Press '2' to open Login ")
    print("Press '3' to Exit ")
    print("--------------------------------")
    
    u2 = input("Enter your option to continue : ")
    
    #--------------------REGISTRATION METHOD------------------------#
    
    if u2 == "1":
            print()
            name     = input("Enter your name : ")
            age      = input("Enter your age : ")
            email    = input("Enter your email : ")
            ph_no    = input("Enter your phone number : ")
            password = input("Enter your password : ")
            print("-------------------------------")
            user_registration("user.json",name,age,email,ph_no,password) 
            
    #-----------------------LOGIN METHOD-----------------------------#
           
    elif u2 == "2":
            print()
            while True:
                print("Press '1' to open User login ")
                print("Press '2' to open Admin login  ")
                print("Press '3' to Exit ")
                print("-----------------------------------") 
                u3 = input("Enter your option to continue : ")
                print("-----------------------------------") 
                
                if u3 == "1":
                    
                    user = input("Enter your name : ")
                    password = input("Enter your Password : ")
                    user_file  = open("user.json", "r+")
                    user_file2 = json.load(user_file)
                    for i in range(len(user_file2)):
                        if user_file2[i]["name"]== user:
                            user_file2[i]["id"] == user_file2[i]["id"]
                            if user_file2[i]["password"]== password: 
                                
                                while True:
                                    print("-------------------------------")
                                    print("you have logged in successfully")
                                    print()
                                    print("Press '1' to view food menu")
                                    print("Press '2' to order the food")
                                    print("Press '3' to view order history ")
                                    print("Press '4' to update your profile")
                                    print("Press '5' to view food items in a list ")
                                    print("Press '6' to Exit ")
                                    print("-------------------------------")
                                    u4 = input("Enter your option to continue : ")
                                    
                                    if u4 == "1":
                                        read_food_items("food_items.json")
                                        
                                    elif u4 == "2":
                                        date = datetime.datetime.today().strftime("%d/%m/%y")
                                        user_file = open("user.json","r+")
                                        user_file2=json.load(user_file)
                                        food_file = open("food_items.json","r+")
                                        food_file2=json.load(food_file)
                                        for i in range(len(food_file2)):
                                            print(" Dear customer please observe and enter the food details to confirm your order ")
                                            if food_file2[i]["id"] == int(input("Enter the food id to order : ")): 
                                                food_file2[i]["name"]==(input("Enter the name of the food : "))
                                                print(food_file2[i])
                                                food_file2[i]["no of orders"] -= int(input(" Enter the quantity of food : "))
                                                print("-----------------------------------------------------------")
                                                print("Your order got placed and here are the order details")
                                                food_amount =food_file2[i]['price']-food_file2[i]['discount']
                                                final_amount=food_amount*(int(input('confirm the quantity of food : ')))
                                                if food_file2[i]['discount']<=food_file2[i]['discount']:
                                                    discount_amount=food_file2[i]['discount']*(int(input('confirm the quantity of food again to get discount :  ')))
                                                    print(f"your total amount to pay is {final_amount} and discount amount is {discount_amount}")
                                                    print(f" you saved {discount_amount} ")
                                                    print("------------------------------------------------------------------------------")
                                                    for j in range(len(user_file2)):
                                                        if user_file2[j]["id"] == int(input("Enter the user id : ")):
                                                            if date not in user_file2[j]["order history"]:
                                                                user_file2[j]["order history"][date]=[food_file2[i]["name"]]
                                                            else:
                                                                user_file2[j]["order history"].append(food_file2[i]["name"])
                                                                
                                                                
                                                            
                                                else:
                                                    print("Discount price is added more than given")
                                                    break
                                            




                                            else:
                                                print("--------------------------------------------------------------------------------")

                                        user_file.seek(0)
                                        user_file.truncate()
                                        json.dump(user_file2,user_file,indent = 4)
                                        user_file.close()

                                        food_file.seek(0)
                                        food_file.truncate()
                                        json.dump(food_file2,food_file,indent = 4)
                                        food_file.close()
                                        print("-------------------------------------------------------------------")
                                        
                                    elif u4 == "3":
                                        user_file = open("user.json","r+")
                                        user_file2=json.load(user_file)
                                        for i in range(len(user_file2)):
                                            user_file2[i]["id"]==int(input("Enter the user id to view order history : "))
                                            #user_file2[i]["name"]==input("Enter the your name : ")
                                            print("|  Date   |  order   |") 
                                         #   print(user_file2[i]["order history"])
                                          #  break
                                            for i,j in user_file2[i]["order history"].items() :
                                                print(f"|{i} | {j}|")
                                        else:
                                            user_file.close()
                                    elif u4== "4":
                                        user_file = open("user.json","r+")
                                        user_file2=json.load(user_file)
                                        for i in range(len(user_file2)):
                                            if user_file2[i]["id"]==int(input("Enter your user id to make updates : ")):
                                                while True:
                                                    print("Press '1' to update user name")
                                                    print("Press '2' to update age")
                                                    print("Press '3' to update email")
                                                    print("Press '4' to update phone number")
                                                    print("Press '5' to update password")
                                                    print("Press '6' to make changes overall profile")
                                                    
                                                    print("--------------------------------------")
                                                    A1 = input("Enter your option to continue : ")
                                                    print("--------------------------------------")
                                                    if A1 == "1":
                                                        user_file2[i]["name"]=user_file2[i]["name"].replace(input("Enter your old user name  : "),input("Enter your new user name  : "))
                                                        break
                                                    elif A1 == "2":
                                                        user_file2[i]["age"]=user_file2[i]["age"].replace(input("Enter your old age : "),input("Enter your current age : "))
                                                        break
                                                    elif A1 == "3" :
                                                        user_file2[i]["email"]=user_file2[i]["email"].replace(input("Enter your old email id : "),input("Enter your new email id : "))
                                                        break
                                                    elif A1 == "4":
                                                        user_file2[i]["ph_no"]=user_file2[i]["ph_no"].replace(input("Enter your old phone number"),input("Enter your new phone number : "))
                                                        break
                                                    elif A1 == "5":
                                                        user_file2[i]["password"]=user_file2[i]["password"].replace(input("Enter old password : "),input("Enter your new password : "))
                                                        break
                                                    elif A1 =="6":
                                                        user_file2[i]["name"]=user_file2[i]["name"].replace(input("Enter your old user name  : "),input("Enter your new user name  : "))
                                                        user_file2[i]["age"]=user_file2[i]["age"].replace(input("Enter your old age : "),input("Enter your current age : "))
                                                        user_file2[i]["email"]=user_file2[i]["email"].replace(input("Enter your old email id : "),input("Enter your new email id : "))
                                                        user_file2[i]["ph_no"]=user_file2[i]["ph_no"].replace(input("Enter your old phone number"),input("Enter your new phone number : "))
                                                        user_file2[i]["password"]=user_file2[i]["password"].replace(input("Enter old password : "),input("Enter your new password : "))
                                                        break
                                                        
                                                        
                                                    else:
                                                        print("invalid option selected")
                                                        break
                                                else:
                                                    print("invalid id")
                                                    

                                        else:
                                            print("------------------------------------------------------------------")
                                        user_file.seek(0)
                                        user_file.truncate()
                                        json.dump(user_file2,user_file,indent=4)
                                        user_file.close()
                                        print()
                                        print("your profile is updated successfully")
                                        print("------------------------------------")

                                    elif u4 == "5":
                                        user_file = open("user.json","r+")
                                        user_file2=json.load(user_file)
                                        food_file = open("food_items.json","r+")
                                        food_file2=json.load(food_file)
                                        for i in range(len(food_file2)):
                                            print()
                                            print(f"{[food_file2[i]['id']]}.{[food_file2[i]['name']]} 1 item : [INR {[food_file2[i]['price'] ]} ] ")
                                        
                                        food_file.seek(0)
                                        food_file.truncate()
                                        json.dump(food_file2,food_file,indent = 4)
                                        food_file.close()
                                
                                        
                                    else:
                              
                                        break
                        
                            
                            
                elif u3 =="2":
                    print("----------------------------------------")
                    user = input("Enter your admin user name : ")
                    password = input("Enter your password : ")
                    admin_file = open("Admin.json","r+")
                    admin_file2 = json.load(admin_file)
                    for i in range(len(admin_file2)):
                        if admin_file2[i]["user_name"] ==user:
                            if admin_file2[i]["password"] == password:
                                print()
                                while True: 
                                    print("---------------------------------------------")
                                    print(f"               Admin page                   ")
                                    print("---------------------------------------------")
                                    print("Press '1' to Add food items")
                                    print("Press '2' to View food items")
                                    print("Press '3' to Update the items")
                                    print("Press '4' to Remove food items")
                                    print("Press '5' to view the stock")
                                    print("press '6' to Exit")
                                    print("---------------------------------------------")
                                    u5= input("Enter your option to continue : ")
                                    if u5== "1":
                                        food_details = {
                                            "id"   : 1,
                                            "name" : input("Enter the food name to add : "),
                                            "no of orders" : int(input("Enter the number of food items to add : ")),
                                            "price"  : int(input("Enter the price of food to add : ")),
                                            "discount" :int(input("Enter the discount for the food item : ")),
                                            }
                                            
                                         
                                                                                    
                                        try:
                                            food_file  = open("food_items.json","r+")
                                            food_file2 = json.load(food_file)
                                            for i in range(len(food_file2)):
                                                
                                                if food_file2[i]["name"] == "name":
                                                    food_file.close()
                                                    print("Item added already")
                                            
                                            food_details["id"] = len(food_file2)+1
                                            food_file2.append(food_details)
                                        except json.JSONDecodeError:
                                            food_file2 = []
                                            food_file2.append(food_details)
                                        food_file.seek(0)
                                        food_file.truncate()
                                        json.dump(food_file2,food_file,indent = 4)
                                        adding_food_items("food_items.json","name","no of orders")
                                        food_file.close()
                                    
                                    elif u5=="2":
                                        print("-------------------------------------------")
                                        read_food_items("food_items.json")
                                        print("____________________________________________")
                                    elif u5 == "3":
                                        food_file = open("food_items.json","r+")
                                        food_file2 = json.load(food_file)
                                        for i in range(len(food_file2)):
                                            if food_file2[i]["id"]==int(input("Enter the food id : ")):
                                                food_file2[i]["no of orders"] >=1
                                                print("add the plates")
                                                print()
                                                print("Enter 0 if you don't want to update details ")
                                                food_file2[i]["no of orders"]+=int(input("enter the number of plates to update : "))
                                                food_file2[i]["price"]+=int(input("enter the price : "))
                                                food_file2[i]["discount"]+=int(input("enter the discount coupon in rupees : "))
                                                
                                                break
                                        food_file.seek(0)
                                        food_file.truncate()
                                        json.dump(food_file2,food_file,indent=4)
                                        food_file.close()
                                        print("your food item is updated successfully")
                                        

                                    elif u5 == "4":
                                        print()
                                        food_file = open("food_items.json","r+")
                                        food_file2 = json.load(food_file)
                                        for i in range(len(food_file2)):
                                            if food_file2[i]["id"]==int(input("Enter the food id : ")):
                                                    del food_file2[i] 
                                                    food_file.seek(0)
                                                    food_file.truncate()
                                                    json.dump(food_file2,food_file,indent = 4)
                                                    food_file.close()
                                                    removing_food_items("food_items.json","id")
                                                    print("food item removed successfully")
                                            

                                    elif u5=="5":
                                        user_file = open("user.json","r+")
                                        user_file2=json.load(user_file)
                                        food_file = open("food_items.json","r+")
                                        food_file2=json.load(food_file)
                                        for i in range(len(food_file2)):
                                            print("The stock available")
                                            print(f"Food items : {[food_file2[i]['name']]}  [ num of items available : {[food_file2[i]['no of orders'] ]} ]")
                                            
                                        food_file.seek(0)
                                        food_file.truncate()
                                        json.dump(food_file2,food_file,indent = 4)
                                        food_file.close()
                                            
                                            
                                            
                                    else:
                                        print("No changes have been made")
                                        
                                        break
                                        
                            else:
                                print("Enter valid password")
                                break
                        else:
                            print("Enter valid user name")
                            break
                            
                elif u3 == "3":
                    print("you entered invalid option")
                    break
    else:
        print("Please visit us again")
        break


# In[ ]:





# In[ ]:




