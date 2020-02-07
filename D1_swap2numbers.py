# Exchange the Values of Two Numbers Without Using a Temporary Variable

# Method1
num1=int(input("please enter first number : "))
print("num1 now : ",num1)
num2=int(input("please enter second number : "))
print("num2 now : ",num2)
num1, num2 = num2, num1
print("num1 now : ",num1)
print("num2 now : ",num2)


# Method2
print ("++++++++++++++++++++++++++++++++++++++")
a=int(input("please enter first number : "))
print("num1 now : ",a)
b=int(input("please enter second number : "))
print("num2 now : ",b)

a=a+b
b=a-b
a=a-b

print("num1 now : ",a)
print("num2 now : ",b)
