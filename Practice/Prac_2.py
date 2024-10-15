# Program 1
""" n=int(input("Enter a number:"))
i=1
while i<=n:
    print(2*i-1,end=' ')
    i=i+1 """

# Program 2
""" n=int(input("Enter a number:"))
i=1
while i<=n:
    print(2*i,end=' ')
    i=i+1 """

#Program 3 
""" n=int(input("Enter a number:"))
while n!=0:
    print(2*n-1,end=' ')
    n=n-1 """

#Program 4
""" n=int(input("Enter a number:"))
i=1
while i<=n:
    print(i,i*i)
    i+=1 """

#Program 5
""" print("Sum of first N natural number.")
n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum is:",sum) """

#Program 6
""" print("Factorial of N.")
n=int(input("Enter a number:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print("Factorial of",n,"is",fact) """

#Program 7 
""" print("Count digit in a number.")
n=int(input("Enter a number:"))
count=0
while n:
    n=n//10
    count=count+1
print("No. of digit is:",count) """

#Program 8
""" print("Sum of digits of a number.")
n=int(input("Enter a number:"))
sum=0
while n:
    sum=sum+n%10
    n=n//10
print("Sum of digit is:",sum) """

#Program 9
""" print("Check Prime or Not.")
n=int(input("Enter a number:"))
i=2
while i<n:
    if n%i==0:
       break
    i+=1
if i==n:
    print("Prime")
else:
    print("Not Prime") """

""" print("Check Prime or Not.")
n=int(input("Enter a number:"))
i=2
while i<n:
    if n%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime") """ 

#Program 10
""" print("LCM of 2 numbers.")
print("Enter two number:")
a=int(input())
b=int(input())
LCM=a if a>b else b
while LCM<=a*b:
    if LCM%a==0 and LCM%b==0:
        break
    LCM+=1
print("LCM is:",LCM) """