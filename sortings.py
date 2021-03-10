import random
import time
def insertionsort(mylist):
    n=len(mylist)
    for i in range(1,n):
        key=mylist[i]
        j=i-1
        while mylist[j]>key and j>-1:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=key
        
            
def bubblesort(mylist):
    n=len(mylist)
    for i in range(n):
        for j in range(n-i-1):
            if mylist[j]>mylist[j+1]:
                temp=mylist[j]
                mylist[j]=mylist[j+1]
                mylist[j+1]=temp

def selectionsort(mylist):
    n=len(mylist)
    for i in range(n):
        for j in range(i,n):
            if mylist[i]>mylist[j]:
                temp=mylist[i]
                mylist[i]=mylist[j]
                mylist[j]=temp
def calc1(mylist):
    start=time.time()
    bubblesort(mylist)
    end=time.time()
    exec_time=end-start
    list1.append(exec_time)
    start=time.time()
    insertionsort(mylist)
    end=time.time()
    exec_time=end-start
    list2.append(exec_time)
    start=time.time()
    selectionsort(mylist)
    end=time.time()
    exec_time=end-start
    list3.append(exec_time)
def calc2(mylist):
    start=time.time()
    bubblesort(mylist)
    end=time.time()
    exec_time=end-start
    list4.append(exec_time)
    start=time.time()
    insertionsort(mylist)
    end=time.time()
    exec_time=end-start
    list5.append(exec_time)
    start=time.time()
    selectionsort(mylist)
    end=time.time()
    exec_time=end-start
    list6.append(exec_time)

def calc3(mylist):
    start=time.time()
    bubblesort(mylist)
    end=time.time()
    exec_time=end-start
    list7.append(exec_time)
    start=time.time()
    insertionsort(mylist)
    end=time.time()
    exec_time=end-start
    list8.append(exec_time)
    start=time.time()
    selectionsort(mylist)
    end=time.time()
    exec_time=end-start
    list9.append(exec_time)
    
tc=int(input())
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
list9=[]

for i in range(tc):
    mylist=[]
    size=int(input())
    for i in range(size):
        b=random.randrange(1,100)
        mylist.append(b)
    calc1(mylist)
    mylist.sort()
    calc2(mylist)
    mylist.reverse()
    calc3(mylist)
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)









    
        
            
    
    
