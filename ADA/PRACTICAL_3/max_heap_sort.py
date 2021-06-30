from time import *

def Heapify(arr,n,i):
    L = i
    left=2*i+1
    right=2*i+2
    if left<n and arr[i]<arr[left]:
        L=left
    if right<n and arr[L]<arr[right]:
        L=right
    if L!=i:
        arr[i],arr[L]=arr[L],arr[i]
        Heapify(arr,n,L)
  
def heapSort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        Heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)
  
arr = [58,96,14,23,74,52,49,37,82,99,9,1,28,77,29]
t=time()
heapSort(arr)
n = len(arr)
print(arr)
print("Max-Heap sort completed in ",time()-t," sec")

  