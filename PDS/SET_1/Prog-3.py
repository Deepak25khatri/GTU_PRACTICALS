# Python Program for Sum of squares of first n natural numbers

def sum(n):
    return (n*(n+1)*(2*n+1)//6)

num=int(input("Enter the number : "))
print("The sum of squares of all natural numbers till",num,"is :",sum(num))