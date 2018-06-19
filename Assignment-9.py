
#Question-1
import threading
import time
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        time.sleep(5)
        print("Thread %d was slept for 5 seconds.. and now it is working.."%(self.h))

Thread1=Mythread(1)
Thread1.start()

#Question-2
class Mythread2(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run(self):
        print("Thread %d will now print from 1 to 10 with lag of 1 second in between"%(self.h))
        for i in range(10):
            print(i)
            time.sleep(1)

Thread2=Mythread2(2)
Thread2.start()


#Question-3
li1=[2,4,6,8,10]
class Mythread3(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        for i in li1:
            print(i)
            time.sleep(i)
Thread3=Mythread3()
Thread3.start()

#Question-4
def factorial(p):
    if(p==1):
        return 1
    else:
        t=p*factorial(p-1)
        return t

class Mythread4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k=factorial(5)
        print("Print factorial of number 5 is %d"%(k))

Thread4=Mythread4()
Thread4.start()












