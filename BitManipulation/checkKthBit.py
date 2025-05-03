# we need to check in given number if kth bit set (1) or not 

# n=5   000....00101 k=1  
# yes last bit is set 


# thinsg which we need to know 

# to check last bit set or not 
  #### (n&1)!=0 then bit is set  


# naive apporch will be run a loop and create a mask where kth bit is set and do bit wise and with number 

# in mask all bits will be zero except kth bit 


def isSet(num,k):
    # create a variable for mask 
    x=1
    for i in range(0,k-1):
        x=x*2
    
    # now we will check with num 
    if (num&x)!=0:
        return True
    else:
        return False    




#time complexity ->O(K) 

# is there is another by which we reduce time for mask creation ?

# we know 1<<k is == 1*2^k
# we need to create mask is 1<<k-1 
# WE can also use right with number 
# mask=num>>(k-1) 

def setBitEff(num,k):
    # mask creation
    mask=1<<k-1
    if(num & mask)!=0:
        return True
    else:
        return False

#print(isSet(5,2))
print(setBitEff(5,3))
