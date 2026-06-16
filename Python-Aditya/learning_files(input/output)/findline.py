word = "5hi"
data = True
line_no = 1 
with open("Python-Aditya/learning_files(input/output)/practice.txt","r")as f:
 while data: 
  data = f.readline()
  if(word in data):
   print(line_no)
   return

  line_no += 1
  