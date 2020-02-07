# Remove the Duplicate Items from a List

# declare an empty list variable to get the list emements from the user
lst = []
# get the number of elements count from user
n = int(input("number of elements in this list: "))
# traverse the for loop for each iteration to get input from the user
for i in range (n):
    # get the input from user
    a=int(input(" enter list element : "))
    # append it to the empty lists
    lst.append(a)
# print the list
print (lst)
# set() is the pyhton standard function which will store the distinct elements in ascemding order
# b=set(lst) - if we use this way the requested program is already over
# but we are going to use empty set and math logic
b=set()
# just to show the set element 'b' is empty
print (b)
# declaring another empty list variable to store the unique numbers
unique = []
# run the for loop for the list we created
for x in lst:
    # we have not in function in python to check if the element is present in the list
    if x not in b:
        # append to the new empty list 'unique'
        unique.append(x)
        # since b is an empty set, we just keep adding the element one by one from the list 'lst'
        b.add(x)
# once the for loop is over print the unique elements list
print("Non-duplicate items:")
print(unique)
