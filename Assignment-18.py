#Question-1 And Question-2
from tkinter import *
from tkinter import messagebox
dic={'Vivek':9872435977,'Deepansh':9109508408,'Ajay':9876545291,'Biju':9888765754,'Shubham':987654356}
def savephnn():
    if (e1.index(END)==0 or e2.index(END)==0):
        messagebox.showwarning("Warning","Please enter all values")
    else:
        nam = e1.get()
        phn = int(e2.get())
        myList.insert(i, nam + "-" + str(phn))
        e1.delete(0, END)
        e2.delete(0, END)
        messagebox.showinfo("Congrats","Contact addded")
root=Tk()
lbl1=Label(root,text="Phone Directory")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in dic:
    myList.insert(i,line+"-"+str(dic[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save",command=savephnn)

lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()
