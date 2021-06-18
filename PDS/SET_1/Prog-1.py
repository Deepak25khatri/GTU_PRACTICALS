# Python program to print all Prime numbers in an Interval.

l=int(input("Enter Lower Bound : "))
u=int(input("Enter Upper Bound : "))
print("The prime numbers between ",l," and ",u," are :-")
for i in range(l,u+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
            break
        