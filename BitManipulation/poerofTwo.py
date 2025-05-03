# we are given a number and we need to tell wheather number is power of two or not 

#ex: 4 -true
#    0 -false 
#    6-flase 

# basically if we able to repsemnt a number on 2^x=number then number is power of two 


# basic naive approch will be : we will check if remainder is zero then keep on dividng by at the end 
# if n==1 then return true 
# time complexity will be O(logn)


def checkPowerTwo(n):
     
     if n==0:
        return False
     while n!=1:
        if n%2!=0:
            return False 
        n=n//2

     return True  



# if we use bitwise operator we can make it better 
# if in a number there is only a set bit then it is power of two

# 1=000000...001
# 2=000000....10
# 4=0000000...100

# 3= 0000.....0011 : 2 set bit not a power of two

# if we use # Berian kergingam algo
# for power of set bit time will be constant but if not power of two then timw will be O(SETbits)...
# we can use same approch with some modifications

# Apprcoh will we will reset very first bit and if number is 0 then return true else 
# return false as it may contain more than 1 set bits 

def checkPowerTwoEff(num):
    if num==0:
        return False
    else:
        return (num & (num-1)==0)
  

    
    
              


#print(checkPowerTwo(6))
print(checkPowerTwoEff(5))
