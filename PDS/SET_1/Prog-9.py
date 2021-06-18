# Program to print duplicates from a list of integers
L1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
res=[]
for i in L1:
    if L1.count(i)>1:
        res.append(i)
print(set(res))