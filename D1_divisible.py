# Print all Numbers in a Range Divisible by a Given Number

startingrng=int(input("Please enter starting range  : "))
endingrng=int(input("Please enter Ending range  : "))
divider=int(input("Please enter the divider :"))
for i in range(startingrng,endingrng):
    if(i%divider==0):
        print(i)
