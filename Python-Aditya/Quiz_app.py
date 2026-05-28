score = 0

print("welcome to the quize game ")
print("--------------------------")

name = input("inter your name:    ")
print("weclome to the quize game  ",name)

# quize qui 1 
ans  = input("\n what is capital of japan :  ")

while True:
    if ans.lower() == "tokyo":
        print("correct :")
        print("\n you are brillent  ",name)
        score += 1
        break

    else:
        print("wrong")
        print("abhyas kara  ",name)
        break

# quize qui 2

ans = input("\nwhat is national animal of india:   ")

while True:
    if ans.lower() == "tiger":
        print("correct :")
        print("\n you are too brillent ",name)
        score += 1
        break

    else:
        print("wrong")
        print("abhyas kara vo ",name)
        break

# quize qui 3 

ans = input("what is the year of india independence:  ")

while True:
    if ans == "1947":
        print("correct :")
        print("\n you are too brillent  ",name)
        score += 1
        break

    else:
        print("wrong")
        print("abhyas kara vo ",name)
        break


print("your score is: ",score)

while True:
    if score == 3:
        print("\n you are too much brillent ", name)
        print("\n keep it up")
        break

    else:
        print("\n ks honar tumch ",name)
        break

print("\n thank you for vising us " ,name)
print("--------------------------")
