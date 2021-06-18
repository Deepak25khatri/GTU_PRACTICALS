# Python Program for array rotation

def L_rotation(Arr,n,d):
    for i in range(d):
        x=Arr.pop(0)
        Arr.append(x)

def R_rotation(Arr,n,d):
    for i in range(d):
        x=Arr.pop(n-1)
        Arr.insert(0,x)

Arr=[0,1,2,3,4,5,6,7,8,9]
print(Arr)
n=len(Arr)
d=int(input("Enter the rotation length : "))
ch=str(input("Enter L for Left Rotation/ R for Right Rotation : "))
if ch=='L' or ch=='l':
    L_rotation(Arr,n,d)
    print(Arr)
elif ch=='R' or ch=='r':
    R_rotation(Arr,n,d)
    print(Arr)
else:
    print("Please Enter appropriate choice..")
    