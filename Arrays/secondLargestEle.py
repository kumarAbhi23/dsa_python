# given an array and we need to find second largest element in array

def secondLagest(lst):
    # approch will be first find first then second
    lar=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>lar:
            lar=lst[i]

    # by the end of this array we will get our first largest array

    # now find second largest element
    res=0
    for i in range(0,len(lst)):
        if lst[i]>res and res<lar and lst[i]<lar:
            res=lst[i]


    return  res

# another way will be we can keep only a loop and keep track of both largest and second largest element 








array=[1,20,34,53,46,77,81,98]
print(secondLagest(array))