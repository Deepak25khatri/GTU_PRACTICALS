from time import *
def merge_sort(Arr, p, r):
    if r - p > 1:
        q = (p + r)//2
        merge_sort(Arr, p, q)
        merge_sort(Arr, q, r)
        merge(Arr, p, q, r)
 
def merge(Arr, p, q, r):
    L = Arr[p:q]
    R = Arr[q:r]
    k = p
    i = 0
    j = 0
    while (p + i < q and q + j < r):
        if (L[i] <= R[j]):
            Arr[k] = L[i]
            i = i + 1
        else:
            Arr[k] = R[j]
            j = j + 1
        k = k + 1
    if p + i < q:
        while k < r:
            Arr[k] = L[i]
            i = i + 1
            k = k + 1
    else:
        while k < r:
            Arr[k] = R[j]
            j = j + 1
            k = k + 1
 
init_time=time()
arr = [55,54,53,52,51,50,49,48,47,46,45,44,43,42,41]
print(arr)
print("Merge Sort started")
merge_sort(arr,0,(len(arr)-1))
print(arr)
print("Merge Sort Completed in",(time()-init_time),"sec")
