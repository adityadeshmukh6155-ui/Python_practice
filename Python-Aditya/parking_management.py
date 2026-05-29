
# parking management system

parking = ["empty"] * 5

print("welcome to the parking management system")
print("----------------------------------------")


name = input("enter your name   ")

car_number = input("enter your car number  ")


while True:
    
    print("\n 1. view parking ")
    print(" 2. car parking ")
    print(" 3. remove car")
    print(" 4. availeble parking")
    print("5. exit ")

    exit_time = input("select one ")

    

    if exit_time == "1":

        print("\ncheaking parking status")
        print("we have 5 parking lots")

        for i in range (len(parking)):
            print(f"slot{i+1}: {parking[i]}")

        else:
         print("invalid choice")

    break

    if exit_time == 2:
       print("your car is parked suscessfully")
       print("fair priced is $100")

    
    elif exit_time == 3:
     print("your car removed succesfully")
     print("you have to pay $100")

    elif exit_time == 4:
       print("cheaking availebility of parking")

       for i in rnage (len(parking)):
          print("fslot{i+1}:{parking[i]}")
          break
       
    elif exit_time == 5:
       print("thank for visiting us")

    else:
       print("error")
       break    
        




