import math
import random
f = open ('iris.data','r+')

def filetolist (ar):
    nop =[]
    bbv = []

    for line in ar:
        bbv =[]
        for b in range (0,13,4):
            argoman = line[b:b+3] 
            strin = float (argoman)
  	    bbv.append(strin)
        nop.append(bbv)
    return nop

  
mylist2 = filetolist (f)

avg1=mylist2[0]
avg2=mylist2[1]
avg3=mylist2[2]
i=150
mylist=[]
while len(mylist2):#confect now list
      indx = int ((random.random())*(len(mylist2)))
      mylist.append(mylist2[indx])
      del mylist2[indx]
      
br = br1 = br2 = br3 = 0
an = an1 = an2 =0
k=0


x0=x1=x2=x3=0

for n in mylist:#add index 4

    n.append(0)


def antkhab(ml):#function chose 
    wh=0
    while wh<2:
          ind = int ((random.random())*(149))
          ant = mylist[ind]
          if ant[4] == 0:
             break
    return ant


def an (nn ,av ) :
    x0=((nn[0]-av[0])**2 / nn[0])**2 
    x1=((nn[1]-av[1])**2 / nn[1])**2 
    x2=((nn[2]-av[2])**2 / nn[2])**2 
    x3=((nn[3]-av[3])**2 / nn[3])**2 
    ano=math.sqrt(x0+x1+x2+x3)
    return ano

while br<10:
      for n in mylist:

          an1=an (n,avg1) 
          an2=an (n,avg2) 
          an3=an (n,avg3) 
        

          if an1<an2 and an1<an3:
             n[4]=1
          if an2<an1 and an2<an3:
             n[4]=2
          if an3<an1 and an3<an2:
             n[4]=3 
      aa=a0=a1=a2=a3=0
      bb=b0=b1=b2=b3=0
      cc=c0=c1=c2=c3=0         
      for m in mylist:
          if m[4]==1:
             a0=a0+m[0]
             a1=a1+m[1]
             a2=a2+m[2]
             a3=a3+m[3]
             aa=aa+1

          if m[4]==2:
             b0=b0+m[0]
             b1=b1+m[1]
             b2=b2+m[2]
             b3=b3+m[3]  
             bb=bb+1

          if m[4]==3:
             c0=c0+m[0]
             c1=c1+m[1]
             c2=c2+m[2]
             c3=c3+m[3]
             cc=cc+1
 
      print aa,cc,bb

      try :
          avg1=[a0/aa,a1/aa,a2/aa,a3/aa] 
      except :
             avg1= antkhab(mylist)
      try :
          avg2=[b0/bb,b1/bb,b2/bb,b3/bb] 
      except :
             avg2= antkhab(mylist)
      try :
          avg3=[c0/cc,c1/cc,c2/cc,c3/cc]
      except :
             avg3= antkhab(mylist)


     
      k=k+1
      if br1==avg1[0] and br2==avg2[0] and br3==avg3[0]:
         break
      br1=avg1[0]
      br2=avg2[0]
      br3=avg3[0]



iii=0.0
f = open ('iris.data','r+')
anallist=filetolist (f)

 
def selectin(anal ,nam):   
    for exa in mylist:
        if exa[0]==anal[0] and exa[1]==anal[1] and exa[2]==anal[2] and exa[3]==anal[3]:
           indn=exa[4]
           break
    for e1 in anallist[nam:nam+50]:
        e1.append(indn)


anal1 = anallist[0]
anal2 = anallist[50]
anal3= anallist[100]
selectin (anal1,0)
selectin (anal2,50)
selectin (anal3,100)

for rea in anallist:
    for ex1 in mylist:
        if ex1[0]==rea[0] and ex1[1]==rea[1] and ex1[2]==rea[2] and ex1[3]==rea[3] and ex1[4]==rea[4]:
	   print ex1 , rea 
           iii=iii+1
           break
cent=(iii/len(mylist))*100
print cent,'%', '     k=',k


