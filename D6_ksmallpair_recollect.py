def ksmallpair(lst1,lst2,k):
    n1=len(lst1)
    n2=len(lst2)
    if(k>n1*n2):
        k=n1*n2
    if(n1*n2==0):
        print("one of the list is empty")
        return
    if(k>n1):
        k=n1
    finalist=[]
    # minimum=lst1[n1-1]+lst2[n2-1]
    # print(minimum)
    # for x in range (k,0,-1):
        # minimum=lst1[n1-1]+lst2[n2-1]
    for i in range (0,k,1):
        minimum=lst1[n1-1]+lst2[n2-1]
            # print(minimum)
        for j in range(0,n2,1):
            if(lst1[i]+lst2[j]<minimum):
                lst=[]
                lst.append(lst1[i])
                lst.append(lst2[j])
                minimum=lst1[i]+lst2[j]
        minimum=lst1[i]+lst2[j]
        finalist.append(lst)
    print(finalist)


if __name__=='__main__':
    lst1=[1,2,3,4,5]
    lst2=[1,2,3,4,5]
    k=7
    ksmallpair(lst1,lst2,k)
