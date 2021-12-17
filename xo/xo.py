import turtle
t=turtle.Turtle()
class body :
    staticmethod
    def main():
        t.left(90)
        t.forward(240)
        t.penup()
        t.goto(100,0)
        t.pendown()
        t.forward(240)
        t.penup()
        t.goto(-100,80)
        t.pendown()
        t.right(90)
        t.forward(300)
        t.penup()
        t.goto(-100,160)
        t.pendown()
        t.forward(300)
        t.penup()
        
def square():
    for i in range (4):
        t.forward(30)
        t.left(90)
def circle():
    t.circle(20)        



def bodyc():
    print("1 . 2 . 3")  
    print('...........')
    print('4 . 5 . 6') 
    print('...........') 
    print('7 . 8 . 9')    












z=1
body.main()
li1=[]
li2=[]


class game:
    staticmethod
    for x in range (9):
        bodyc()
        a=int(input("adad makan khod ra vared knid:"))
        
        if a in li1:
            print("it chosen ")
            b=int(input("adad makan khod ra vared knid:"))
            a=b
        li1.append(a)
        
        if a==7:
            t.penup()
            t.goto(-60,30)
            t.pendown()
            b=1
            if z>0:
                circle()
            if z<0:
                square()
        if a==8:
            t.penup()
            t.goto(40,30)  
            t.pendown()  
            b=4 
            if z>0:
                circle()
            if z<0:
                square()  


        if a==9:
            t.penup()
            t.goto(140,30)  
            t.pendown() 
            b=7
            if z>0:
                circle()
            if z<0:
                square()
        if a==4:
            t.penup()
            t.goto(-60,110)  
            t.pendown() 
            b=2
            if z>0:
                circle()
            if z<0:
                square()
        if a==5:
            t.penup()
            t.goto(40,110)  
            t.pendown() 
            b=5
            if z>0:
                circle()
            if z<0:
                square()
        if a==6:
            t.penup()
            t.goto(140,110)  
            t.pendown() 
            b=8
            if z>0:
                circle()
            if z<0:
                square()
        if a==1:
            t.penup()
            t.goto(-60,190)  
            t.pendown() 
            b=3
            if z>0:
                circle()
            if z<0:
                square()
        if a==2:
            t.penup()
            t.goto(40,190)  
            t.pendown() 
            b=6
            if z>0:
                circle()
            if z<0:
                square()

        if a==3:
            t.penup()
            t.goto(140,190)  
            t.pendown() 
            b=9
            if z>0:
                circle()
            if z<0:
                square()        
        li2.append(b)
        z=z*(-1) 
        if x>=4:
            if li1[x]==(li1[x-2]+li1[x-4])/2 or li1[x-2]==(li1[x]+li1[x-4])/2 or li1[x-4]==(li1[x]+li1[x-2])/2  :
                if x%2==0:
                    print("o u win")
                if x%2==1:
                    print('square u win')
                         
                break 
                
    turtle.mainloop()          

        
            

    