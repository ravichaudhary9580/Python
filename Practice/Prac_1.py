#Program 1
'''
x,y=float(input("Enter the length:")),float(input("Enter the breadth:"))
print("Area of Rectangle:",x*y)
'''

#Program 2
'''
principle=int(input("Enter the principle:"))
rate=float(input("Enter the rate:"))
time=int(input("Enter the time:"))

si=(principle*rate*time)/100
print("Simple Interest:",si)
'''

#Program 3
""" 
number=int(input("Enter a number:"))
print(number)
number=number//10
print("Number after last digit:",number)
"""

#Program 4
"""
x,y=3,4
c=x
x=y
y=c
print(x,y)
"""

#Program 5
""" 
x=int(input("Enter a number:"))
if x%5==0:
    print("Divisible by 5")
else:
    print("Not")
"""

#Program 6

#Program 7
""" 
x=int(input("Enter a Number:"))
if x>99 and x<1000:
    print("Given number is of 3 digit.")
else:
    print("Not 3 digit number.")
"""

#Program 8
""" 
year=int(input("Enter a year:"))
if year%400==0:
    print("Leap year.")
elif year%100==0:
    print("Not a Leap year.")
elif year%4==0:
    print("Leap year.")
else:
    print("Not a Leap year.")
"""

#Program 9
""" 
number=int(input("Enter a number:"))
if number<0:
    print("Negative number.")
if number==0:
    print("Zero.")
if number>0:
    print("Positive number.")
"""

#Program 10
""" 
x=complex(input("Enter a complex number:"))
print(x)
if x.real>x.imag:
    print(x.real,"is greater part.")
else:
    print("Imaginary part is greater.")
""" 