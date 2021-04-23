# program to check the input number
num=eval(input())
if type(num)==int:
    print("real number")
elif type(num)==float:
    print("float number")
elif type(num)==str:
    print("string")
elif type(num)==complex:
    print("complex number")
elif num==0:
    print("Zero")
