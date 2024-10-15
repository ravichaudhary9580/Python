#Program 1
""" print("Sum of two numbers.")
print("Enter two number:")
x=int(input())
y=int(input())
print("Sum of two number is:",x+y)

x,y=input("Enter two number with space:").split(' ')
x=int(x)
y=int(y)
print("Sum is:",x+y) """


#Program 2
""" print("Subtraction of two numbers.")
print("Enter two number:")
x=int(input())
y=int(input())
print("Difference of two number is:",x-y)

x,y=input("Enter two number with minus symbol(-):").split('-')
x=int(x)
y=int(y)
print("Differnce is:",x-y) """

#Program 3
""" print("Product of two numbers.")
x,y=input("Enter two number:").split(' ')
x=int(x)
y=int(y)
print("Product is:",x*y) """

#Program 4
""" print("Division of two numbers.")
x,y=input("Enter two number:").split(' ')
x=int(x)
y=int(y)
print("Product is:",x/y) """

#Program 5
""" print("Calculating Remainder when one number is divided by other number.")
x,y=input("Enter two number:").split(' ')
x=int(x)
y=int(y)
print("Remainder is:",x%y) """

#Program 6
""" print("Calculate Power")
x,y=input("Enter two number:").split(' ')
x=int(x)
y=int(y)
print("Product is:",x**y) """

#Program 7
import math
# Square root of a number.
""" print('Squre root is:',math.sqrt(int(input("Enter a number:")))) """

#Program 8
""" print('Even') if int(input("Enter a number:"))%2==0 else print('Odd')  """

#Program 9
""" n=int(input("Enter a number:"))
if n>0:
    print('Positive')
elif n<0:
    print('Negative')
else:
    print('Zero') """

#Program 10
""" a,b,c=input('Enter three number:').split(' ')
a=int(a)
b=int(b)
c=int(c)
if a>b:
    if a>c:
        print(a,'is greatest.')
    else:
        print(c,'is greatest.')
else:
    print(b,'is greatest.') """

#Program 11
""" a,b,c=input('Enter three number:').split(' ')
a=int(a)
b=int(b)
c=int(c)
if a<b:
    if a<c:
        print(a,'is Smallest')
    else:
        print(c,'is Smallest')
else:
    print(b,'is Smallest') """

#Program 12
""" n=int(input('Enter a number:'))
if n%5==0 and n%11==0:
    print(n,'is divisble by 5 and 11')
else:
    print('Not divisble by 5 and 11') """

#Program 13
""" n=int(input('Enter a year:'))
if n%100==0:
    if n%400==0:
        print("Leap Year")
    else:
        print('Not a Leap Year')
elif n%4==0:
    print('Leap Year')
else:
    print('Not a Leap Year') """

#Program 14
""" ch=input('Enter a Character:')
if ch.isalpha():
    for e in 'aeiou':
        if e is ch:
            print('Vowel')
            break
        else:
            print('Consonant')
            break """

#Program 15
""" ch=input('Enter a Character:')
if ch.isalpha():
    print('Alphabet')
elif ch.isdigit():
    print('Digit')
else:
    print("Special Character") """

#Program 16
""" a=int(input())
b=int(input())
if a>b:
    print(a,'is greater')
else:
    print(b,'is greater') """

#Program 17
""" a=int(input())
b=int(input())
if a<b:
    print(a,'is smaller')
else:
    print(b,'is smaller') """

#Program 18
n=input('Enter a number:')
if n == n[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')
