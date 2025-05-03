# left rotate by d places 

# keep one thing in mind 
# d=size%d
# if size =5 and d=5 5%5=0 means no roatation as it same 

# first reverse_arr (arr,0,d-1)
# second  revser_arr(arr,d,n-1)
# thirs revse_arr(arr,0,n-1)   whole array revsere

def reverseArray(arr,start,end):
     while(start<end):
          temp=arr[start]
          arr[start]=arr[end]
          arr[end]=temp
          start+=1
          end-=1

def rotateByDplaces(arr,d):
     n=len(arr)

     reverseArray(arr,0,d-1)  # revser from start to d-1
     reverseArray(arr,d,n-1)
     reverseArray(arr,0,n-1)

arr =[1,2,3,4,5]
rotateByDplaces(arr,3)
print(arr)  


# time:theta (n)

