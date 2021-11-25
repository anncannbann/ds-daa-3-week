#inp: 5 1 4 2 8
#out: 1 2 4 5 8



def bubbleSort(arr):
    len_arr= len(arr)

    for i in range(len_arr):
        for j in range(0,len_arr-i-1):
            if(arr[j]> arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)





arr = [5, 1, 4, 2, 8]
bubbleSort(arr)