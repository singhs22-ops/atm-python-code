import os
import sys
import getpass
from tkinter import *
from PIL import Image
from datetime import date
import time
import socket

img = Image.open('picture.jpg')
#img.show()
today = date.today()
print("Today's date:", today)
#os.system('date')

amount = 0
add_money =0
balance=1000

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to Socket server ")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print("There was an error connecting to the server")
    sys.exit()

# connecting to the server
sock.connect((host_ip, port))

print("the server has successfully connected ")

def welcome():
    print("Welcome to State Bank of India")
    #menu to enter pin and match pin
    #we are assuming that the details are preentered
    #hardware code to acheive atm data from customers atm,Let assume since hardware is not
    #present a pseudo code is already written
    #we assume the pin is retrieved from hardware
    print("Please wait for few seconds.Retreiving your details")
    time.sleep(5)
    pin ="12349"
    count = 0 #max=4
    while count<3:
        enteredpin = input("Insert your 5 digit pin .")
        if (enteredpin == pin):
            break
        else:
            count +=1
            print('You have entered incorrect password {} times'.format(count))

            if (count ==3):
                print("You have exceeded the maximum limit")
                print("*****************************")
                sys.exit(0)


top = Tk()
top.title("Welcome to an automated atm Machine")
top.geometry("400x50")
top.colormapwindows(3)

def CashWith():
    welcome()
    print("Please wait and enter the cash amount to be withdrawn")
    amount1 = int(input())
    print('Amount to be withdrawn is {}'.format(amount1))
    global balance
    if(amount1 > balance):
        print("cash cannot be withdrawn.since amount is above cash limit of your account")
        sys.exit(0)
    print("Calling a function to dispatch cash")
    time.sleep(5)
    print("************Please Wait and collect cash************")
    balance = balance-amount1
    return

def BalanceWith():
    welcome()
    global balance
    print('The balance remaining in your account is {}'.format(balance))
    return


def Depositmoney():
    welcome()
    input1= int(input("Enter the amount to be deposited"))
    global balance
    balance=input1+balance
    print('Money successfully deposited, Enter 1 to check balance')

    x = int(input("Enter 1 or 0"))
    if x==1:
        print('Your updated balance is {}'.format(balance))
    sys.exit(0)

def exit_func():
    print("You have declined the request. Thankyou for banking with us")
    sys.exit(-1)

b1 = Button(top, text="Cash Withdrawal", command=CashWith, activeforeground="red", background="pink", pady=20, fg ="white")
b2 = Button(top, text="Balance", command=BalanceWith, activeforeground="blue", background="green", pady= 30)
b3 = Button(top, text="Deposit", command=Depositmoney, activeforeground="green", background="blue", pady=30)
b4 = Button(top, text="EXIT", command= exit_func, activeforeground="yellow", activebackground="yellow", pady=40)

b1.pack(side=LEFT,expand= False,fill = BOTH )
b2.pack(side=RIGHT, expand= False,fill = BOTH)
b3.pack(side=LEFT, expand= False,fill = BOTH)
b4.pack(side = TOP, expand = True, fill = BOTH)

top.mainloop()

if __name__ == "__main__":
    main_menu()