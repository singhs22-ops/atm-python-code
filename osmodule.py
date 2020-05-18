import os

print()
print(os.getcwd())

os.chdir("C:\\Users\\himii\PycharmProjects\\untitled\\.idea")

print()
print(os.getcwd())

print("check if dir exists: ",os.path.exists("C:\\Users\\himii\\PycharmProjects\\pythonmodules\\osmodule.py"))


list =[1,2,3,4,5,6]
for i in list:
    print(i, ":,", end="")

arr = ['string','chararcter',1,3,'abc']

print()
for i in arr:
    print(i, "::", end="")