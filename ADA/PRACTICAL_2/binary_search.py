def binary_search(Arr, x):
    l = 0
    r = len(Arr)-1
    q = 0
    while l <= r:
        q = (r + l) // 2
        if Arr[q] < x:
            l = q + 1
        elif Arr[q] > x:
            r = q - 1
        else:
            return q
    return -1
 

L1 = [ 2,3,4,10,40,54,65,78,88,89,91,92,98,100]
x =int(input('Enter the number to Search : '))
result = binary_search(L1, x)
if result != -1:
    print("\'",x,"\' is present at index",result)
else:
    print("\'",x," is not present in List")