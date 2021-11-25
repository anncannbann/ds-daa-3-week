# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies 
# a2 + b2 = c2.


#inp = rr[] = {3, 1, 4, 6, 5} 
#out = (3,4,5)


def triplet(arr):
    n =len(arr)
    for i in range(n):
       arr[i] = arr[i]**2
    
    arr.sort()

    x = arr[len(arr)-1]
    
    for i in range(n-1,1,-1):
        j =0
        k=i-1
        
    
    return False


arr = [3, 1, 4, 6, 5]
print(triplet(arr))


