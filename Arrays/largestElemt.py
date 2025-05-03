# given an array and we need to find out index of largest element in array 

def lagestIndex(lst):
    res=0
    for i in range(0,len(lst)):
        if lst[i]>lst[res]:
            res=i

    return res
           

            