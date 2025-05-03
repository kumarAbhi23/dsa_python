# given sorted array and we need to remove duplicate element from it 

# ls=[1,10,10,30,34,34,45]

# we need to return size of array which will contains distinct size only 

# naive sol: take temp array travsese original array and keep adding to temp and before adding check that elemet 
# is in temp_array or not 

# time -o(n) space o(n)

def removeDuplicate(arr,n):
    
     #create temp array 
     tem_arry=[]
     tem_arry.append(arr[0])
     

     size=1
     for i in range(1,n):
          if arr[i-1]!=arr[i]:
               tem_arry.append(arr[i])
               

     print(tem_arry)  

            
          
# lets see if we can avoid extra space -in place 

def removeDulicateEff(arr,n):
     size_ptr=1
     for i in range(1,n):
          if arr[i]!=arr[i-1]:
               arr[size_ptr]=arr[i]
               size_ptr+=1

     return size_ptr          

arr=[1,1,10,10,30,34,34,45] 
size=removeDulicateEff(arr,len(arr))
for i in range(0,size):
     print(arr[i]) 