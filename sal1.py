import random
l=["r","p","s"]
d={'r':"rock",'p':'paper','s':'scissor'}
us=0
cs=0
while True:
    u=input("enter your choice,rock,paper,scissor,press n to discontinue")
    if u=='n':
        print("game over")
        print("computer scroe",cs)
        print("user scroe",us)
        if us<cs:
            print("computer wins")
        elif us==cs:
            print("its tie")
        else :
            print("user wins") 
        exit()
    c=random.choice(l)
    print ("computer choice",d[c])
    print ("user choice",d[u])
    if u == c:
        print("tie")
    elif u=="r" and c=="p":
        print("comp wins")
        cs=cs+1
    elif u == 'r' and c =='s':
        print("user wins")
        us=us+1         
    elif u=="p" and c=="r":
        print("comp wins")
        cs=cs+1
    elif u == 'p' and c =='s':
        print("user wins")
        us=us+1         
    elif u=="s" and c=="r":
        print("comp wins")
        cs=cs+1
    elif u == 's' and c =='p':
        print("user wins")
        us=us+1         


