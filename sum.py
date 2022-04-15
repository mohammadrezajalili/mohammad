import time
num1=float(input( " please enter number"))
num2=float(input( " please enter number"))
num3=float(input( " please enter number"))
if num1>0 and num2>0 and num3>0:
    print("sum",num1+num2+num3)
else:
    print("the condition of exit is entering  negetive number please enter numbers greater or equal than zero ")
    breakpoint()
time.sleep(1000)

