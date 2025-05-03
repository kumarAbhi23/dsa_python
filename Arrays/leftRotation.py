# left roatation : counter clock wise
# arr =[1,2,3,4,5]
# o/p left rotate by 1 place  [2,3,4,5,1]

# all elements after 1 (d) will be moves 1 place behind and first element will add at back (last)


# sol : first copy first elements and rest of element move behind

def leftRotatae(arr):

    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp

arr =[1,2,3,4,5]
leftRotatae(arr)
print(arr)


