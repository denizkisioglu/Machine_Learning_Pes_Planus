import pandas as pd
import numpy as np
df=pd.read_csv("Finalcapstonedata2.csv")
from sklearn.naive_bayes import GaussianNB
X=df.drop(["Disesase"], axis = 1)
y=df["Disesase"]
bayes = GaussianNB()
bayes.fit(X,y)
from tkinter import *
from tkinter import messagebox

pencere=Tk()
pencere.title("Pes Planus")
pencere.geometry("1300x600+100+100")
#pencere.resizable(False,False) 
pencere.configure(background="antiquewhite3")

saklama=""

icerik = StringVar()

def temizle():
    global saklama
    saklama = " " 
    icerik.set(saklama)
    
    parametre1.delete(0,"end")
    parametre2.delete(0,"end")
    parametre3.delete(0,"end")
    parametre4.delete(0,"end")
    parametre5.delete(0,"end")
    parametre6.delete(0,"end")
    parametre7.delete(0,"end")
    parametre8.delete(0,"end")
    


def sonucgoster(): 
   global saklama
   if len(    parametre1.get() 
          and parametre2.get() 
          and parametre3.get() 
          and parametre4.get() 
          and parametre5.get() 
          and parametre6.get() 
          and parametre7.get()
          and parametre8.get()
          )== 0:
       messagebox.showinfo(title="Unsuccessful", message="Please fill in all the blanks")
   else:
       if (parametre1.get().replace('.', '', 1).replace('-', '', 1).isdigit() 
           and parametre2.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre3.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre4.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre5.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre6.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre7.get().replace('.', '', 1).replace('-', '', 1).isdigit()
           and parametre8.get().replace('.', '', 1).replace('-', '', 1).isdigit()):
           
           
        yeniveri = [[parametre1.get(),parametre2.get(),parametre3.get(),parametre4.get(),parametre5.get(),parametre6.get(),parametre7.get(),parametre8.get()]]
        yeniveri2 = np.array(yeniveri, dtype=float)
        pred=bayes.predict(yeniveri2)
        saklama=str(pred)
        icerik.set(saklama)
          
       else:
           messagebox.showinfo(title="Unsuccessful", message="Please enter only NUMBER") 


label=Label(text="RESULT",font= "arial 20 bold",bg="antiquewhite3",)
label.place(x=980,y=160)
sonuc=Entry(pencere, state="disabled", textvariable=icerik, font= "arial 30 bold", disabledforeground="red", disabledbackground="yellow", justify="center", bd=10, )
sonuc.place(x=900,y=200,width=280,height=80)

buton=Button(pencere, text="Show Result",font="arial 9 bold", bd=5, bg="aqua",command=sonucgoster)
buton.place(x=990,y=300,width=100,height=50)

buton2=Button(pencere, text="Reset",font="arial 9 bold", bd=5, bg="aqua",command=temizle)
buton2.place(x=1015,y=370,width=50,height=50)

label1=Label(text="Weight",font= "arial 10 bold",bg="antiquewhite3", )
label1.place(x=100,y=120)
parametre1=Entry(pencere,font= "arial 10 bold", bg="aquamarine3", justify="center", bd=5,)
parametre1.place(x=100,y=150,width=100,height=50)

label2=Label(text="BMI",font= "arial 10 bold",bg="antiquewhite3", )
label2.place(x=250,y=120)
parametre2=Entry(pencere,font= "arial 10 bold",   bg="aquamarine3", justify="center", bd=5,)
parametre2.place(x=250,y=150,width=100,height=50)

label3=Label(text="ML_Mean_OS",font= "arial 10 bold",bg="antiquewhite3", )
label3.place(x=400,y=120)
parametre3=Entry(pencere,font= "arial 10 bold",   bg="aquamarine3", justify="center", bd=5,)
parametre3.place(x=400,y=150,width=100,height=50)

label4=Label(text="RMS_Radius_OF",font= "arial 10 bold",bg="antiquewhite3", )
label4.place(x=550,y=120)
parametre4=Entry(pencere,font= "arial 10 bold",   bg="aquamarine3", justify="center", bd=5,)
parametre4.place(x=550,y=150,width=100,height=50)

label5=Label(text="ML_Mean_CS",font= "arial 10 bold",bg="antiquewhite3", )
label5.place(x=100,y=220)
parametre5=Entry(pencere,font= "arial 10 bold", bg="aquamarine3", justify="center", bd=5,)
parametre5.place(x=100,y=250,width=100,height=50)

label6=Label(text="Mean_Dist_CS",font= "arial 10 bold",bg="antiquewhite3", )
label6.place(x=250,y=220)
parametre6=Entry(pencere,font= "arial 10 bold",   bg="aquamarine3", justify="center", bd=5,)
parametre6.place(x=250,y=250,width=100,height=50)

label7=Label(text="ML_Mean_CF",font= "arial 10 bold",bg="antiquewhite3", )
label7.place(x=400,y=220)
parametre7=Entry(pencere,font= "arial 10 bold",   bg="aquamarine3", justify="center", bd=5,)
parametre7.place(x=400,y=250,width=100,height=50)

label8=Label(text="Mean_Dist_CF",font= "arial 10 bold",bg="antiquewhite3", )
label8.place(x=550,y=220)
parametre8=Entry(pencere,font= "arial 10 bold",  bg="aquamarine3", justify="center", bd=5,)
parametre8.place(x=550,y=250,width=100,height=50)

pencere.mainloop()