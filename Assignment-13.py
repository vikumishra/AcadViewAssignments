#Question-1
#Exception Occured is ZeroDivisionError
try:
    a=3
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
    print("Zero Division HAs Occured")

#Question-2
#Exception Occured is IndexError
try:
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("Index out of bound")

#Question-3
#Output of the folloeing code is An Exception

#Question-4
#-1
#a/b result is zero

#Question-5
#Import Error
try:
    import viku
except ImportError:
    print("import error")

#Value Error
try:
    a=int(input("Enter number"))
    print(a)
except (ValueError):
    print("Please Enter Only Number")

#Index Error
try:
    a=[1,2,3]
    print(a[3])
except IndexError:
    print("Index out of bound")

#Question-6
class AgeTooSmall(Exception):
    pass
c=1
while(c==1):
    age = int(input("Enter Age"))
    try:
        if(age<18):
            raise AgeTooSmall

    except AgeTooSmall:
        print("Sorry age is too small.. Please enter age greater then or equal to 18")
    else:
        print("Congratulations You entered valid age which is %d "%(age))
        c=-1




