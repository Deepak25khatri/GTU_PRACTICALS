# Max-Heap Sort

def max_heapify(Arr,i):
    n=len(Arr)
    L=Arr[2*i]
    R=Arr[2*i+1]
    if L<=n and Arr[L]>Arr[i]:
        Largest=L
    else:
        Largest=i
    if R<n and Arr[R]>Arr[Largest]:
        Largest=R
    if Largest!=i:
        Arr[i],Arr[Largest]=Arr[Largest],Arr[i]
        max_heapify(Arr,Largest)



def build_max_heap(Arr):
    n=len(Arr)
    for i in range((n//2),0):
        max_heapify(Arr,i)


def heap_sort(Arr):
    n=len(Arr)
    build_max_heap(Arr)
    for i in range(n,1):
        Arr[1],Arr[i]=Arr[i],Arr[1]
        n=n-1
        max_heapify(Arr,1)

L1=[9,5,7,12,2,6,4]
heap_sort(L1)
print(L1)
