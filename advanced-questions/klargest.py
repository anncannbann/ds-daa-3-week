#k largest(or smallest) elements in an array | added Min Heap method
#For example, if the given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30, and 23.



arr =[1, 23, 12, 9, 30, 2, 50]
k =3


#bad n*log(n)
arr.sort(reverse = True)
print(arr)
for i in range(k):
    print(arr[i], end=" ")
