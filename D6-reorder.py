# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# Example 1:
# Given 1->2->3->4, reorder it to 1->4->2->3.#


def reorder(mylist):
    n=len(mylist)
    mylist0 = [mylist[i] for i in range(0,n,2) ]
    mylist1 = [mylist[i] for i in range(n-2,0,-2) ]
    print(mylist0)
    print(mylist1)
    n1=len(mylist1)
    for i in range(n1):
        mylist0.insert(i+1, mylist1[i])
    print(mylist0)

if __name__=='__main__':
    # mylist = ['a', 'b', 'c', 'd', 'e']
    mylist = ['10', '11', '12', '13', '14']
    reorder(mylist)
