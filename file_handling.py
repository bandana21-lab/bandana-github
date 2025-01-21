# file handling is the process of handling file(.txt,.csv,etc) using programming language
# file=open("sample.txt",'r')
# a=file.read()
# print(a)

# file.close() 

# name=input("Enter your name: ")
# age=(input("Enter your age: "))
# course=input("Enter your course: ")
# with open("info.txt",'w') as file:
#     a=file.writelines(
#         [f"{name}\n{age}\n{course}\n"]
#     )

# with open("animal.txt","w") as file:
#     a=file.read("dog")
#     print(a)

# with open("animal.txt","x") as file:
#     a=file.write("cat")
#     print(a)

# to open files in different location the syntax used is: 
# f=open("D:\\myfiles\welcome.txt",'r')
# print(f(read()))

# we can also specify how many characters of fike we want to send

# with open("sample.txt","r") as file:
#     a=file.read(5)
#     print(a)

# looping inside the characters of words inside the file 
# f=open("sample.txt","r")
# for x in f:
#     print(x)

# with open("sample.txt","a") as file:
#     a=file.write("\nNow the file has more content")

# with open("sample.txt","r") as file:
#     b=file.read()
#     print(b)

# with open("random.txt","w") as file:
    # b=file.write("It is going to trash bin")

# import os
# os.remove("random.txt") 