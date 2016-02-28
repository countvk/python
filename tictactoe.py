import random
#matrix printer
import tkinter.simpledialog
import tkinter.messagebox
def printmat(*m):
    for i in range(0,3):

        print(  m[i]  ,end='');
        print(  "\t" ,end='');
    print("\n");
    for i in range(3,6):

        print(  m[i]  ,end='');
        print(  "\t" ,end='');
    print("\n");
    for i in range(6,9):

        print(  m[i]  ,end='');
        print(  "\t" ,end='');
    print("\n");
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




#play button function
def play():
    while 1:
        print("new game starts")
        m=['*','*','*','*','*','*','*','*','*'];
        count=0;

        while 1:


#player one's turn

            while 1:
                print("PLAYER ONE");

                printmat(*m)
                x=int(tkinter.simpledialog.askinteger('playerone','number'))-1;
                if m[x]!='x' and m[x]!='o':
                        m[x]='x';
                        count+=1;
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
                print("wait ...........");

                y=random.randint(1,9)-1;
                if m[y]!='x' and m[y]!='o':
                    m[y]='o';
                    count+=1;
                    break;
                else:
                    print("YOU CANNOT PLACE HERE");
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
        break;
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from tkinter import *

master = Tk()
master.geometry()
t=Text(master)
t.pack()
master.title("XNO BY VINAY")
frame=Frame(master,width=1000,height=500)
frame.pack()
tkinter.messagebox.showinfo("INSTRUCTIONS",'keeping in mind that each position is respectively held by a number from 1-9\n give the respective number to place your pick\n the first row elements are 1,2,3 respectively\n')
tlabel=Label(master,text="TIC TAC TOE")
tlabel.pack(side="top")
but1=Button(frame,text="play",fg="red",bg="yellow",command=play)
but1.pack(side="left",fill=X,expand=YES)
but2=Button(master,text="quit!",fg="orange",bg="black",command=frame.quit)
but2.pack(side="bottom",fill=X,expand=YES)



master.mainloop()
