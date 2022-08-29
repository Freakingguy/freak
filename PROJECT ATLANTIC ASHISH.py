import sys
import random 
def tax(t):
    t=t+(18/100)*t
    return t
def pizza(M,N,O,P,Q):
    X=(M*25)+(N*20)+(O*15)+(P*35)+(Q*24)+300
    return X
def burger(R,S,T,W,V):
    Y=(R*15)+(S*10)+(T*14)+(W*25)+(V*12)+100
    return Y
e=0
f=0
g=0
h=0
m=0
o=0
p=0
q=0
r=0
s=0
A=0
B=0
C=0
D=0
E=0
F=0
G=0
H=0                                                                                                                                                              
I=0
J=0
M=0
N=0
O=0
P=0
Q=0
R=0
S=0
T=0
W=0
V=0
w=0
v=0
aa=0
aaa=0
bb=0
bbb=0
cc=0
ccc=0
dd=0
ddd=0
ee=0
eee=0
yy=0
yyy=0
pizz=0
ff=0
burg=0
gg=0
uu=0
uuu=0
print("Welcome To PROJECT ATLANTIC")
print("Enter 1 if you want to see the topics used in this program")
print("Enter 2 if you want to directly enter in the prograam :)")
try:    
    a=int(input("ENTER Either 1 or 2 or get an error :( -->"))
    if a==1:
        print("def,import,pass,error statements,list,count,if-else,range,patterns")
        b=int(input("Enter 3 to start the program -->"))
        if b==3:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Welcome To Rich table Restaurant")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            c=1
    if a==2:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Welcome To Rich table Restaurant")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        c=1

    if c==1 or 2:
        for i in range(1,6,1):
            for j in range(1,i+1,1):
                print("*",end=' ')
            print()
        print("_______________________________________________________________")
        print("                        ミ★ MEALS ★彡                         ")
        print("```````````````````````````````````````````````````````````````")
        print("Pizza Grilled Sandwich                       @Rs145 {CODE: 101}")
        print("ALoo Tikki with Choley                       @Rs115 {CODE: 102}")
        print("Chilli Paneer with Noodles                   @Rs170 {CODE: 103}")
        print("Veg Fried Rice                               @Rs160 {CODE: 104}")
        print("Rajma Rice Combo                             @Rs155 {CODE: 105}")
        print("Bhalla Paddi                                 @Rs120 {CODE: 106}")
        print("Raj Kachori                                  @Rs130 {CODE: 107}")
        print("Matar Kulcha                                 @Rs110 {CODE: 108}")
        print("Purani Dilli Ke Chole Rice                   @Rs135 {CODE: 109}")
        print("ATLANTIC SPECIAL                             @Rs700 [CODE: 110]")        
        print("                        ミ★ DRINKS ★彡                        ")
        print("```````````````````````````````````````````````````````````````")
        print("                             ⓉⒺⒶ                             ")
        print("Ice Lemon Tea                                @Rs190 {CODE: 111}")        
        print("Italian tea                                  @Rs240 {CODE: 112}")
        print("Green tea                                    @Rs220 {CODE: 113}")
        print("Heaven delight tea                           @Rs300 {CODE: 114}")
        print("                           ⒸⓄⒻⒻⒺⒺ                          ")
        print("Espresso Americano                           @Rs200 {CODE: 115}")
        print("Cappuccino                                   @Rs205 {CODE: 116}")
        print("Iced Mocha                                   @Rs209 {CODE: 117}")
        print("Caffe Latte                                  @Rs290 {CODE: 118}")
        print("_______________________________________________________________")
        print("                    ╰•★★ CUSTOM MEAL ★★•╯                    ")
        print("CUSTOM PIZZA                                @Rs300+ {CODE: 119}")
        print("   cheese layer                                +@Rs25          ")
        print("   paneer layer                                +@Rs20          ")
        print("   tomato layer                                +@Rs15          ")
        print("   onion layer                                 +@Rs35          ")
        print("   mushroom layer                              +@Rs24          ")
        print("CUSTOM BURGER                               @Rs100+ {CODE: 120}")
        print("   cheese layer                                +@Rs25          ")
        print("   mayonnaise layer                            +@Rs20          ")
        print("   tomato layer                                +@Rs15          ")
        print("   onion layer                                 +@Rs35          ")
        print("   latus layer                                 +@Rs24          ")
        print("_______________________________________________________________")
        for i in range(1,6,1):
            for j in range(7,i+1,-1):
                print("*",end=' ')
            print()
        L=[]
        d=int(input("ENTER NUMBER OF ITEMS YOU WANNA ORDER:"))
        if d<21:
            for k in range(0,d):
                val=int(input("ENTER CODE OF YOUR ITEM:"))
                L.append(val)
                if L[k]==101:                    
                    if L.count(101)> 1:
                        print("System got to know you have already enter code 101")
                    else:
                        A=int(input("ENTER THE QUANTITY OF YOUR Pizza Grilled Sandwich-->"))
                        e=145
                elif L[k]==102:                    
                    if L.count(102)> 1:                                                
                        print("System got to know you have already enter code 102")
                    else:
                        B=int(input("ENTER THE QUANTITY OF YOUR ALoo Tikki with Choley-->"))
                        f=115
                elif L[k]==103:                    
                    if L.count(103)> 1:                        
                        print("System got to know you have already enter code 103")
                    else:
                        C=int(input("ENTER THE QUANTITY OF YOUR Chilli Paneer with Noodles-->"))
                        g=170
                elif L[k]==104:                    
                    if L.count(104)> 1:
                        print("System got to know you have already enter code 104")
                    else:                        
                        D=int(input("ENTER THE QUANTITY OF YOUR Veg Fried Rice-->"))
                        h=160
                elif L[k]==105:                    
                    if L.count(105)> 1:
                        print("System got to know you have already enter code 105")
                    else:
                        E=int(input("ENTER THE QUANTITY OF YOUR Rajma Rice Combo-->"))
                        m=155
                elif L[k]==106:                    
                    if L.count(106)> 1:
                        print("System got to know you have already enter code 106")
                    else:
                        F=int(input("ENTER THE QUANTITY OF YOUR Bhalla Paddi-->"))
                        o=120
                elif L[k]==107:                    
                    if L.count(107)> 1:
                        print("System got to know you have already enter code 107")
                    else:
                        G=int(input("ENTER THE QUANTITY OF YOUR Raj Kachori-->"))
                        p=130
                elif L[k]==108:                    
                    if L.count(108)> 1:
                        print("System got to know you have already enter code 108")
                    else:
                        H=int(input("ENTER THE QUANTITY OF YOUR Matar Kulcha-->"))
                        q=110
                elif L[k]==109:                    
                    if L.count(109)> 1:
                        print("System got to know you have already enter code 109")
                    else:
                        I=int(input("ENTER THE QUANTITY OF YOUR Purani Dilli Ke Chole Rice-->"))
                        r=135
                elif L[k]==110:                    
                    if L.count(110)> 1:
                        print("System got to know you have already enter code 110")
                    else:
                        J=int(input("ENTER THE QUANTITY OF YOUR ATLANTIC SPECIAL-->"))
                        s=700
                elif L[k]==111:
                    if L.count(111)> 1:
                        print("System got to know you have already enter code 111")
                    else:
                        w=int(input("ENTER THE QUANTITY OF YOUR Ice Lemon Tea-->"))
                        v=190
                elif L[k]==112:
                    if L.count(112)> 1:
                        print("System got to know you have already enter code 112")
                    else:
                        aa=int(input("ENTER THE QUANTITY OF YOUR Italian tea-->"))
                        aaa=240
                elif L[k]==113:
                    if L.count(113)> 1:
                        print("System got to know you have already enter code 113")
                    else:
                        bb=int(input("ENTER THE QUANTITY OF YOUR Green tea-->"))
                        bbb=220
                elif L[k]==114:
                    if L.count(114)> 1:
                        print("System got to know you have already enter code 114")
                    else:
                        uu=int(input("ENTER THE QUANTITY OF YOUR Heaven delight tea-->"))
                        uuu=300
                elif L[k]==115:
                    if L.count(115)> 1:
                        print("System got to know you have already enter code 115")
                    else:
                        cc=int(input("ENTER THE QUANTITY OF YOUR Espresso Americano-->"))
                        ccc=200
                elif L[k]==116:
                    if L.count(116)> 1:
                        print("System got to know you have already enter code 116")
                    else:
                        dd=int(input("ENTER THE QUANTITY OF YOUR Cappuccino-->"))
                        ddd=205
                elif L[k]==117:
                    if L.count(117)> 1:
                        print("System got to know you have already enter code 117")
                    else:
                        ee=int(input("ENTER THE QUANTITY OF YOUR Iced Mocha-->"))
                        eee=209
                elif L[k]==118:
                    if L.count(118)> 1:
                        print("System got to know you have already enter code 118")
                    else:
                        yy=int(input("ENTER THE QUANTITY OF YOUR Caffe Latte-->"))
                        yyy=290
                elif L[k]==119:
                    if L.count(119)> 1:
                        print("System got to know you have already enter code 119")
                    else:
                        ff=int(input("ENTER THE QUANTITY OF YOUR CUSTOM PIZZA-->"))
                        M=int(input("ENTER THE QUANTITY OF cheese layer-->"))
                        print("1 layer= 8 to 10 pieces[for toppings]")
                        N=int(input("ENTER THE QUANTITY OF paneer layer-->"))
                        O=int(input("ENTER THE QUANTITY OF tomato layer-->"))
                        P=int(input("ENTER THE QUANTITY OF onion layer-->"))
                        Q=int(input("ENTER THE QUANTITY OF mushroom layer-->"))
                        pizz=pizza(M,N,O,P,Q)                        
                elif L[k]==120:
                    if L.count(120)> 1:
                        print("System got to know you have already enter code 120")
                    else:
                        gg=int(input("ENTER THE QUANTITY OF YOUR CUSTOM BURGER-->"))
                        R=int(input("ENTER THE QUANTITY OF cheese layer-->"))
                        S=int(input("ENTER THE QUANTITY OF mayonnaise layer-->"))
                        print("1 layer= 3 to 5 pieces[for tomatos & onions]")
                        T=int(input("ENTER THE QUANTITY OF tomatos layer-->"))
                        W=int(input("ENTER THE QUANTITY OF onions layer-->"))
                        V=int(input("ENTER THE QUANTITY OF latus layer-->"))
                        burg=burger(R,S,T,W,V)
                else:
                    print("LOOKS LIKE YOU ENTER THE CODE WRONG this order will not be inclueded")
        
        else:
            print("let me tell you a secret there are only 20 items available plz run the program again")
            exit()                    
        t=e*A+f*B+g*C+h*D+m*E+o*F+p*G+q*H+r*I+s*J+w*v+aa*aaa+bb*bbb+cc*ccc+dd*ddd+ee*eee+uu*uuu+yy*yyy+ff*pizz+gg*burg        
        u=tax(t)
        print("ORDER SUMMARY",L)
        Y=int(input("ENTER YOUR CARD PIN:"))
        print("THANKS FOR HAVING YOUR MEAL HERE")
        print("NOTHING BRINGS PEOPLE TOGETHER LIKE GOOD FOOD")
        print("-------------------------------------INVOICE-------------------------------------")
        print("ITEM NAME                         PRICE RATE         QUANTITY         PRICE")
        print("_________________________________________________________________________________")
        if 101 in L:
            print("Pizza Grilled Sandwich            @Rs 145.00           ",A, "          Rs",e*A)
        else:
            pass
        if 102 in L:
            print("ALoo Tikki with Choley            @Rs 115.00           ",B, "          Rs",f*B)
        else:
            pass
        if 103 in L:
            print("Chilli Paneer with Noodles        @Rs 170.00           ",C, "          Rs",g*C)
        else:
            pass
        if 104 in L:
            print("Veg Fried Rice                    @Rs 160.00           ",D, "          Rs",h*D)
        else:
            pass
        if 105 in L:
            print("Rajma Rice Combo                  @Rs 155.00           ",E, "          Rs",m*E)      
        else:
            pass
        if 106 in L:
            print("Bhalla Paddi                      @Rs 120.00           ",F, "          Rs",o*F)
        else:
            pass
        if 107 in L:
            print("Raj Kachori                       @Rs 130.00           ",G, "          Rs",p*G)
        else:
            pass
        if 108 in L:
            print("Matar Kulcha                      @Rs 110.00           ",H, "          Rs",q*H)
        else:
            pass
        if 109 in L:
            print("Purani Dilli Ke Chole Rice        @Rs 135.00           ",I, "          Rs",r*I)
        else: 
            pass
        if 110 in L:
            print("ATLANTIC SPECIAL                  @Rs 700.00           ",J, "          Rs",s*J)                  
        else:
            pass
        if 111 in L:
            print("Ice Lemon Tea                     @Rs 190.00           ",w, "          Rs",w*v)
        else:
            pass
        if 112 in L:
            print("Italian tea                       @Rs 240.00           ",aa,"          Rs",aa*aaa)
        else:
            pass
        if 113 in L:
            print("Green tea                         @Rs 220.00           ",bb,"          Rs",bb*bbb)
        else:
            pass
        if 114 in L:
            print("Heaven delight tea                @Rs 300.00           ",uu,"          Rs",uu*uuu)
        else:
            pass
        if 115 in L:
            print("Espresso Americano                @Rs 200.00           ",cc,"          Rs",cc*ccc)      
        else:
            pass
        if 116 in L:
            print("Cappuccino                        @Rs 205.00           ",dd,"          Rs",dd*ddd)
        else:
            pass
        if 117 in L:
            print("Iced Mocha                        @Rs 209.00           ",ee,"          Rs",ee*eee)
        else:
            pass
        if 118 in L:
            print("Caffe Latte                       @Rs 290.00           ",yy,"          Rs",yy*yyy)
        else:
            pass
        if 119 in L:
            print("CUSTOM PIZZA                      @Rs 300+             ",ff,"          Rs",ff*pizz)
        else: 
            pass
        if 120 in L:
            print("CUSTOM BURGER                     @Rs 100+             ",gg,"          Rs",gg*burg)                  
        else:
            pass
        print("_________________________________________________________________________________")
        print("TOTAL (WITHOUT TAX)                                                 Rs",t)
        print("TOTAL (Including all taxes)                                         Rs",u)
        print("-------------------------------------INVOICE-------------------------------------")
        discount=u-((20/100)*u)
        gift=int(input("Do you want to take a chance to get a discount of 20% by paying 5% of your total? (ENTER 1 for yes & 2 for no)"))
        loser=u+((5/100)*u)
        if gift==1:
            wow=int(input("Enter 1 or 2 there is 50% chances of you winning"))
            num=random.randrange(1,3)
            if wow==num:
                print("congratulation now you have to pay only",discount)
            else:
                print("better luck next time your total",loser)
        else:
            print("YOU can still check your luck there will be no change in your total")
            wow2=int(input(" Enter a number between 1 or 2 there is 50% chances of you winning"))
            num2=random.randrange(1,3)
            if wow2==num2:
                print("you win but who cares you didn't take the risk")
            else:
                print("I think your decision was right of not taking the risk")                                                                          
except:
     print(" ERROR!!! I THINK YOU PRESS 1 OR 2 KEYS WRONG kindly run the program again")
     exit()
