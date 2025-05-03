# gcd of two number 
# greatest common divisor 

   # lets see by exmaple :
       # a=4, b=6  o/p =2 
       # a=100 b= 200 
        # a complety divides b so a is gcd 


# naive approch will : a=12  and b =15 
      # we will take min of these two and check with minimum that will divide both of them 
      # and keep decresing 
      # 12,11,,....3 will divide both of them so 3 will be ans 

      # time complexity will be O(MIN(a,b))




# Eculid algorithm
# a=12 b=15
# we will keeo on decresing higest -lowest (we need to subtract it till both a and b becomes equal )

# def gcdEculid(a,b):

#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a

#     #return any value 
#     return a   


# more optimized version this alogrithm is :
# we will find gcd(a,b)= if b==0 return a
# else we call gcd(b,a%b) ...keep on till we achive our termination condition 

#  o(log(min(a,b)))

def gcdOtmizedEculid(a,b):
    if b==0:
        return a
    return gcdOtmizedEculid(b,a%b)    



print(gcdOtmizedEculid(12,15))