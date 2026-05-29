
# parking management system

parking = ["empty"] * 5

print("welcome to the parking management system")
print("----------------------------------------")


name = input("enter your name   ")

car_number = input("enter your car number  ")


while True:
    
    print("\n 1 hour parking fee is $10")
    print(" 2 hours parking fee is $15")
    print(" 3 hours parking fee is $20")
    print(" 24 hours parking fee is $100")

    exit_time = input("how long can a car be parked in parking lot ")

    

    if exit_time == "1":

        print("\ncheaking parking status")
        print("we have 5 parking lots")

        for i in range (len(parking)):
            print(f"slot{i+1}: {parking[i]}")

        else:
         print("invalid choice")

    break



