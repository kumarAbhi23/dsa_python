# write program to count number of digits in a number 
# 9234- o/p:4

#concept: if we divide number given number with 10 then last digit will be removed ...do till number gets 0 and evry 
# time make a counter variable 


 # 9234//10= 923 and if we wanted number which is removed then we can do 9234%10=4  -- it will last digit 



n= eval(input("enter number : "))
count=0
while n>0:
    #divide 
    n= n//10
    #incrment count 
    count+=1

print(count)
