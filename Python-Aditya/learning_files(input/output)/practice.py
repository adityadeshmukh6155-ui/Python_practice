word = "learning"
with open("Python-Aditya/learning_files(input/output)/practice.txt","r") as f:
     data =  f.read()
     if(data.find(word)):
      print(len(word))