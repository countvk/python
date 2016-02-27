for p in range(3):
    print("*\t*\t*\n");
print("||");
print("1\t2\t3\n4\t5\t6\n7\t8\t9\n")   ;
print("enter the respective number to place your symbol player one will be x and player two will be o\n");

import random
#matrix printer

def printmat(*m):
    for i in range(3):
        print(m[i],end='');
    print("\n");
    for i in range(3,6):
        print(m[i],end='');
    print("\n");
    for i in range(6,9):
        print(m[i],end='');
    print("\n");

def play():



    while 1:
        #game asker

        print("NEW GAME=any number AND QUIT=0");
#turn rotation while loop
        ans=int(input());
        if ans!=0:
            m=['*','*','*','*','*','*','*','*','*'];
            count=0;
            while 1:


#player one's turn

                while 1:
                    print("PLAYER ONE");
                    printmat(*m);
                    x=int(input())-1;
                    if m[x]!='x' and m[x]!='o':
                        m[x]='x';
                        count+=1;
                        break;
                    else:
                        print("YOU CANNOT PLACE HERE");
#checking if
#diagonal checking
                if m[4]==m[0]and m[4]==m[8]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[4]==m[6]and m[4]==m[2]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
#row and column checkings
    #1,1
                if m[0]==m[1] and m[0]==m[2]:
                    if m[0]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[0]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[0]==m[3] and m[0]==m[6]:
                    if m[0]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[0]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
    #2,2
                if m[3]==m[4] and m[3]==m[5]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[1]==m[4] and m[1]==m[7]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
    #3,3
                if m[6]==m[7] and m[6]==m[8]:
                    if m[8]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[8]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[2]==m[5] and m[2]==m[8]:
                    if m[8]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[8]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
#draw match scenario
                if count==9:
                    printmat(*m);
                    print("MATCH IS A DRAW!!!!");
                    break;
#player two's turn
                while 1:
                    print("PLAYER TWO");
                    printmat(*m);
                    y=random.rndint(1,9)-1;
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
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[4]==m[6]and m[4]==m[2]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
#row and column checkings
    #1,1
                if m[0]==m[1] and m[0]==m[2]:
                    if m[0]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[0]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[0]==m[3] and m[0]==m[6]:
                    if m[0]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[0]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
    #2,2
                if m[3]==m[4] and m[3]==m[5]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[1]==m[4] and m[1]==m[7]:
                    if m[4]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[4]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
    #3,3
                if m[6]==m[7] and m[6]==m[8]:
                    if m[8]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[8]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;
                if m[2]==m[5] and m[2]==m[8]:
                    if m[8]=='x':
                        printmat(*m);
                        print("PLAYER ONE WINS!!!!!!!");
                        break;
                    if m[8]=='o':
                        printmat(*m);
                        print("PLAYER TWO WINS!!!!!!!");
                        break;

        else:
            print("GOOD BYE");
            break;
#play
play();
