#*simple snake game in python*
import turtle   
   #turtle is  a pre-installed python library that enables users to create shape and 
#pictures by providing them the virtual canvas.[myth that a turtle draws it ]
import time

import random   #module used to chose random numbers i.e. to choose random locations

delay=0.1

#score
score=0
high_score=0

#set up the screen 
wn=turtle.Screen()  #creates a graphics window and S of screen should be capital
wn.title("SNAKE GAME BY BANSAL SAAB")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  #turns  off the screen updates


#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)           #to move the object to co-ordinate(x,y)
head.direction="stop"
#snake food(means so we will craete a  new turtle)
food = turtle.Turtle()
food.speed(0)      #this speed means basically the animation speed
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]    #every time snake bites the food its length increases by one box

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 high score: 0",align="center",font= ("courier",24,"normal"))


#functions
def go_up():
    if head.direction!="down":     #this thing helps the snake to prevent from running into its
                                    #own body  
        head.direction="up"
def go_down():
    if head.direction!="up":
        
        head.direction="down"
def go_left():
    if head.direction!="right":
        
        head.direction="left"
def go_right():
    if head.direction!="left":
        
        head.direction="right"    




def move():
    if head.direction=="up":
        
        
        y=head.ycor()       #snake will move  up 20units everytime and now it will be very fast
        head.sety(y+20)                      #so import module time and delay the time
    
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
        
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#keyboard bindings means that it connects keypress with particular functions
wn.listen()          #to listen for clicks
wn.onkey(go_up,"w")       #here onkey is used for python2.7 and onkeypress for updated version
wn.onkey(go_down,"s")     #and also wuth every fucntion call there are no parenthesis means()
wn.onkey(go_right,"d")
wn.onkey(go_left,"a")
        


#main game loop
while True:
    wn.update()        #now everytime it updates the screen as it is always true
    
    #check for the collisions with the border
    
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)     #this gives a pause of 1 second to the game
        head.goto(0,0)
        head.direction="stop"
        #when the game restarts segments will show at the origin except the head of the snake
        
        #so we need to hide the segments
        for segment in segments:
            segment.goto(1000,1000)#in python we cant delete the segment so will send it far away
                                    #but still it appears due to while loop running always
                                     #so we need to clear the segments list
        
        #clearing the segments list
        segments=[]  #for updates version in python segments.clear() would work
        
        
        #reset the score
        score=0  #so that score now resets to zero when game runs again
        
        pen.clear()
        pen.write("score:{} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))
        #check for the collision with the food
        
    if head.distance(food)<20:       #here distance is an in-built function to calculate distance
       #between the two turtles
        
        #move the food to random spot
        #done with the help of module random
        x=random.randint(-290,290)  #range is this so that it don't go off the screen 
        y=random.randint(-290,290)
        food.goto(x,y)
        
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)  #means to add box at last of snake head when food is bitten
    
    
        #increase the score
        score= score+10     #adds 10 to score everytime it bites the food
        
        if score>high_score:
            high_score=score   #this tells that the new high score is now the score
        
        pen.clear()    #so that the score don't get overlapped
        pen.write("score: {} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))
    
    
    
    
    
    
    #move the end segments first in reverse order:
    
    for index in range(len(segments)-1,0,-1):  #each segment is a turtle which has xcor and ycor
        x=segments[index-1].xcor()      #means if segment is 9 then it will move to segment 8
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    #move segment 0 to where the head is:    
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    move()
    
    #check for the collision of head of the snake with its body:
    for segment in segments:
        if segment.distance(head)<20:   #it means overlapping
            time.sleep(1)
            head.goto(0,0)
            head.direction= "stop"
            
            #so again we need to hide the segments
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
    
    
    
            #clear the segments 
            segments = []          #segments.clear()
            
            #reset the score
            score=0
        
        
            #update the score display
            pen.clear()
            pen.write("score:{} high score:{}".format(score,high_score),align="center",font=("courier",24,"normal"))
        
    
    time.sleep(delay)         #it will delay the movement of snake 1/10 time of earlier
wn.mainloop()
