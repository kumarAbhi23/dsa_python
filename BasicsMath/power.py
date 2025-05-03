# we have inbuild function for computing power 
# power (x,n) : x*x...n times 

# naive approch will be
# it is taking O(N) 

def powNaive(x,n):
    ans=1
    while n!=0:
        ans*=x
        n-=1
    return ans    

# We can optimized it further 

# approch we call recursive pow(x,n)->pow(x,n/2)...
# every time we making n/2: ...timecomplexity will be --logn 

def powerEff(x,n):
    if n==0:
        return 1  #base condition 

    temp =powerEff(x,n//2)     
    temp*=temp
    if n%2==0:
        return temp
    else:
        return temp*x


#print(powNaive(2,3))
print(powerEff(2,3))