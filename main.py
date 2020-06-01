"""Created on Tue Apr 14 15:08:48 2020
@author: Dhruv  Khurana
"""
checkimport = 0
from tkinter import * 
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk,Image 
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split
import csv
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def dfimport() :
   global df,checkimport,b_next,import_file_path
   import_file_path = filedialog.askopenfilename()
   if import_file_path.endswith('.csv'):
      canvas2.create_text(240,260,fill="darkblue",font="Arial 12 bold",text="File read successfully!",tag = "read")
      checkimport = 1
      b_next = Button(f3, text='Next',style = 'W.TButton',command=lambda :f4.tkraise())
      b_next.place(relx = 0.8, rely = 0.8, anchor = 'se')
      df = pd.read_csv(import_file_path)
   else: 
      messagebox.showerror("MedPred Warning","Error: Sorry, file format is not supported!") 
def read_back():
    f2.tkraise()
    b_next.destroy()
    canvas2.delete("read")
def butpress(v):
    global checkimport
    if v.get() == 1:
     f4.tkraise()
     checkimport = 0
    elif v.get() == 2:
     f3.tkraise()
    else: 
     messagebox.showwarning("MedPred","AppWarning: You must select an option to proceed further.")         
def train():
   global drugTree
   global bn,acc
   if checkimport == 0:
     my_data = pd.read_csv("drug200.csv", delimiter=",")
     X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
     Label_s = preprocessing.LabelEncoder()
     Label_s.fit(['M','F'])
     X[:,1] = Label_s.transform(X[:,1]) 
     Label_BP = preprocessing.LabelEncoder()
     Label_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
     X[:,2] = Label_BP.transform(X[:,2])
     Label_C = preprocessing.LabelEncoder()
     Label_C.fit([ 'NORMAL', 'HIGH'])
     X[:,3] = Label_C.transform(X[:,3]) 
     y = my_data["Drug"]
     X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
     drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
     drugTree.fit(X_trainset,y_trainset)
     predTree = drugTree.predict(X_testset)
     acc = metrics.accuracy_score(y_testset, predTree)
     canvas3.create_text(240,280,fill="black",font="Arial 12 bold",text="Model is trained.",tag = "Trained")
     messagebox.showinfo("MedPred"," Training completed! ")
     bn = Button(f4, text='Next',style = 'W.TButton',command=lambda :f5.tkraise())
     bn.place(relx = 0.85, rely = 0.85, anchor = 'se')
   else:
       if len(df)==0:
           messagebox.showerror("MedPred Warning","Error: Training failed! File is empty/corrupted")
       elif len(df)<10: 
           messagebox.showwarning("MedPred Error","Error: Training failed! File is too short. We recommend min. size of 10 samples for a good model training")
       else:
          X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
          Label_s = preprocessing.LabelEncoder()
          Label_s.fit(['M','F'])
          X[:,1] = Label_s.transform(X[:,1]) 
          Label_BP = preprocessing.LabelEncoder()
          Label_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
          X[:,2] = Label_BP.transform(X[:,2])
          Label_C = preprocessing.LabelEncoder()
          Label_C.fit([ 'NORMAL', 'HIGH'])
          X[:,3] = Label_C.transform(X[:,3]) 
          y = df["Drug"]
          X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)
          drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
          drugTree.fit(X_trainset,y_trainset)
          predTree = drugTree.predict(X_testset)
          acc = metrics.accuracy_score(y_testset, predTree)
          canvas3.create_text(240,260,fill="darkblue",font="Arial 12 bold",text="Model is trained.",tag = "Trained")
          messagebox.showinfo("MedPred"," Training completed! ")
          bn = Button(f4, text='Next',style = 'W.TButton',command=lambda :f5.tkraise())
          bn.place(relx = 0.85, rely = 0.85, anchor = 'se')
def train_back():
    f2.tkraise()
    if checkimport==1:
        read_back()
    bn.destroy()
    canvas3.delete("Trained")
