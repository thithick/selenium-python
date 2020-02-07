# Read a number n and Compute n+nn+nnn
y=0
n=int(input("enter a integer"))
for i in range (0,n):
    x=i*n
    print("x:",x)
    y=y+x
    print("y",y)
print(y)



# 1. Take the value of a element and store in a variable n.
# 2. Convert the integer into string and store it in another variable.
# 3. Add the string twice so the string gets concatenated and store it in another variable.
# 4. Then add the string thrice and assign the value to the third variable.
# 5. Convert the strings in the second and third variables into integers.
# 6. Add the values in all the integers.
# 7. Print the total value of the expression.
# 8. Exit.


n1=int(input("enter a integer"))
temp=str(n1)
t1=temp+temp
t2=t1+temp
comp=temp+t1+t2
print (comp)
comp1=n+int(t1)+int(t2)
print(comp1)
