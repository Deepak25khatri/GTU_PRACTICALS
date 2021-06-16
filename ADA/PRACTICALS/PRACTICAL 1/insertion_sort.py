def Insertion_sort(Arr):
    n=len(Arr)
    for i in range(n):
        flag=Arr[i]
        j=i-1
        while j>=0 and Arr[j]>flag:
            Arr[j+1],j=Arr[j],j-1
        Arr[j+1]=flag
arr = [10,9,8,7,6,5,4,3,2,1]
Insertion_sort(arr)
print(arr)
