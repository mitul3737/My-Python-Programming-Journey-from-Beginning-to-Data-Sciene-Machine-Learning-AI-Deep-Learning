import turtle

#function to create a square
def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter=0
while counter<90: #creating 90 squares
    draw_square(100) #calling function
    turtle.right(4) #moving to 4 degree angle of the prevous square
    counter+=1
turtle.exitonclick()