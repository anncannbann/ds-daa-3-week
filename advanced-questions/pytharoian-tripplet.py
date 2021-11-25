
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


# # Python program that returns true if there is
# # a Pythagorean Triplet in a given array.
 
# # Returns true if there is Pythagorean
# # triplet in ar[0..n-1]
# def isTriplet(ar, n):
#     # Square all the elements
#     for i in range(n):
#         ar[i] = ar[i] * ar[i]
 
#     # sort array elements
#     ar.sort()
 
#     # fix one element
#     # and find other two
#     # i goes from n - 1 to 2
#     for i in range(n-1, 1, -1):
#         # start two index variables from
#         # two corners of the array and
#         # move them toward each other
#         j = 0
#         k = i - 1
#         while (j < k):
#             # A triplet found
#             if (ar[j] + ar[k] == ar[i]):
#                 return True
#             else:
#                 if (ar[j] + ar[k] < ar[i]):
#                     j = j + 1
#                 else:
#                     k = k - 1
#     # If we reach here, then no triplet found
#     return False
