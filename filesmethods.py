import os
import shutil
#os.mkdir("c:\\suryapythonfiles")
#wrie
createfile=open("c:\\suryapythonfiles\suryafile.txt","w+")
print(createfile.write("this is suryateja ponnaganti"))
#append
createfile=open("c:\\suryapythonfiles\suryafile.txt","a+")
print(createfile.write(".Iam learning python"))
print(createfile.readline())
#read
createfile=open("c:\\suryapythonfiles\suryafile.txt","r+")
print(createfile.read())
print(createfile.write(". my collegoues are nani,vijji,shishva,kiran,chanukya,pavan,sai,sowjanya,durga"))
createfile.close()
#file1=open("c:\\suryapythonfiles\\tejafile.txt","x")
file1=open("c:\\suryapythonfiles\\tejafiles.txt","w")
print(file1.write("Iam working for clariont software solutions"))
file1=open("c:\\suryapythonfiles\\tejafiles.txt","r")
print(file1.readline())




