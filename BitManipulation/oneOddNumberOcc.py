# given an array in which a number occurs odd time (only 1 number ) expect that all occuring even times

# Input : arr = {1, 2, 3, 2, 3, 1, 3}
#       1:2 , 2:2, 3:3

# Output : 3


# Input : arr = {5, 7, 2, 7, 5, 2, 5}
# Output : 5


# naive approch will be taka a number and count it in array if ist count is odd then print it /return it

# it is taking simply O(n^2)


def oddOccur(lst):
    size=len(lst)
   
    for i in range(0,size):
        count=0
        for j in range(0,size):
            if lst[i]==lst[j]:
                count+=1
        if count %2!=0:
            print(lst[i])        
               
# we can more optimize it we can use xor 
#   [1,2,3,2,2,1,3]  
#    1^1=0
#    3^3=0
#    2^2=0
#    0^2=2   
# 
# it will take o(n)  

def oddOccurEff(num):
    res=0
    for i in num:
        res^=i

    return res

arr=[1,2,3,2,2,1,3]
print(oddOccurEff(arr))