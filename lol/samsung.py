
import os
import sys

def harga(a,b,c,d,menu,total,n,loop):
 for i in range (menu):
    #print(i,n)
    m=[]
    totalnow=total
    for x in range (len(n)):
         m.append(n[x])
    if(a>=d[i][0] and b>=d[i][1] and c>=d[i][2] and n[i]<=loop):  
         x=a-d[i][0]
         y=b-d[i][1]
         z=c-d[i][2]
         totalnow=totalnow+d[i][3]
	 #print(x,y,z,i,n,totalnow)
         m[i]=m[i]+1
	 #print(m,n)
         harga(x,y,z,d,menu,totalnow,m,loop)
         hasil.append(totalnow)
"""
variabel
loop=1#maksimal banyaknya pemesanan
menu=3

a=3
b=2
c=7
n= [1,1,1] #banyaknya pemesanan

d= [[1,2,3,22],#bahan menu1
    [2,1,1,15],#bahan menu2
    [1,1,1,18]]#bahan menu3
"""
total=0
hasil=[]
the_string = raw_input()
loop, menu = the_string.split()
menu = int (menu)
loop = int (loop)
the_string = raw_input()
a, b, c = the_string.split()
a = int (a)
b = int (b)
c = int (c)
n=[]
for z in range(menu):
    n.append(1)
d= [[1,2,3,22],#bahan menu1
    [2,1,1,15],#bahan menu2
    [1,1,1,18]]#bahan menu3
harga(a,b,c,d,menu,total,n,loop)
print(max(hasil))
