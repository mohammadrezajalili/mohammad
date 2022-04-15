import array
import time
num1=input("please enter  student number")
num2=input("please enter  student number")
num3=input("please enter  student number")
num=[num1,num2,num3]
nume=[int(i)for i in num]
def loop():
    for i in nume:
        if i >=17:
           print("momtaz")
        elif i >=10 <17:
           print("ghabol")
        else:print("mardod")
input("")
