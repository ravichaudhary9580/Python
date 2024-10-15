""" i=1
while i<=5:
    print("MySirG")
    i=i+1;     """


""" n=int(input("Enter a number:"))
i=1
while i<=n:
    print(i,end=' ')
    i+=1 """


""" n=int(input("Enter a number:"))
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print("Sum of fist N natural numbers:",sum) """

""" n=int(input("Enter a number:"))
i=1
count=0
while i<=n:
    if n%i==0:
        count=count+1
    i=i+1
if count>2:
    print("Not prime")
else:
    print("Prime")

n=int(input("Enter a number:"))
i=2
while i<=n:
    if n%i==0:
        break
    i+=1
if i==n:
    print("Prime")
else:
    print("Not Prime")

n=int(input("Enter a number:"))
i=2
while i<=n:
    if n%i==0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime") """


""" n=input("Enter a string:")

for i in n:
    print(i,ord(i))
  """  


""" n=int(input("Enter a number:"))
r=range(1,n+1)
for e in r:
    print(e,end=' ') """

n=int(input("Enter a number:"))
r=range(1,n+1)
for e in r:
    print(e,e**2)