File=open("demo.txt","r+")
print(File.tell())   #==>its tell position  its show 0
data=File.read()  #its read al;l data and in position last pointer
print(data)
print(File.tell())  #==>now file pointer at last that is 57