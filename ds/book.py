#Program to number of bits that are set to 1 in an integer
x = int(input("Enter int"))
y = bin(x).split("0b")
# x = y.split("0b")
print(y[1])

c=0

#M1
'''
for i in range(len(x)):
    if(x[i]=='1'):
        c+=1
    else:
        continue
print("count",c)
'''

#M2
    