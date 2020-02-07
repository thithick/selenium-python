# Reverse a Given Number
# /division
# //floor division
# %modulo

# get the integer input from the user. the number that you want to reverse
n=int(input("please enter integer :  "))
# initializing a variable with value 0
rev=0
# since we do not know the number of digits in the given number we are using while loop
while(n>0):
    # % is modulos operator which is used to get the reminder
    reminder=n%10
    # since we are using 10 as a devider and to keep all the reversing number in decimal place we multiply by 10,
    # so the remider will be multiplied for each iteration.
    rev=rev*10+reminder
    # the next step it to get the n-1 th position
    # // is a floor division operator
    # Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
    n=n//10
print("Reverse of the number:",rev)

print ("+++++++++++++++++++++++++++++++.\n")
