import turtle
class AjobTurtle(turtle.Turtle):
    """AjobTurtle is a aclass for new type of turtle"""
    pass

if __name__=="__main__":
    montu=AjobTurtle()
    print(type(montu))
    montu.left(30)
    montu.forward(200)

    turtle.done()
