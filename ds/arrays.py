# import array as arr

# a = arr.array('i',[1,2,3,4,5,6,7,8,9,10])

# for i in range(0,10):
#     print(a[i],end=" ")

# print("\n2nd Elem:",a[2])

# a.insert(2,9)

# print("Insertion after",a)


# a.pop(2)
# print("Popped ,newArray:",a)

# print(a[:])

#REVERSE A STRING best = slicing
l='Hello my name is JOn'
c=''
if(type(l)!=str or len(l)<2):
    print('Not a string')
else:
    for x in l:
        c = x + c
    print(c)
    # print(l[::-1])