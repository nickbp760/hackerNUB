# for @@@+@@@=@@@@ with 0-9 is different
f = open("wk.txt")
i=0
for x in f:
    angka1="".join(x[0:3:1])
    angka2="".join(x[3:6:1])
    angka3="".join(x[6:10:1])
    a1=int(angka1)
    a2=int(angka2)
    a3=int(angka3)
    if(a1+a2==a3):
       i=i+1
       print(a1,"+",a2,"=",a3,"      ",i)
