 # Take in the Marks of 5 Subjects and Display the Grade
def grade(avrg):
    if(mark>90):
        print("Grade A")
    elif(90>mark>80):
        print("Grade B")
    elif(80>mark>60):
        print("Grade C")
    else:
        print("Grade D")

n=int(input("Please enter number of subject  : "))
lst=[]
for i in range (0,n):
    mark=int(input("Please enter the mark : "))
    lst.append(mark)
total=sum(lst)
avrg=total/n
print(avrg)
grade(avrg)
