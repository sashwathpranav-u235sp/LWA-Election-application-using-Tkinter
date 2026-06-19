import csv as v
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#to announce results
information=open("info.csv",'r')
a=v.reader(information)
terminating_statement=["-------------------------------------EXISTING SESSION ENDS HERE-------------------------------------------------------"]
l=[]
n=[]
result_set=[]
r1=0
r2=0
r3=0
r4=0
r5=0
total_votes=0
index=1
candidate_info={1:'Hrishikesh Varahan',2:'Jeevitesh',3:"Manish",4:'Thayanitha',5:'Muhilan'}
candidate_results={"Hrishikesh Varahan":0,"Jeevitesh":0,"Manish":0,"Thayanitha":0,"Muhilan":0}

for i in a:
    l.append(i)

for i in l:
    a=l.index(i)
    if l[a+1]==[] and l[a+2]==terminating_statement:
        n.append(i)
for i in n:
    for j in i:
        number=int(j.strip()[-1])
        candidate_results[candidate_info[index]]+=number
        index+=1
        if index>len(candidate_info):
            index=1
            break
for i in n:
    votes=int(i[-2].strip()[-1])
    print(votes)
    total_votes+=votes
max=candidate_results["Hrishikesh Varahan"]
maxname=candidate_info[1]
for i in candidate_results:
    if candidate_results[i]>max:
        max=candidate_results[i]
        maxname=i
result_set.append([maxname,max])
for i in candidate_results:
    if max==candidate_results[i] and i!=maxname:
        result_set.append([i,candidate_results[i]])
string=""
tot=f"Total votes: {total_votes}"
for i in result_set:
    string+=f"{i[0]} : {i[1]} votes\n"

result_display=Label(root,text="The winner(s) is/are: \n"+string+tot)
result_display.pack()

root.mainloop()
information.close()


















