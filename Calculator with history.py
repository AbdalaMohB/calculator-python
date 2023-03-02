from tkinter import *
from math import *
parent = Tk()
parent.geometry('400x350')
c = Canvas(parent,bg = "black",height = "350",width='400')  
  

c.pack()
parent.title("Calculator")
xax=''
yay=xax
history=[]
hvar=-1
screen=Label(parent,text=xax,anchor=W)
screen.place(x=10,y=12,width=200)
class func:
    def __init__(self):
        y=2
    def number(self,num):
        global xax
        xax=xax+num
        screen['text']=xax
    def plus(self):
        global xax
        xax=xax+'+'
        screen['text']=xax
    def multi(self):
        global xax
        xax=xax+'*'
        screen['text']=xax
    def div(self):
        global xax
        xax=xax+'/'
        screen['text']=xax
    def minus(self):
        global xax
        xax=xax+'-'
        screen['text']=xax
    def equal(self):
        global xax
        global history
        global yay
        try:
            yay=xax
            if len(history)>5:
                history.pop(0)
            if '=' in xax:
                screen['text']=xax
            elif eval(xax)==int(eval(xax)):
                xax=eval(xax)
                xax=str(int(xax))
                screen['text']=xax
                history.append(yay+'='+xax)
            else:
                xax=eval(xax)
                xax=str(xax)
                screen['text']=xax
                history.append(yay+'='+xax)
        except:
            screen['text']=xax
    def clear(self):
        global xax
        xax=''
        screen['text']=xax
    def par1(self):
        global xax
        xax=xax+'('
        screen['text']=xax
    def par2(self):
        global xax
        xax=xax+')'
        screen['text']=xax
    def point(self):
        global xax
        xax=xax+'.'
        screen['text']=xax
    def dele(self):
        global xax
        xax=list(xax)
        if len(xax)==0:
            xax.append('')
            xax=''.join([str(i) for i in xax])
            screen['text']=xax
        elif len(xax)>0:
            xax.pop(-1)
            xax=''.join([str(i) for i in xax])
            screen['text']=xax
    def hispv(self):
        global xax
        global history
        global hvar
        if -hvar<len(history):
            hvar-=1
            xax=history[hvar]
            screen['text']=xax
        else:
            screen['text']=xax
    def hisfr(self):
        global xax
        global history
        global hvar
        if hvar<-1:
            hvar+=1
            xax=history[hvar]
            screen['text']=xax
        else:
            screen['text']=xax
calc=func()
numcol='Orange'
symcol='White'
xcoor=0
ycoor=0
b1=Button(parent,text=1,command=lambda:calc.number('1'),bg=numcol).place(x=xcoor+10,y=ycoor+36,width=25)
b2=Button(parent,text=2,command=lambda:calc.number('2'),bg=numcol).place(x=xcoor+36,y=ycoor+36,width=25)
b3=Button(parent,text=3,command=lambda:calc.number('3'),bg=numcol).place(x=xcoor+62,y=ycoor+36,width=25)
b4=Button(parent,text=4,command=lambda:calc.number('4'),bg=numcol).place(x=xcoor+10,y=ycoor+62,width=25)
b5=Button(parent,text=5,command=lambda:calc.number('5'),bg=numcol).place(x=xcoor+36,y=ycoor+62,width=25)
b6=Button(parent,text=6,command=lambda:calc.number('6'),bg=numcol).place(x=xcoor+62,y=ycoor+62,width=25)
b7=Button(parent,text=7,command=lambda:calc.number('7'),bg=numcol).place(x=xcoor+10,y=ycoor+88,width=25)
b8=Button(parent,text=8,command=lambda:calc.number('8'),bg=numcol).place(x=xcoor+36,y=ycoor+88,width=25)
b9=Button(parent,text=9,command=lambda:calc.number('9'),bg=numcol).place(x=xcoor+62,y=ycoor+88,width=25)
b0=Button(parent,text=0,command=lambda:calc.number('0'),bg=numcol).place(x=xcoor+10,y=ycoor+114,width=25)
bp=Button(parent,text='+',command=calc.plus).place(x=xcoor+92,y=ycoor+36,width=25)
be=Button(parent,text='=',command=calc.equal).place(x=xcoor+92,y=ycoor+139,width=25)
bmi=Button(parent,text='-',command=calc.minus).place(x=xcoor+92,y=ycoor+62,width=25)
bd=Button(parent,text='/',command=calc.div).place(x=xcoor+92,y=ycoor+114,width=25)
bmu=Button(parent,text='*',command=calc.multi).place(x=xcoor+92,y=ycoor+88,width=25)
bc=Button(parent,text='Clr',command=calc.clear).place(x=xcoor+122,y=ycoor+36,width=25)
bpr1=Button(parent,text='(',command=calc.par1).place(x=xcoor+122,y=ycoor+62,width=25)
bpr2=Button(parent,text=')',command=calc.par2).place(x=xcoor+122,y=ycoor+88,width=25)
bpnt=Button(parent,text='.',command=calc.point).place(x=xcoor+122,y=ycoor+114,width=25)
bdel=Button(parent,text='<-',command=calc.dele).place(x=xcoor+154,y=ycoor+36,width=25)
bpv=Button(parent,text='Prv',command=calc.hispv).place(x=xcoor+154,y=ycoor+62,width=25)
bpv=Button(parent,text='Nxt',command=calc.hisfr).place(x=xcoor+154,y=ycoor+88,width=25)
parent.mainloop()
