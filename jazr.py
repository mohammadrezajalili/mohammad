import math
import time
num=int(input("please enter number"))
if num>0:
    num=math.sqrt(num)
    print(num)
else:
    print("please enter positive number")
time.sleep(1000)