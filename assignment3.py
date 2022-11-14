list=(10,21,4,45,66,93,1,64)

even=0
odd=0

for i in list:
    if  i%2  == 0 :
        even = even+1

    else:
        odd = odd+1

print('even no. in lst',even)
print('odd no. in lst',odd)