with open("Python-Aditya/learning_files(input/output)/practice.txt","r") as f:
     data =  f.read()

new_data = data.replace("java","python")
print(new_data)

with open("Python-Aditya/learning_files(input/output)/practice.txt","w") as f:
     f.write(new_data)