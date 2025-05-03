#lcm:least common multile 
# a=4 b=6 lcm = 12 (lowest number which is divisble by both is 12 )

# a=2  b=8 lcm =8 (if one of number is divisble by other then ans is ans )

# a=3 b =7 --(co prime- no factor common ) then thier multiple will be lcm =21

# first we take a value max(a,b)
# we will keep on checking if res%a==0 and res%b==0 and if not then increment 



def lcm(a,b):
    res =max(a,b)

    while True:
        if(res%a ==0 and res%b==0):
            return res
        res+=1

    return res 

print(lcm(4,6))     



# we can further optimized it 

# we know a*b = gcd(a,b)*lcm(a,b)
#         4*6 = gcd(4,6)*12
#          24 = 2*12
# o(log(min(a,b)))


#so as we know gcd we can use this  

def lcmOpti(a,b):
    return (a*b)//gcdOtmizedEculid(a,b)


print(lcmOpti(4,6))