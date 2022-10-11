1)LEAP YEAR
year = 2000
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
2)AMSTRONG NUMBER
def amstrongnum(n):
    t=n
    l=len(str(n))
    s=0
    while n>0:
        d=n%10
        s=s+d**l
        n=n//10
    return t==s
amstrongnum(143)
3)PRIME NUMBER
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
4)GCD OF 2 NUMBERS
def gcd(n1,n2):
    if(n1>n2):
        small=n2
    else:
        small=n1
    for i in range(1,small+1):
        if((n1%i==0) and (n2%i==0)):
            g=i
    return g
gcd(60,48)
5)GCD
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
gcd(60,48)
6)Amstrong Number
l=[0,1]
for i in range(10):
    l.append(l[-1]+l[-2])
print(l)
7)Amstrong Number
l=[0,1]
[l.append(l[-1]+l[-2]) for i in range(5)]
print(l)
8)FIND ASCI VALUE
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
9)zip function
index = [1, 2, 3]
languages = ['python', 'c', 'c++']
dictionary = dict(zip(index, languages))
print(dictionary)
10)index = [1, 2, 3]
languages = ['python', 'c', 'c++']
dictionary = {k: v for k, v in zip(index, languages)}
print(dictionary)
11)Reverse a digit
n=int(input())
s=0
while n>0:
    d=n%10
    s=s*10+d
    n=n//10
print(s)
