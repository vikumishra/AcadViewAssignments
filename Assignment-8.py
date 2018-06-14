import datetime
import time
import math
import os

#Question-1
#the time tuple is a tuple of 9 values which represt time attributes...
#these are (0)tm_year (1)tm_month (2)tm_day (3)tm_hour (4)tm_month (5)tm_sec
#(6)tm_wkday (7)tm_yday (8)tm_isdst

#Question-2
print('formated time is ')
print(time.asctime())
print('\n')

# Question-3
print("extracted month is ")
d = datetime.date.today()
print (d.month)
print('\n')

#Question-4
print("extracted day is ")
d = datetime.date.today()
print (d.day)
print('\n')

#Question-5
k="11-01-2021"
l=datetime.datetime.strptime(k,"%d-%m-%Y")
print(l.day)
print('\n')

#Question-6
print("Time printed using local time is ")
print(time.asctime(time.localtime()))
print('\n')

#Question-7
fact=int(input("input enter the number whose factorial u want to find"))
print("Factorial of number %d is "%(fact))
print(math.factorial(fact))
print('\n')

#Question-8
num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("gcd of %d and %d is"%(num1,num2))
print(math.gcd(num1,num2))
print('\n')

#Question-9
print("Current working directory is ")
print(os.getcwd())
print("user environment is")
print(os.environ)




