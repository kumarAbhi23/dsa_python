# we need to count number set bits in a number  

# naive approch 
  # o(n)

def countSetBit(num):
    count=0
    # print(count+"intial")    
    while num!=0:
        # check for last bit 
        if (num & 1)!=0:
            count+=1
        # now reduce number 
        num=num//2          
    return count

#Another efficent apporch if we could reduce time in loop 

# Berian kergingam algo
# make last set bit zero 
# n=40 -101000  --fiest set is at 4th postion
# n=39 -100111  -- first set bit become zero 
# n&n-1  -100000

#O(SETBIT )

def countSetBitEff(num):
    count=0
    while num!=0:
        num=num&(num-1)
        count+=1
    return count    

print(countSetBitEff(2))