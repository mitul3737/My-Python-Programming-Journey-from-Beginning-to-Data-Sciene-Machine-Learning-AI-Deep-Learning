"""Linear Search Algorithm"""
def linear_search(L,x):
    n=len(L)
    i=0

    while i<n:
        if L[i]==x:
            return i
        i+=1

    i=-1

    return i
x=int(input("Give the value to search from the list [1,3,34,46,57,2,67,35,5]:\n"))
print("We have found ",x," on index: ",linear_search([1,3,34,46,57,2,67,35,5],x)+1)