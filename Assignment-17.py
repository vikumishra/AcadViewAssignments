from tkinter import *
from tkinter import messagebox
#Question-1
#Fxn to exit from Gui
def Ext():
    messagebox.showwarning("Confirmation","Clicking on ok will exit the current Gui")
    root.quit()
#Function to display some text
def DisplaySomeText():
    messagebox.showinfo("You clicked button for qsn-2","Question-2 Solved")
#Function to display the text of changed label
def ChangeLabelText():
    lbl1.config(text="You changed the text of label")
def KnowTheValue():
    messagebox.showinfo("Entered Value",e1.get())

root=Tk()
root.title("Assignment-17")
root.geometry("400x400")
lbl=Label(root,text="HELLO WORLD")
lbl.place(x=150,y=0)
btndisplay=Button(root,text="Click to see some value in message box",command=DisplaySomeText)
btndisplay.place(x=100,y=50)
btnDisplayText=Button(root,text="Change Label",command=ChangeLabelText)
btnDisplayText.place(x=0,y=90)
lbl1=Label(root,text="Before Changing the label text")
lbl1.place(x=100,y=90)
btnDisplayEnteredValue=Button(root,text="Click to know the enterd value",command=KnowTheValue)
btnDisplayEnteredValue.place(x=0,y=120)
e1=Entry(root)
e1.place(x=180,y=120)
btnExit=Button(root,text="Exit",command=Ext)
btnExit.place(x=200,y=200)
mainloop()