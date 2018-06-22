
#question-1
f=open("test1.txt","r")
n=int(input("Enter number of lines you want to read from end"))
k=f.readlines()
k.reverse()
for i in range(n):
    print(k[i])
f.close()


#Question-2
a="said"
f1=open("test1.txt","r")
k=f1.read()
m=k.split()
print("Frequency of words in a given file is..")
print(m.__len__())
print("frequency of word said is ")
print(k.count(a))
f1.close()


#Question-3
f2=open("OriginalFileForQsn3.txt","r")
f3=open("CopyFileForQsn3.txt","w")
q=f2.read()
f3.write(q)

#Question-4
obj4=open("file1.txt","r")
obj5=open("file2.txt","r")
obj6=open("file3.txt","w")
li1=obj4.readlines()
li2=obj5.readlines()
for i in range(li1.__len__()):
    obj6.write(li1[i].strip('\n')+'\t'+li2[i])
obj4.close()
obj5.close()
obj6.close()



#Question-5
import random
obj1=open("UnsortedFile.txt","w")
obj2=open("SortedFile.txt","w")
unsortli=[]
sortli=[]
str1=""
str2=""
#Writing the unsorted numbers in unsorted.txt file
for i in range(10):
    a=random.randint(0,9)
    unsortli.append(a)
for j in unsortli:
    str1="".join(str(j))
    obj1.write(str1+"\n")
obj1.close()
#Reading The Unsorted.txt file and sorting it
obj3=open("UnsortedFile.txt","r")
str5=obj3.read()
print("Unsorted random numbers read from unsortedfile are")
print(str5)
for x in str5:
    if(x.isdigit()):
        str6="".join(x)
        sortli.append(str6)
sortli.sort()
#Writing the sorted list of numbers into sorted.txt file
for k in sortli:
    str2="".join(str(k))
    obj2.write(str2+"\n")
obj2.close()
obj3.close()









