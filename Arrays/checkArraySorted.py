#given an array we need to check that element in array is sorted or not 

# [8,12,15] yes
# [8,10,10,12] - yes 
# [100] -yes
#[100,20,200]- No 

# naive will two nested loop and comapre each elene -o(N^2)

# sorted means arr[curr]>arr[prev] this conditon should be satisfy - o(n)


def isSorted(arr):
    if len(arr)==1:
        return True
    
    prev=0
    curr=1
    while curr<len(arr) and prev<curr:
        if arr[curr]<arr[prev]:
            return False
        else:
            curr+=1
            prev+=1  
    return True          

arr=[8,7,90] 
print(isSorted(arr))