from time import *
def partition(Arr,p,r):
    x=Arr[r]
    i=p-1
    for j in range(p,r):
        if Arr[j]<=x:
            i=i+1
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[i+1],Arr[r]=Arr[r],Arr[i+1]
    return i+1

def quick_sort(Arr,p,r):
    if p<r:
        q=partition(Arr,p,r)
        quick_sort(Arr,p,q-1)
        quick_sort(Arr,q+1,r)

init_time=time()
arr = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86]
print(arr)
print("Quick Sort started")
quick_sort(arr,0,(len(arr)-1))
print(arr)
print("Quick Sort Completed in",(time()-init_time),"sec")
