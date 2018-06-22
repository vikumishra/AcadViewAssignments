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

#Question-5





