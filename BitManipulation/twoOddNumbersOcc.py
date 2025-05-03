# given an array where all number appears even times and except two number which appears odd time 
# o/p those numbers 

# l=[1,2,1,3,4,3,4,5]
# o/p:[2,5]
# 1:2 ,2:1,3:3,4:2,5:1


# naive approch will be same as we saw on oneOdd numbr -O(n^2)

def twoOddN(lst):
     size=len(lst)
     res=[]
   
     for i in range(0,size):
        count=0
        for j in range(0,size):
            if lst[i]==lst[j]:
                count+=1
        if count %2!=0:
            res.append(lst[i]) 
     return res        


# now if we use xor 
# arr=[5,6,10,6,10,6,3,3]
# if i perform xor opereration 
# 5^6^10^6^10^6^3^3=5^6 will remain after performing xor 
#    0000....101  ^ 0......000110 
# res of above xor will be  : ....101
#                             ....110
# res                      :      011 = 3 in decimal

# now we need to figure out how to get 5 ,6 form it 

# we need to find a value where only last set bit of original number is set and other bits will 0 

# ex: x=3: 00011
#  if k:   00001: we need to find this k some how which will give idea that number which are in res 
# thier bits at this postiion either 0 0r 1 based on that we can figure out 
# grp1: where last bit is 0 from our given array [5,10,6]  
# grp2:where last bit is 1                       [3]


# lets see how we can achoive k 
# x:3:     0000...11
# x-1:2:   000....01 (last set bit will be toggle and apart from this every thing remain same)
# ~(x-1):  1111...10 (every thing is toogle and last set bit remain as it is )
# x&(~(x-1)):000000...1(every thing will be zero and last set bit will be set )
# k =(x& (~(x-1))):


# now we will perform biwise and with each number :if result  is non zero then they have same bit 



def twoOddEff(lst):
     res=0
     for i in lst:
         res^=i
     #res will contain res and we need to get number from it 
     k=res &(~(res-1))
     r1=0
     r2=0
     for i in range(0,len(lst)):
        if (lst[i]&k!=0): #set bits are same 
            r1^=lst[i]
        else:
            r2^=lst[i]    
     
     print(r1,r2)



l=[1,2,1,3,4,3,4,5]
(twoOddEff(l))
