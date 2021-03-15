def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r):
         if a[j]<=x:
             i=i+1
             a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return a
             


def quicksort(a,p,r):
    if(p<=r):
        partition(a, p, r)
        quicksort(a, p, r-1)
        quicksort(a, p+1, r)

a=[2,8,7,1,3,5,6,4]
quicksort(a, 0, 7)
print(a)