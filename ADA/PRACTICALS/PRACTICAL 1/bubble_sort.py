def Bubble_sort(Arr):
    n=len(Arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if Arr[j]>Arr[j+1]:
                Arr[j],Arr[j+1]=Arr[j+1],Arr[j]
            j=j+1
arr = [3,5,1,8,6,2,4,7,9,10]
Bubble_sort(arr)
print(arr)
