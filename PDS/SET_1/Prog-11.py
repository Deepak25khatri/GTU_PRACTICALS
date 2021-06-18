 # Python program to find N largest elements from a list
 
L1 = [4, 5, 1, 2, 9]
x=int(input("Enter n to get N largest element from list : "))
L2=L1
for i in range(x):
    print(max(L2), end=' ')
    L2.remove(max(L2))
    