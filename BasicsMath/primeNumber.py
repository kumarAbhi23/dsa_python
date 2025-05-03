# a number is said is to be prime if it is divisble by 1 and itslef 

# 1 is nor prime nor composite

import math
#naive approch : check from 2 to n-1 if any one divides then return false else true 

  # time complexity will be O(N)

def primeNavie(number):
    if number==1:
         return False
    else:
        for i in range(2,number-1):
            if i%2==0:
                return False


    return True   


# EFFICENT Approch will :
# lets see divisor of number 
# 30 - (1,30) (2,15) (3,10), (5,6)     
# (x,y) is pair 
# x*y=n  lets consider x<=y
# x*x=n
# x <=Square root(n) 

# not to check from 2 to n-1 insted of we can check to 2 to sqrt(n)

def primeEfficient(num):
    if num==1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))):
            if i%2==0:
                return False

    return True     

# there can more efficent if we check divisblity by 2 and 3 we can sakip many iteration also 
# if a number is not divisble by 2 then we need not to check it from 4,6,8,10,12,14,16,18....
# similarly we can skip iteration if divisble by 3 then 9,15....
#     
def primeMoreEff(num):
    if num==1:
        return False
    if num==2 or num==3 :
        return True 
    if num %2==0 or num %3==0:
         return False
    else:
        for i in range(5,int(math.sqrt(num)),6):
           if  num%i==0  or num%i+2:
              return False

    return True          

#print(primeNavie(3))   
#print(primeEfficient(7)) 
print(primeMoreEff(18))           

