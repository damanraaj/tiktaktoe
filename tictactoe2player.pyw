from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *

player1=['Player 1','  X  ']
player2=['Player 2','  O  ']
player3=['Computer',None]
winner=0
emptybox='       '
def newname(x):
   global player1,player2
   nm=askstring("Change name","Enter new name : ")
   if nm:
      if x==1:
         p1.config(text=nm)
         player1[0]=nm
      elif x==2:
         p2.config(text=nm)
         player2[0]=nm
   
curr=1
res=[0,0,0,0,0,0,0,0,0]
def result():
   global winner
   if res[0]==curr:
      if res[1]==res[2] and res[1]==res[0]:winner=curr
      if res[3]==res[6] and res[3]==res[0]:winner=curr
      if res[4]==res[8] and res[4]==res[0]:winner=curr
   if res[1]==curr:
      if res[4]==res[7] and res[4]==res[1]:winner=curr
   if res[2]==curr:
      if res[4]==res[6] and res[4]==res[2]:winner=curr
      if res[5]==res[8] and res[5]==res[2]:winner=curr
   if res[3]==curr:
      if res[4]==res[5] and res[4]==res[3]:winner=curr
   if res[8]==curr:
      if res[6]==res[7] and res[6]==res[8]:winner=curr
   return winner
root=Tk()
root.title("TicTacToe")

main=Frame(root)
main.pack(expand=YES,fill=BOTH)
Label(main,text="TicTacToe",font=('times',32),fg='blue').pack(side=TOP,anchor=N,expand=YES,fill=BOTH)

game=Frame(main)
game.pack(side=LEFT,expand=YES)

def clear(self):
   self.config(text=emptybox,bg='white',state='normal')

def reset():
   global res
   global curr
   global winner
   p2.config(bg='red',state='normal')
   p1.config(bg='cyan',state='normal')
   curr=1
   winner=0
   res=[0,0,0,0,0,0,0,0,0]
   for b in bx:
      clear(b)

def resetmsg():
   if askokcancel("Reset?","Start new game?"):
      reset()
   
def endprg():
    if askyesno("Quit?","Do you really want to quit?"):
        root.destroy()
    else:
       pass

def row(x):
   x=Frame(game)
   x.pack(side=TOP)
   return x

def col(x,parent):
   x=Frame(parent)
   x.pack(side=LEFT,expand=YES,fill=BOTH)
   return x
   
def box(x,parent):
   x=Button(parent,text=emptybox,bd=0,command=lambda:press(x),bg='white',font=('times',20))
   x.pack(expand=YES,fill=BOTH,padx=10,pady=10)
   return x

r1=r2=r3=0
r1=row(r1)
r2=row(r2)
r3=row(r3)
r11=r12=r13=0
r11=col(r11,r1)
b11=0
b11=box(b11,r11)
r12=col(r12,r1)
b12=0
b12=box(b12,r12)
r13=col(r13,r1)
b13=0
b13=box(b13,r13)

r21=r22=r23=0
r21=col(r21,r2)
b21=0
b21=box(b21,r21)
r22=col(r22,r2)
b22=0
b22=box(b22,r22)
r23=col(r23,r2)
b23=0
b23=box(b23,r23)

r31=r32=r33=0
r31=col(r31,r3)
b31=0
b31=box(b31,r31)
r32=col(r32,r3)
b32=0
b32=box(b32,r32)
r33=col(r33,r3)
b33=0
b33=box(b33,r33)


bx=[b11,b12,b13,b21,b22,b23,b31,b32,b33]

def turn():
   global curr
   if curr==1: curr=2
   else: curr=1
   if 0 not in res:tied()
   

def press(self):
   global curr,winner
   if res[bx.index(self)]==0:
      p2.config(bg='red')
      p1.config(bg='cyan')
      if curr==1:
         self.config(text=player1[1],bg='cyan')
      elif curr==2:
         self.config(text=player2[1],bg='red')
      res[bx.index(self)]=curr
      if result(): won()
      else: turn()
      
def tied():
   tie=Toplevel(root)
   Frame(tie)
   Label(tie,text='No winner').pack()
   p1.configure(state='disable')
   p2.configure(state='disable')
   for b in bx:
      b.configure(state='disable')
   def newgame():
      reset()
      tie.destroy()
   Button(tie,text='Start new game?',command=newgame).pack()
   Button(tie,text='Exit',command=lambda:root.destroy()).pack()

def won():
   gamewon=Toplevel(root)
   Frame(gamewon).pack(side=TOP)
   p1.configure(state='disable')
   p2.configure(state='disable')
   for b in bx:
      b.configure(state='disable')
   def newgame():
      reset()
      gamewon.destroy()
   if winner==1:
      Label(gamewon,text=player1[0]+' won!!').pack()
   else:Label(gamewon,text=player2[0]+' won!!').pack()
   newgamebutt=Button(gamewon,text='Start new game?',command=newgame)
   
   newgamebutt.pack()
   newgamebutt.focus()
   Button(gamewon,text='Exit',command=lambda:root.destroy()).pack()
   gamewon.focus()
   
menu=Frame(main)
menu.pack(expand=YES,side=RIGHT)
p1=Button(menu,text="Player 1",command=lambda:newname(1),bd=0,pady=5,padx=10,bg='cyan',font=('arial',14))
p1.pack(side=TOP,anchor=N)
p2=Button(menu,text="Player 2",command=lambda:newname(2),bd=0,pady=5,padx=10,bg='red',font=('arial',14))
p2.pack(side=TOP,anchor=N)
Label(menu,text="\n").pack()
Button(menu,text="Quit",command=endprg,font=('arial',16)).pack(side=BOTTOM,anchor=S)
Button(menu,text="Reset",command=resetmsg,font=('arial',16)).pack(side=BOTTOM,anchor=N)
root.mainloop()
