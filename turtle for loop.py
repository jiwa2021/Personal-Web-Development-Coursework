import turtle

                                        # keep len at 55 and ang at 87 for cool design
Length = int(input('enter length: '))
Angle = int(input('enter angle: '))         # instead of entering each value manually nelow, this is here to to resize the shape to user specification

turtle.speed(150)
def octagon():                                            
    turtle.forward(Length)
    turtle.right(Angle)
    turtle.forward(Length)
    turtle.right(Angle)
    turtle.forward(Length)                      # KEEP ANGLE AT 45 DEGREES FOR OCTAGON
    turtle.right(Angle)
    turtle.forward(Length)
    #turtle.right(Angle)
    #turtle.forward(Length)
    #turtle.right(Angle)
    #turtle.forward(Length)
    #turtle.right(Angle)
    #turtle.forward(Length)
    #turtle.right(Angle)
    #turtle.forward(Length)
    #turtle.right(Angle)

octagon()

for count in range(200):
    octagon()
