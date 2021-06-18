#  Python Program to check if given array is Monotonic

def check_monotonic(Arr,n):
    if Arr[0]<=Arr[1]:
        for i in range(n-1):
            if Arr[i]>Arr[i+1]:
                return False
        else:
            return True
    elif Arr[0]>=Arr[1]:
        for i in range(n-1):
            if Arr[i]<Arr[i+1]:
                return False
        else:
            return True

n=int(input("Enter Size of Array :"))
Arr=[0]*(n)
for i in range(n):
    print("Arr[",i,"] :",end=' ')
    Arr[i]=int(input())
print("Entered Array is : ",Arr)
print(check_monotonic(Arr,n))