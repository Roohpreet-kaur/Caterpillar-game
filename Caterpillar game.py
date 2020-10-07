#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random
import turtle as t


# In[12]:


#create a new turtle for the caterpillar
caterpillar =t.Turtle()
caterpillar.shape('circle')
caterpillar.color('red')
#we dont want turtle to ,ove before the game starts
caterpillar.speed(0)
caterpillar.penup()
#hides the turtle
caterpillar.hideturtle()


# In[13]:


#this turtle will draw leaves
leaf=t.Turtle()
#the coordinates of leaf shape
leaf_shape= ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 4))
t.register_shape('leaf',leaf_shape)
#this line tells the turtle about the leaf shape
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)


# In[14]:


#you'll need to know later if the game has started
game_started = False
text_turtle = t.Turtle()
#draws some text on screen
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
#this hides the turtle but not the text.
text_turtle.hideturtle()
#add a turtle to write the score
score_turtle = t.Turtle()
score_turtle.hideturtle()
#the turtle needs to stay where it is, so that it can update the score
score_turtle.speed(0)


# In[15]:


#to get a basic version of the program running sooner, you can use placeholders for functions that you'll finish coding later.
def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    #this fxn returns two values(a "tuple").
    (x,y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall 
    #if any of the four conditions above is true, then outside is true
    return outside

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!', align = 'center', font=('Arial', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align= 'right', font=('Arial', 40 , 'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    leaf.st()
  


# In[16]:


def start_game():
    global game_started
    #if game has already started, the return command makes the function quit so it doesnt run a second time
    if game_started:
        return
    game_started = True
    
    score = 0
    #clear the text from screen
    text_turtle.clear()
    
    caterpillar_speed = 2
    caterpillar_length = 3
    #the turtle stretches into a caterpillar shape
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    #This line places the first leaf on the screen
    place_leaf() 
    while True: 
        caterpillar.forward(caterpillar_speed)
    #the caterpillar eats the leaf when its less than 20px away
        if caterpillar.distance(leaf) < 20:
        #the current leaf has been eaten, so add a new leaf
            place_leaf()
        #this will make the caterpillar grow longer
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break    


# In[ ]:





# In[17]:


def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)
def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
        


# In[18]:


#when you press the space bar, the game begins
t.bgcolor('yellow')
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_right, 'Right')
t.onkey(move_left, 'Left')
t.listen()
t.title("Caterpillar Game")
t.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




