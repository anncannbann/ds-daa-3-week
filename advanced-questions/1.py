#Find the element that appears once in a sorted array

# Input:   arr[] = {1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8}
# Output:  4

# Input:   arr[] = {1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8}
# Output:  8



def search(arr, n) :
 
    XOR = 0
    for i in range(n) :
        XOR = XOR ^ arr[i]
 
    print("The required element is", XOR)
 
# Driver code
arr = [ 1, 1, 2, 4, 4, 5, 5, 6, 6 ]
Len = len(arr)
 
search(arr, Len)