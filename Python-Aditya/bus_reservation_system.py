# bus reservation system 

latur = 400
pune  = 600
mumbai = 1000

count = 0


print("welcome the gade travels latur ")


    

print("our bus goes nanded to this city \n latur \n pune  \n mumbai")

name = input("inter your name  ")

name_city = input("inter your where do you want to go  ")

if name_city.lower() == "latur":
    print("your nand to latur seat is booked  ")
    print("your fair is price nanded to latur is : ",latur)

elif name_city.lower() == "pune":
    print("your nanded to pune seat is booked  ")
    print("your fair is price nanded to latur is : ",pune)

elif name_city.lower() == "mumbai":
    print("your nanded to mumabi seat is booked  ")
    print("your fair is price nanded to mumbai is : ",mumbai)

else:
    print("our bus does not go to that city")
    print("sorry for that")
