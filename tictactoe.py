
import random
#matrix printer
import tkinter.simpledialog
import tkinter.messagebox
def printmat(*m):

#labeler
    for i in range(0,3):

        t.insert(END, m[i] + '\t')
    t.insert(END,  '\n')
    for i in range(3,6):

       t.insert(END, m[i] + '\t')
    t.insert(END,  '\n')
    for i in range(6,9):

       t.insert(END, m[i] + '\t')
    t.insert(END,  '\n')
    t.insert(END,'_______________________\n')
def clr():
    t.delete('1.0', END)



#play button function
def play():

    while 1:
        tkinter.messagebox.showinfo("","the game begins")
        m=['*','*','*','*','*','*','*','*','*'];
        count=0;

        while 1:


#player one's turn

            while 1:


                printmat(*m)

                x=int(tkinter.simpledialog.askinteger('playerone','number'))-1;
                if m[x]!='x' and m[x]!='o':
                        m[x]='x';
                        count+=1;
                        clr()
                        break;

                else:
                    tkinter.messagebox.showerror('!!!!!!!!','UCANTDOTHAT!')

#checking if
#diagonal checking
            if m[4]==m[0]and m[4]==m[8]:
                if m[4]=='x':
                    printmat(*m);

                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[4]==m[6]and m[4]==m[2]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
#row and column checkings
    #1,1
            if m[0]==m[1] and m[0]==m[2]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[0]==m[3] and m[0]==m[6]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
    #2,2
            if m[3]==m[4] and m[3]==m[5]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[1]==m[4] and m[1]==m[7]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
    #3,3
            if m[6]==m[7] and m[6]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[2]==m[5] and m[2]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
#draw match scenario
            if count==9:
                printmat(*m);
                tkinter.messagebox.showinfo('!!!!!!!!','ITISADRAW')
                break;
#player two's turn
            while 1:


#diagone
                if m[4]==m[0]and m[8]=='*' and m[4]!='*' :
                    m[8]='o';
                    count+=1;
                    clr()
                    break;
                if m[4]==m[8]and m[0]=='*'and m[4]!='*':
                    m[0]='o';
                    count+=1;
                    clr()
                    break;
                if m[8]==m[0]and m[4]=='*' and m[0]!='*':
                    m[4]='o';
                    count+=1;
                    clr()
                    break;
                #diag two
                if m[4]==m[2]and m[6]=='*'and m[4]!='*' :
                    m[6]='o';
                    count+=1;
                    clr()
                    break;
                if m[4]==m[6]and m[2]=='*' and m[4]!='*':
                    m[2]='o';
                    count+=1;
                    clr()
                    break;
                if m[6]==m[2]and m[4]=='*' and m[2]!='*':
                    m[4]='o';
                    count+=1;
                    clr()
                    break;
                #column one
                if m[0]==m[3]and m[6]=='*'and m[0]!='*':
                    m[6]='o';
                    count+=1;
                    clr()
                    break;
                if m[0]==m[6]and m[3]=='*'and m[0]!='*':
                    m[3]='o';
                    count+=1;
                    clr()
                    break;
                if m[6]==m[3]and m[0]=='*'and m[3]!='*':
                    m[0]='o';
                    count+=1;
                    clr()
                    break;
                #column two
                if m[4]==m[1]and m[7]=='*'and m[4]!='*':
                    m[7]='o';
                    count+=1;
                    clr()
                    break;
                if m[4]==m[7]and m[1]=='*'and m[4]!='*':
                    m[1]='o';
                    count+=1;
                    clr()
                    break;
                if m[7]==m[1]and m[4]=='*'and m[1]!='*':
                    m[4]='o';
                    count+=1;
                    clr()
                    break;
                #column three
                if m[5]==m[2]and m[8]=='*'and m[5]!='*':
                    m[8]='o';
                    count+=1;
                    clr()
                    break;
                if m[5]==m[8]and m[2]=='*'and m[8]!='*':
                    m[2]='o';
                    count+=1;
                    clr()
                    break;
                if m[8]==m[2]and m[5]=='*'and m[8]!='*':
                    m[5]='o';
                    count+=1;
                    clr()
                    break;
                #row one
                if m[0]==m[2]and m[1]=='*'and m[0]!='*':
                    m[1]='o';
                    count+=1;
                    clr()
                    break;
                if m[0]==m[1]and m[2]=='*'and m[0]!='*':
                    m[2]='o';
                    count+=1;
                    clr()
                    break;
                if m[1]==m[2]and m[0]=='*'and m[1]!='*':
                    m[0]='o';
                    count+=1;
                    clr()
                    break;
                #row two
                if m[4]==m[3]and m[5]=='*'and m[4]!='*':
                    m[5]='o';
                    count+=1;
                    clr()
                    break;
                if m[4]==m[5]and m[3]=='*'and m[4]!='*':
                    m[3]='o';
                    count+=1;
                    clr()
                    break;
                if m[5]==m[3]and m[4]=='*'and m[5]!='*':
                    m[4]='o';
                    count+=1;
                    clr()
                    break;
                #row three
                if m[7]==m[8]and m[6]=='*'and m[8]!='*':
                    m[6]='o';
                    count+=1;
                    clr()
                    break;
                if m[7]==m[6]and m[8]=='*'and m[6]!='*':
                    m[8]='o';
                    count+=1;
                    clr()
                    break;
                if m[6]==m[8]and m[7]=='*'and m[8]!='*':
                    m[7]='o';
                    count+=1;
                    clr()
                    break;
                y=random.randint(1,9)-1;
                if m[y]!='x' and m[y]!='o':
                    m[y]='o';
                    count+=1;
                    clr()
                    break;
                else:
                    pass
