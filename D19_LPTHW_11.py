# D19_LPTHW_11.py

#end = "" is to print on the same line. so it will not go to the next line
print ("what is your name", end=" ")
name = input()
print ("what is your height", end = "       ")
height = input()
print ("what is your weight", end = " ")
weight = input()

# when you put 'f' on the print function before the "" it will consider the variable . otherwise it will treat those as strings
print (f" my name is {name} and my height is {height} and my weight is {weight} ")
