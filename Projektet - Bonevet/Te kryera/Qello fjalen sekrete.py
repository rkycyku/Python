import turtle,time,random

emri = input("Si e keni emrin? ")

print("Tung", emri, 'Koha per te luajtur "Qello fjalen sekrete"!')
time.sleep(1)

print("\nProvo te qellosh fjalen sekrete...")
time.sleep(.5)

lista = ["bonevet","rilind","kacanik","python","programim","kyqyku","vetura","televisioni","pica","byrek","embelsir","pite","flej","luaj","vizatoj","mesoj","punoj","amerika"]
fjala_sekrete = random.choice(lista)

qello = ""

radha = 7

window = turtle.Screen()
turtle.bgcolor("yellow")
turtle.color("blue","lightblue")

turtle.pensize(5)

turtle.penup()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.pendown()

while radha > 0:
    deshtim = 0

    for shkronja in fjala_sekrete:
        if shkronja in qello:
            print(shkronja)
        else:
            print("_")
            deshtim +=1
    print("\nJu keni edhe", radha, "here per te provuar")

    
    if radha == 6 and qello_shkronjen not in fjala_sekrete:
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        
    if radha == 5 and qello_shkronjen not in fjala_sekrete:
        turtle.right(90)
        turtle.forward(50)
        
    if radha == 4 and qello_shkronjen not in fjala_sekrete:
        turtle.right(45)
        turtle.forward(80)
        turtle.right(180)
        turtle.forward(80)
        
    if radha == 3 and qello_shkronjen not in fjala_sekrete:
        turtle.right(90)
        turtle.forward(80)
        turtle.right(180)
        turtle.forward(80)
        
    if radha == 2 and qello_shkronjen not in fjala_sekrete:  
        turtle.left(135)
        turtle.forward(150)
        
        
    if radha == 1 and qello_shkronjen not in fjala_sekrete:
        turtle.right(45)
        turtle.forward(100)
        turtle.right(180)
        turtle.forward(100)
        
            
    if deshtim == 0:
        print("***FITOVE***")
        break
    
    qello_shkronjen = input("\nShkruaj shkronjen: ")
    qello_shkronjen = qello_shkronjen.lower()
    qello += qello_shkronjen
    
    
    if qello_shkronjen not in fjala_sekrete:
        radha -=1
        print("\n***GABIM***")

        if radha == 0:
            turtle.right(90)
            turtle.forward(100)
            print("\n***HUMBE***")
            print("\nFjala sekrete ishte -", "***"+fjala_sekrete+"***")


        







window.exitonclick()
