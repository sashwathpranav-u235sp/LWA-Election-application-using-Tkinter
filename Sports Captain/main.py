from tkinter import *
from tkinter import messagebox
from turtle import screensize
from PIL import ImageTk,Image
import csv as v
import datetime as dt
information=open("info.csv",'a+')
ap=v.writer(information)
root=Tk()
total_num_of_votes=230
candidate_info={1:'K Harjeeth',2:'Kavin Chandramohan',3:"Harish",4:'Aryan Nama',5:'Sanjay Varghese',6:"Sarvesh",7:"Subhasmita K"}
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
v=IntVar()
v.set(0)
def showvar(number):
    print(number)

def submit():
    global c1
    global c2
    global c3
    global c4
    global c5
    global c6
    global c7
    a=v.get()
    if a==0:
        messagebox.showwarning("Warning!","You have not selected an option\nPlease select an option to cast your vote")
    else:
        response=messagebox.askyesno("LWA Voting system","Would you like to confirm your choice?\nNote: Once you confirmed your choice, your choice cannot be reverted")
        if response==1:
            if a==1:
                c1+=1
            elif a==2:
                c2+=1
            elif a==3:
                c3+=1
            elif a==4:
                c4+=1
            elif a==5:
                c5+=1
            elif a==6:
                c6+=1
            elif a==7:
                c7+=1
            ap.writerow([f" {candidate_info[1]}:{c1}",f" {candidate_info[2]}:{c2}",f" {candidate_info[3]}:{c3}",f" {candidate_info[4]}:{c4}",f" {candidate_info[5]}:{c5}",f" {candidate_info[6]}:{c6}",f" {candidate_info[7]}:{c7}",f" Total:{c1+c2+c3+c4+c5+c6+c7}",f" Time Stamp:{dt.datetime.now()}"])
            v.set(0)

def exit():
    response=messagebox.askyesno("LWA Voting System","Are you sure you want to exit?\nAll existing data will be lost")
    if response==1:
        ap.writerow(["-------------------------------------EXISTING SESSION ENDS HERE-------------------------------------------------------"])
        root.quit()

    
txt=Label(root,text="Please click on the desired radio button to cast your vote").grid(row=0,columnspan=7)
imgs=[]
for i in range(0,7):
    a=Image.open(f"pictures\\{i+1}.png")
    ra=a.resize((200,200))
    img=ImageTk.PhotoImage(ra)
    imgs.append(img)
    lbl=Label(root,image=imgs[-1])
    lbl.grid(row=1,column=i)

#Not recommended for displaying multiple images at a time
#a1=Label(root,image=ImageTk.PhotoImage(Image.open(r"D:\LWA Election Systems\Pupil Captain\pictures\on.png")))
#a2=Label(root,image=ImageTk.PhotoImage(Image.open(r"D:\LWA Election Systems\Pupil Captain\pictures\tw.png")))
#a3=Label(root,image=ImageTk.PhotoImage(Image.open(r"D:\LWA Election Systems\Pupil Captain\pictures\thr.png")))
#a4=Label(root,image=ImageTk.PhotoImage(Image.open(r"D:\LWA Election Systems\Pupil Captain\pictures\fr.png")))
#a5=Label(root,image=ImageTk.PhotoImage(Image.open(r"D:\LWA Election Systems\Pupil Captain\pictures\fv.png")))
#a1.grid(row=1,column=0)
#a2.grid(row=1,column=1)
#a3.grid(row=1,column=2)
#a4.grid(row=1,column=3)
#a5.grid(row=1,column=4)
Radiobutton(root,text=candidate_info[1],variable=v,value=1,command=lambda:showvar(1),anchor='s').grid(row=2,column=0)
Radiobutton(root,text=candidate_info[2],variable=v,value=2,command=lambda:showvar(2),anchor='s').grid(row=2,column=1)
Radiobutton(root,text=candidate_info[3],variable=v,value=3,command=lambda:showvar(3),anchor='s').grid(row=2,column=2)
Radiobutton(root,text=candidate_info[4],variable=v,value=4,command=lambda:showvar(4),anchor='s').grid(row=2,column=3)
Radiobutton(root,text=candidate_info[5],variable=v,value=5,command=lambda:showvar(5),anchor='s').grid(row=2,column=4)
Radiobutton(root,text=candidate_info[6],variable=v,value=6,command=lambda:showvar(6),anchor='s').grid(row=2,column=5)
Radiobutton(root,text=candidate_info[7],variable=v,value=7,command=lambda:showvar(7),anchor='s').grid(row=2,column=6)
confirm_button=Button(root,text="Submit",padx=30,pady=40,command=submit,bg='red',fg='white').grid(row=3,columnspan=7)
exit_button=Button(root,text="Exit program",padx=30,pady=30,fg='white',bg='red',command=exit).grid(row=3,column=4,columnspan=7)

root.mainloop()
information.close()