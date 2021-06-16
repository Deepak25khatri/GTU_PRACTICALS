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

num=[10,9,8,7,6,5,4,3,2,1]
n=len(num)
quick_sort(num,0,n-1)
print(num)