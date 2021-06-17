from time import *
def Selection_sort(Arr):
    n=len(Arr)
    for i in range(n):
        min=Arr[i]
        index=i
        for j in range(i+1,n):
            if min>Arr[j]:
                min,index=Arr[j],j
        Arr[i],Arr[index]=Arr[index],Arr[i]

init_time=time()
arr = [40,39,38,37,36,35,34,33,32,31,30,29,28,27,26]
print(arr)
print("Selection sort started")
Selection_sort(arr)
print(arr)
print("Selection sort Completed in",(time()-init_time),"sec")