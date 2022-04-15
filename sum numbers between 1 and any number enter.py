import time
#num1=float(input(" please enter number"))
num1=1
num2=float(input(" please enter number : "))
if num1>num2:
    num=num1-num2+1
else:
    num=num2-num1+1
def sum1(num):
    sum=(num*(num1+num2))/2
    sum=sum-(num1+num2)
    return sum
print("sum between two numbers is ",sum1(num))
input('press anything to exit : ')