def predict(age,sex,bp,c,nak):
    if len(age)==0:
     messagebox.showwarning("MedPred","Please enter age!")    
    elif len(nak)==0 :
     messagebox.showwarning("MedPred","Please enter Na-K level!")
    elif is_integer(age)==False:
     messagebox.showwarning("MedPred","Please enter a valid numeric age!")
    elif is_float(nak)==False:
     messagebox.showwarning("MedPred","Please enter valid Na-K level")
    else:
     age = int(age)
     nak = float(nak) 
     canvas4.delete("predict")
     z = []
     z.append(age)
     z.append(sex.get()) 
     z.append(bp.get())
     z.append(c.get())
     z.append(nak)
     z = np.array(z).reshape(1,-1)
     pred = drugTree.predict(z)
     canvas4.create_text(180,260,fill="black",font="Calibri 14 bold",text="The drug suitable for this patient is: %s"%pred[0],tag="predict")
def load():
    if checkimport == 0:
     window = Toplevel(root)
     window.title("Patient Dataset")
     width = 590
     height = 600
     screen_width = window.winfo_screenwidth()
     screen_height = window.winfo_screenheight()
     x = (screen_width / 2) - (width / 2)
     y = (screen_height / 2) - (height / 2)
     window.geometry("%dx%d+%d+%d" % (width, height, x, y))
     TableMargin = Frame(window, width=700)
     TableMargin.pack(side=TOP)
     scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
     scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
     tree = Treeview(TableMargin, columns=("Age", "Sex", "BP","Cholesterol","Na_to_K","Drug"), height=400, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
     scrollbary.config(command=tree.yview)
     scrollbary.pack(side=RIGHT, fill=Y)
     scrollbarx.config(command=tree.xview)
     scrollbarx.pack(side=BOTTOM, fill=X)
     tree.heading('Age', text="Age", anchor=W)
     tree.heading('Sex', text="Sex", anchor=W)
     tree.heading('BP', text="BP", anchor=W)
     tree.heading('Cholesterol', text="Cholesterol", anchor=W)
     tree.heading('Na_to_K', text="Na_to_K", anchor=W)
     tree.heading('Drug', text="Drug", anchor=W)
     tree.column('#0', stretch=NO, minwidth=0, width=0)
     tree.column('#1', stretch=NO, minwidth=0, width=90)
     tree.column('#2', stretch=NO, minwidth=0, width=90)
     tree.column('#3', stretch=NO, minwidth=0, width=120)
     tree.column('#4', stretch=NO, minwidth=0, width=120)
     tree.column('#5', stretch=NO, minwidth=0, width=90)
     tree.column('#6', stretch=NO, minwidth=0, width=90)
     tree.pack()
     with open('drug200.csv') as f:
      reader = csv.DictReader(f, delimiter=',')
      for row in reader:
       age = row['Age']
       sex = row['Sex']
       bp = row['BP']
       chol = row['Cholesterol']
       nak = row['Na_to_K']
       drug = row['Drug']
       tree.insert("",'end', values=(age,sex,bp,chol,nak,drug))

    else:
       window = Toplevel(root)
       window.title("Patient Dataset")
       width = 590
       height = 600
       screen_width = window.winfo_screenwidth()
       screen_height = window.winfo_screenheight()
       x = (screen_width / 2) - (width / 2)
       y = (screen_height / 2) - (height / 2)
       window.geometry("%dx%d+%d+%d" % (width, height, x, y))
       TableMargin = Frame(window, width=700)
       TableMargin.pack(side=TOP)
       scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
       scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
       tree = Treeview(TableMargin, columns=("Age", "Sex", "BP","Cholesterol","Na_to_K","Drug"), height=400, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
       scrollbary.config(command=tree.yview)
       scrollbary.pack(side=RIGHT, fill=Y)
       scrollbarx.config(command=tree.xview)
       scrollbarx.pack(side=BOTTOM, fill=X)
       tree.heading('Age', text="Age", anchor=W)
       tree.heading('Sex', text="Sex", anchor=W)
       tree.heading('BP', text="BP", anchor=W)
       tree.heading('Cholesterol', text="Cholesterol", anchor=W)
       tree.heading('Na_to_K', text="Na_to_K", anchor=W)
       tree.heading('Drug', text="Drug", anchor=W)
       tree.column('#0', stretch=NO, minwidth=0, width=0)
       tree.column('#1', stretch=NO, minwidth=0, width=90)
       tree.column('#2', stretch=NO, minwidth=0, width=90)
       tree.column('#3', stretch=NO, minwidth=0, width=120)
       tree.column('#4', stretch=NO, minwidth=0, width=120)
       tree.column('#5', stretch=NO, minwidth=0, width=90)
       tree.column('#6', stretch=NO, minwidth=0, width=90)
       tree.pack()
       with open(import_file_path) as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
         age = row['Age']
         sex = row['Sex']
         bp = row['BP']
         chol = row['Cholesterol']
         nak = row['Na_to_K']
         drug = row['Drug']
         tree.insert("",'end', values=(age,sex,bp,chol,nak,drug))
def reset():
    canvas4.delete("predict")
    e_age.delete(0,'end')
    e_nak.delete(0,'end')
def home_back():
    f1.tkraise()
    if checkimport==1:
        b_next.destroy()
        canvas2.delete("read")
    bn.destroy()
    canvas3.delete("Trained")
    reset()
def accuracy():
    g = acc*100
    messagebox.showinfo("MedPred",'The percentage accuracy of this trained model is %f' % g) 
def about():
    top = Toplevel(root)
    top.title("About MedPred")
    top.geometry("300x200")
    canvas=Canvas(top,width=300,height=300)
    canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')
    canvas.create_text(150,100,fill="red",font="Times 13 bold",text="MedPred")
    canvas.create_text(150,120,fill="black",font="Times 11 bold",text="Personalized Drug Prediction App") 
    canvas.create_text(150,140,fill="blue",font="Arial 10",text="© 2020 Dhruv Khurana")
    canvas.create_text(150,160,fill="black",font="Calibri 10",text="This app was developed by Dhruv Khurana")
    canvas.create_text(150,180,fill="black",font="Calibri 10",text="as a part of second-year NTCC Project at ASET, Noida.")
    canvas.create_text(150,230,fill="purple",font="Times 11",text="Datasets have been extracted from the Internet.")
root = Tk() 
img = PhotoImage(file='doctor.ico')
root.tk.call('wm', 'iconphoto', root._w, img)
root.title('MedPred') 
root.geometry("400x400")
root.resizable(0, 0) 
style = Style() 
style.configure('W.TButton', font = ('Calibri', 11),foreground = 'black',highlightbackground = 'blue',background = 'blue')
f1 = Frame(root, width=400, height=400)
f2 = Frame(root, width=400, height=400)
f3 = Frame(root, width=400, height=400)
f4 = Frame(root, width=400, height=400)
f5 = Frame(root, width=400, height=400)   
f1.grid(row=0, column=0, sticky = 'news')
f2.grid(row=0, column=0, sticky = 'news')
f3.grid(row=0, column=0, sticky = 'news')
f4.grid(row=0, column=0, sticky = 'news')
f5.grid(row=0, column=0, sticky = 'news')
canvas2 = Canvas(f3,width=400,height=400)
image2 = ImageTk.PhotoImage(Image.open("medicine.png"))
canvas2.create_image(0,0,anchor=NW,image=image2)
canvas2.place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas1 = Canvas(f2,width=400,height=400)
image1 = ImageTk.PhotoImage(Image.open("medical.png"))
canvas1.create_image(0,0,anchor=NW,image=image1)
canvas1.place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas3 = Canvas(f4,width=400,height=400)
image3 = ImageTk.PhotoImage(Image.open("train.png"))
canvas3.create_image(0,0,anchor=NW,image=image3)
canvas3.place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas3.create_text(200,170,fill="black",font="Arial 11",text="Train the app model for prediction")
canvas4 = Canvas(f5,width=400,height=400)
image4 = ImageTk.PhotoImage(Image.open("pred.png"))
canvas4.create_image(0,0,anchor=NW,image=image4)
canvas4.place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas4.create_text(200,20,fill="black",font="Arial 11 bold",text="DRUG PREDICTION")
canvas4.create_text(87,40,fill="black",font="Calibri 11 bold",text="Enter details of the patient")
canvas4.create_text(20,64,fill="black",font="Times 11 bold",text="Age")
e_age = Entry(f5)
e_age.place(x = 45,y = 52,width=60,height=22)
canvas4.create_text(20,90,fill="black",font="Times 11 bold",text="Sex")
sex = IntVar()
Radiobutton(f5, text='Male',variable=sex, value=1).place(relx = 0.18, rely = 0.22, anchor = 'center')
Radiobutton(f5, text='Female',variable=sex, value=0).place(relx = 0.33, rely = 0.22, anchor = 'center')
canvas4.create_text(55,118,fill="black",font="Times 11 bold",text="Blood Pressure")
bp = IntVar()
Radiobutton(f5, text='Low',variable=bp, value=1).place(relx = 0.33, rely = 0.29, anchor = 'center')
Radiobutton(f5, text='Normal',variable=bp, value=2).place(relx = 0.48, rely = 0.29, anchor = 'center')
Radiobutton(f5, text='High',variable=bp, value=0).place(relx = 0.63, rely = 0.29, anchor = 'center')
canvas4.create_text(45,145,fill="black",font="Times 11 bold",text="Cholesterol")
c = IntVar()
Radiobutton(f5, text='Normal',variable=c, value=1).place(relx = 0.30, rely = 0.36, anchor = 'center')
Radiobutton(f5, text='High',variable=c, value=0).place(relx = 0.45, rely = 0.36, anchor = 'center')
canvas4.create_text(84,175,fill="black",font="Times 11 bold",text="Sodium-Potassium level")
e_nak = Entry(f5)
e_nak.place(x = 165,y = 162,width=60,height=22)
b = Button(f5, text='Predict drug',style = 'W.TButton',command= lambda :predict(e_age.get(),sex,bp,c,e_nak.get())).place(relx = 0.5, rely = 0.53, anchor = 'center')
bd = Button(f5, text='Load current dataset',style = 'W.TButton',command= lambda :load()).place(relx = 0.7, rely = 0.81, anchor = 'center')
b9 = Button(f5, text='Back to Home',style = 'W.TButton',command= lambda :home_back()).place(relx = 0.37, rely = 0.85, anchor = 'se')
b8 = Button(f5, text='Clear all',style = 'W.TButton',command= lambda :reset()).place(relx = 0.94, rely = 0.1, anchor = 'ne')
b7 = Button(f5, text='Check accuracy',style = 'W.TButton',command= lambda :accuracy()).place(relx = 0.89, rely = 0.565, anchor = 'se')
canvas2.create_text(200,170,fill="black",font="Calibri 11 bold",text="Import your .csv data file below")
canvas2.create_text(200,100,fill="darkred",font="Arial 10 bold",text="Note: File should have the first columns exactly as specified:")
canvas2.create_text(200,130,fill="darkblue",font="Arial 12 bold",text="Age, Sex, BP, Cholesterol, Na_to_K, Drug")
b = Button(f3, text='Browse file',style = 'W.TButton',command= lambda :dfimport()).place(relx = 0.5, rely = 0.5, anchor = 'center')
bb = Button(f3, text='Back',style = 'W.TButton',command= lambda : read_back()).place(relx = 0.4, rely = 0.8, anchor = 'se')
bback = Button(f4, text='Back',style = 'W.TButton',command= lambda : train_back()).place(relx = 0.4, rely = 0.8, anchor = 'se')
b = Button(f4, text='Train',style = 'W.TButton',command= lambda :train()).place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas3.create_text(190,80,fill="black",font="Arial 13 bold",text="Training")
canvas1.create_text(120,80,fill="black",font="Arial 13 bold",text="Choose a dataset")
v = IntVar() 
Radiobutton(f2, text='Use patient dataset for inbuilt disease prediction',variable=v, value=1).place(relx = 0.49, rely = 0.4, anchor = 'center') 
Radiobutton(f2, text='Use patient dataset for custom disease prediction',variable=v, value=2).place(relx = 0.5, rely = 0.5, anchor = 'center') 
b2 = Button(f2, text='Back',style = 'W.TButton',command= lambda : f1.tkraise()).place(relx = 0.4, rely = 0.8, anchor = 'se')
b3 = Button(f2, text='Next',style = 'W.TButton',command=lambda : butpress(v)).place(relx = 0.8, rely = 0.8, anchor = 'se')
canvas=Canvas(f1,width=400,height=400)
image=ImageTk.PhotoImage(Image.open("phar.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.place(relx = 0.5, rely = 0.5, anchor = 'center')
canvas.create_text(200,10,fill="black",font="Arial 11 ",text="Hello, guest")
canvas.create_text(200,170,fill="darkblue",font="Arial 14 bold ",text="MedPred")
canvas.create_text(200,190,fill="black",font="Arial 11 bold ",text="Personalized Drug Prediction Service")
b1 = Button(f1, text='Go!', style = 'W.TButton',command=lambda :f2.tkraise()).place(relx = 0.75, rely = 0.75, anchor = 'se')
b_about = Button(f1, text='About the app', style = 'W.TButton',command=lambda :about()).place(relx = 0.1, rely = 0.9, anchor = 'sw')
f1.tkraise()
root.mainloop() 
