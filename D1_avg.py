# Calculate the Average of Numbers in a Given List

# Get the number of elements in the list from the user
# and store that number to the variable n
n=int(input("Plesse let me know total numbers in the list: "))
# Create an empty list to store the user input
lst = []
# carete a for loop for the list of inputs from the user
for i in range (0, n) :
    # get the inputs from user and store it to a variable a
    a=int(input("Enter element: "))
    # keep append the list for every input
    lst.append(a)
# once the for loop is completed, indend out and print the list
print (lst)
# find the total, sum() is the python standard function.
total=sum(lst)
# find the average.
average=total/n
# print the average
print (average)
