"""Output:
1 found in correct position.
2 found in correct position.
3 found in correct position.
4 not in list
5 found in correct position.
6 found in correct position.
7 found in correct position.
8 found in correct position.
9 found in correct position.
10 not in list
program terminated
"""
def binary_search_recursive(L,left,right,x):
    if left>right:
        return -1
    mid=(left+right)//2
    if L[mid]==x:
        return mid
    if L[mid]<x:
        return binary_search_recursive(L,mid+1,right,x)
    else:
        return binary_search_recursive(L,left,mid-1,x)


if __name__=="__main__":
    L=[1,2,3,5,6,7,8,9]
    left=0
    right=len(L)-1
    for x in range(1,11):
        position=binary_search_recursive(L,left,right,x)

        if position==-1:
            if x in L:
                print(x,"is in L, but function returned -1")
            else:
                print(x,"not in list")
        else:
            if L[position]==x:
               print(x,"found in correct position.")
            else:
               print("binary search returned ",position,"for ",x,"which is not correct")

    print("program terminated")