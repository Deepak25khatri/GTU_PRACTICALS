from time import *
def Bubble_sort(Arr):
    n=len(Arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if Arr[j]>Arr[j+1]:
                Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            j=j+1
init_time=time()
arr = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print(arr)
print("Bubble Sort started")
Bubble_sort(arr)
print(arr)
print("Bubble Sort Completed in",(time()-init_time),"sec")