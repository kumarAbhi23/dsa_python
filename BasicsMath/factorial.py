# program to find factorial of numnber
# 5!= 5*4*3*2*1=120


def fact(num):
    res=1
    for i in range(2,num+1):
        res=res*i

    return res    

print(fact(6))      