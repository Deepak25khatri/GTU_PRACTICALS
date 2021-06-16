def Selection_sort(Arr):
    n=len(Arr)
    for i in range(n):
        min=Arr[i]
        index=i
        for j in range(i+1,n):
            if min>Arr[j]:
                min,index=Arr[j],j
        Arr[i],Arr[index]=Arr[index],Arr[i]
arr = [10,9,8,7,6,5,4,3,2,1]
Selection_sort(arr)
print(arr)