#checking if
#diagonal checking
            if m[4]==m[0]and m[4]==m[8]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[4]==m[6]and m[4]==m[2]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
#row and column checkings
    #1,1
            if m[0]==m[1] and m[0]==m[2]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[0]==m[3] and m[0]==m[6]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
    #2,2
            if m[3]==m[4] and m[3]==m[5]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[1]==m[4] and m[1]==m[7]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
    #3,3
            if m[6]==m[7] and m[6]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
            if m[2]==m[5] and m[2]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','UWON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','ULOST')
                    break;
        tkinter.messagebox.showinfo('matchfinished','hitplayfornewmatch')
        clr()
        break;
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#play button function
def play2():
    while 1:
        print("new game starts")
        m=['*','*','*','*','*','*','*','*','*'];
        count=0;

        while 1:


#player one's turn

            while 1:


                printmat(*m)
                x=int(tkinter.simpledialog.askinteger('playerone','number'))-1;
                if m[x]!='x' and m[x]!='o':
                        m[x]='x';
                        count+=1;
                        clr()
                        break;
                else:
                    tkinter.messagebox.showerror('!!!!!!!!','UCANTDOTHAT!')

#checking if
#diagonal checking
            if m[4]==m[0]and m[4]==m[8]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[4]==m[6]and m[4]==m[2]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
#row and column checkings
    #1,1
            if m[0]==m[1] and m[0]==m[2]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[0]==m[3] and m[0]==m[6]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
    #2,2
            if m[3]==m[4] and m[3]==m[5]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[1]==m[4] and m[1]==m[7]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
    #3,3
            if m[6]==m[7] and m[6]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[2]==m[5] and m[2]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
#draw match scenario
            if count==9:
                printmat(*m);
                tkinter.messagebox.showinfo('!!!!!!!!','ITISADRAW')
                break;

#player two's turn

            while 1:


                printmat(*m)
                x=int(tkinter.simpledialog.askinteger('playertwo','number'))-1;
                if m[x]!='x' and m[x]!='o':
                        m[x]='x';
                        count+=1;
                        clr()
                        break;
                else:
                    tkinter.messagebox.showerror('!!!!!!!!','UCANTDOTHAT!')

#checking if
#diagonal checking
            if m[4]==m[0]and m[4]==m[8]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[4]==m[6]and m[4]==m[2]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
#row and column checkings
    #1,1
            if m[0]==m[1] and m[0]==m[2]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[0]==m[3] and m[0]==m[6]:
                if m[0]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[0]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
    #2,2
            if m[3]==m[4] and m[3]==m[5]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[1]==m[4] and m[1]==m[7]:
                if m[4]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[4]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
    #3,3
            if m[6]==m[7] and m[6]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
            if m[2]==m[5] and m[2]==m[8]:
                if m[8]=='x':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','1WON')
                    break;
                if m[8]=='o':
                    printmat(*m);
                    tkinter.messagebox.showinfo('!!!!!!!!','2WON')
                    break;
        tkinter.messagebox.showinfo('matchfinished','hitplayfornewmatch')
        clr()
        break;






#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
from tkinter import *

master = Tk()
master.geometry('180x180')
frame=Frame(master,width=50,height=50)
frame.pack(side='bottom')
t=Text(master,width=40,height=40)
t.pack(side='top')
master.title("XNO BY VINAY")

tkinter.messagebox.showinfo("INSTRUCTIONS",'keeping in mind that each position is respectively held by a number from 1-9\n give the respective number to place your pick\n the first row elements are 1,2,3 respectively\n')

but1=Button(frame,text="singleplayer",fg="red",bg="yellow",command=play)
but1.pack(side="top",fill=X)
but3=Button(frame,text="2player",fg="red",bg="yellow",command=play2)
but3.pack(side="top",fill=X)
but2=Button(frame,text="quit!",fg="orange",bg="black",command=frame.quit)
but2.pack(side="bottom",fill=X)



master.mainloop()
