# given a array and we need to reverse it 
# arr =[10,5,7,30]


# naive approch will be -
   # travser from right to left and add in a lst

# efficent way using two ptr
# 
#    
def reverseArray(arr):
    i=0
    j=len(arr)-1
    while i<=j:
        # we need to swap 
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1

arr =[10,5,7,30]
reverseArray(arr)
print(arr)