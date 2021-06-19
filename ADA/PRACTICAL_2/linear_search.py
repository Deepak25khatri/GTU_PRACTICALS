L1=[19,85,63,79,24,11,59,9,7,42,4,6,7,25,36]
x=int(input("Enter a number to search : "))
a=False
for i in range(len(L1)):
    if x==L1[i]:
        print("\"",x,"\" found at index ",i)
        a=True
if a==False:
    print("\"",x,"\" not found in list")
