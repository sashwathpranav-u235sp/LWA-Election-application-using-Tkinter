import csv as v
#to announce results
information=open("info.csv",'r')
a=v.reader(information)
results=[]
for i in a:
    results.append(i)
res=results[-2]
for i in res:
    print(i.strip())
    if i==res[-2]:
        break
information.close()




