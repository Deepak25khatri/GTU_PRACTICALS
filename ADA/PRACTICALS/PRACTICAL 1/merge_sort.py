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
 
num = [10,9,8,7,6,5,4,3,2,1]
n= len(num)
merge_sort(num,0,n)
print(num)
