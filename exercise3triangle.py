
num1=float(input( " please enter number"))
num2=float(input( " please enter number"))
num3=float(input( " please enter number"))
def condition():
    if num1+num2>num3 and num3+num2>num1 and num3+num1>num2:
        print("yes included triangle ")
    else:
        print("not includeed")
print(condition())
input("")