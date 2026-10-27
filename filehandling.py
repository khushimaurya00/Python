# Python File Handling

# File=open("text."text"."mode")

# r- read > read an existing file
# w- write > create a file or overwrite an existing file 
# a- apend > add data to the end  
# x-exclusice ceration > create a file  



# file=open("aipa.txt","w")
# file.write("Hello Students of AIPA")
# file.close()


# with open("aipa2.text","w") as file:
#     file.write("Hello Students of AIPA NSTI ALd")

# append "a" -add a new line to an existing as file:

# with open("aipa2".txt","a") as a file:
#      file.write("\n prayagraj , uttar Pradesh")
#      file.write("\nIndia")


# read -"r" read all the content of file    
# import time
# with open("aipa.txt","r") as file:
#     for line in file:
#         print(line.strip())
#         time.sleep(2)

# x=file.read()
# print(x)

# x=file.read(52)
# print(x)

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readline().strip())
# print(file.readline().strip())
# print(file.readline().strip())

# lines=file.readlines()

# print(lines)
# "x" - creates a new file if the file does not already exsits
# try:
#     with open("aipa.txt","x")as file:
#         file.write("X mode")

# except:
#     print("file already exists")

# import csv

# std=[
#     ["Shreya",27,"AIPA"],
#     ["Ajeet",27,"AIPA"],
#     ["Aditya",27,"AIPA"],
#     ["Khushi",27,"AIPA"],
#     ["Nirupma",27,"AIPA"]]
    
# with open("student.csv","w",newline="") as file:
#      writer=csv.writer(file)
#      writer.writerows(std)

# with open ("student.csv","r")as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)  

# Handling Directories & files

# import os,shutil,pathlib

# print(os.getwd)()

# os.mkdir("21 Oct") #create a directory

# os.rmdir("21 Oct") # remove Directory

# print(os.listdir(".")) # list files and directories

# shutil.rmtree("21 0ct") #remove evrything in adirectory

# os.rename("aipa.txt","copa.next)") #rename a file

# shutil.move("a.txt","b.txt")

# os.mkdir("21 oct/22 Oct/aipa")

# with open ("aipa.txt","w") as file:
#     file.write("hello")


# from pathlib import Path
# filename=input ("enter the filename:")

# path=Path(filename)

# if path.exists():
#     print("file exists")
# else:
#     print("file does not exist")
