from time import *
def Insertion_sort(Arr):
    n=len(Arr)
    for i in range(n):
        flag=Arr[i]
        j=i-1
        while j>=0 and Arr[j]>flag:
            Arr[j+1],j=Arr[j],j-1
        Arr[j+1]=flag
init_time=time()
arr = [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11]
print(arr)
print("Insertion Sort started")
Insertion_sort(arr)
print(arr)
print("Insertion Sort Completed in",(time()-init_time),"sec")
