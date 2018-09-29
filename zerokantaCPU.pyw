from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
from random import choice
from unionintersection import intersect

yourname='You'
cpu=2
you=1
emptybox='       '
winner=0
curr=1
res=[0,0,0,0,0,0,0,0,0]

def newname():
   global yourname
   nm=askstring("Change name","Enter new name : ")
   if nm!=None:
      yourname=nm

def clear(label):
   label.config(text=emptybox,bg='white',state='normal')

def resetmsg():
   if askokcancel("Reset?","Start new game?"):
      reset()
   
def endprg():
    if askyesno("Quit?","Do you really want to quit?"):
       root.quit
       root.destroy()
    else:
       pass

def result(res,real=True):
   if real:
      global winner
   else:
      winner=0
   
   if res[0]==curr:
      if res[1]==res[0] and res[2]==res[0]:winner=curr
      if res[3]==res[0] and res[6]==res[0]:winner=curr
      if res[4]==res[0] and res[8]==res[0]:winner=curr
   if res[1]==curr:
      if res[4]==res[1] and res[7]==res[1]:winner=curr
   if res[2]==curr:
      if res[4]==res[2] and res[6]==res[2]:winner=curr
      if res[5]==res[2] and res[8]==res[2]:winner=curr
   if res[3]==curr:
      if res[4]==res[3] and res[5]==res[3]:winner=curr
   if res[8]==curr:
      if res[6]==res[8] and res[7]==res[8]:winner=curr
   return winner

def reset():
   global res
   global curr
   global winner
   curr=1
   winner=0
   res=[0,0,0,0,0,0,0,0,0]
   for b in bx:
      clear(b)

def cpumakesmove():
   global res
   global winner
   board=res[:]
   move=-1
   cpulose=[]
   print(res[:3])
   print(res[3:6])
   print(res[6:9])
   print('cpu begins')
   posiblemoves=list(range(9))
   posiblemoves=[x for x in posiblemoves if board[x]==0]
   print('posible moves',posiblemoves)
   if not posiblemoves:
      return
   else:
      for i in posiblemoves:
      #CPU makes the winning move
         board[i]=2
         if result(board,False)==2:
            winner=2
            move=i
            board[i]=0
            return(move)
      #Check if CPU is Losing
         board[i]=1
         if result(board,False)==1:
            print("inside cpu lose")
            move=i
            cpulose.append(move)

         board[i]=0
      #CPU prevents losing
      if cpulose!=[]:
         print("you win at position(s)")
         print(cpulose)
         move=choice(cpulose)
         return move
      
      #selection corners>edge>center
      if intersect(posiblemoves,(0,2,6,8)):
         move=choice(intersect(posiblemoves,(0,2,6,8)))
      elif intersect(posiblemoves,(1,3,5,7)):
         move=choice(intersect(posiblemoves,(1,3,5,7)))
      else:
         move=choice(posiblemoves)
      return move

         
   
root=Tk()
root.title("TicTacToe")
Label(root,text="TicTacToe",font=('times',32),fg='blue').pack(side=TOP,anchor=N,expand=YES,fill=BOTH)
main=Frame(root)
main.pack(side=LEFT,expand=YES)
      
def row(x):
   x=Frame(main)
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
dashboard=Button(main,text='You are X',font=('times',15),fg='red',bd=0,command=newname)
dashboard.pack(side=BOTTOM,anchor=N,expand=YES,fill=BOTH)
bx=[b11,b12,b13,b21,b22,b23,b31,b32,b33]

def turn():
   global curr
   if curr==1:
      curr=2
   else:
      curr=1
   if 0 not in res:tied()
   

def press(self):
   global curr,winner
   if res[bx.index(self)]==0:
      if curr==1:
         print(res[:3])
         print(res[3:6])
         print(res[6:9])
         print('press',bx.index(self))
         print()
         self.config(text='  X  ',bg='red')
         res[bx.index(self)]=curr
         if result(res): won()      
         else:
            turn()
            cpumove=cpumakesmove()
            print('cpu move',cpumove)
            if cpumove!=None:
               res[cpumove]=2
               bx[cpumove].config(text='  O  ',bg='cyan')
            print(res[:3])
            print(res[3:6])
            print(res[6:9])
            print()
            if result(res): won()
            else:turn()
      
def tied():
   tie=Toplevel(root)
   Frame(tie)
   Label(tie,text='No winner').pack()
   def newgame():
      reset()
      tie.destroy()
   Button(tie,text='Start new game?',command=newgame).pack()
   Button(tie,text='Exit',command=lambda:root.destroy()).pack()

def won():
   gamewon=Toplevel(root)
   Frame(gamewon).pack(side=TOP)
   
   def newgame():
      reset()
      gamewon.destroy()
   if winner==1: Label(gamewon,text=yourname+' won!!').pack()
   else:Label(gamewon,text="GAME OVER").pack()
   Button(gamewon,text='Start new game?',command=newgame).pack()
   Button(gamewon,text='Exit',command=lambda:root.destroy()).pack()
   
root.mainloop()
