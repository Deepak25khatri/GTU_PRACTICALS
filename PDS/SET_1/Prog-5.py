# Python Program to Split the array and add the first part to the end

def Split_and_add_at_end(Arr,n,d):
    for i in range(d):
        x=Arr.pop(0)
        Arr.append(x)

List=[1,11,21,31,41,51,61,71,81,91]
print(List)
n=len(List)
d=int(input("Enter the size of Array you want to split : "))
Split_and_add_at_end(List,n,d)
print(List)