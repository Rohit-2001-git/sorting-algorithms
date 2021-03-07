def mergesort(mylist):
    if len(mylist)>1:
        mid=len(mylist)//2
        left=mylist[:mid]
        right=mylist[mid:]
        mergesort(left)
        mergesort(right)
        #two left and right iterators and main iterators
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                mylist[k]=left[i]
                i=i+1
                k=k+1
            else:
                mylist[k]=right[j]
                j=j+1
                k=k+1
        while i <len(left):          #for left out one
            mylist[k]=left[i]
            i=i+1
            k=k+1
        while j <len(right):
            mylist[k]=right[j]
            j=j+1
            k=k+1
mylist=[100,400.1,2,3,780,-1]
mergesort(mylist)
print(mylist)
