
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9812482
#    Student name: Kevin Gunawan
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BILLBOARD
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "paste_up".
#  You are required to complete this function so that when the
#  program is run it produces an image of an advertising billboard
#  whose arrangement is determined by data stored in a list which
#  specifies how individual paper sheets are to be pasted onto the
#  backing.  See the instruction sheet accompanying this file for
#  full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

sheet_width = 200 # pixels
sheet_height = 500 # pixels
backing_margin = 20 # pixels
backing_width = sheet_width * 4 + backing_margin * 2
backing_height = sheet_height + backing_margin * 2
canvas_top_and_bottom_border = 150 # pixels
canvas_left_and_right_border = 300 # pixels
canvas_width = (backing_width + canvas_left_and_right_border)
canvas_height = (backing_height + canvas_top_and_bottom_border)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(mark_centre_points = True):

    # Set up the drawing canvas
    setup(canvas_width, canvas_height)

    # Draw as fast as possible
    tracer(False)

    # Colour the sky blue
    bgcolor('sky blue')

    # Draw the ground as a big green rectangle (sticking out of the
    # bottom edge of the drawing canvas slightly)
    overlap = 5 # pixels
    grass_height = 100 # pixels
    penup()
    goto(-(canvas_width // 2 + overlap),
         -(canvas_height // 2 + overlap)) # start at the bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_height + overlap)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_height + overlap)
    end_fill()

    # Draw a nice warm sun peeking into the image
    penup()
    goto(-canvas_width // 2, canvas_height // 2)
    color('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height // 3)
    color('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Draw the billboard's wooden backing as four frames
    # and some highlighted coordinates
    #
    # Outer rectangle
    goto(- backing_width // 2, - backing_height // 2) # bottom left
    pencolor('sienna'); fillcolor('tan'); width(3)
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height)
    right(90) # face east
    forward(backing_width)
    right(90) # face south
    forward(backing_height)
    right(90) # face west
    forward(backing_width)
    end_fill()

    # Inner rectangle
    penup()
    goto(- backing_width // 2 + backing_margin,
         - backing_height // 2 + backing_margin) # bottom left
    fillcolor('gainsboro')
    begin_fill()
    pendown()
    setheading(90) # face north
    forward(backing_height - backing_margin * 2)
    right(90) # face east
    forward(backing_width - backing_margin * 2)
    right(90) # face south
    forward(backing_height - backing_margin * 2)
    right(90) # face west
    forward(backing_width - backing_margin * 2)
    end_fill()

    # Draw lines separating the locations where the sheets go
    width(1); pencolor('dim grey')
    for horizontal in [-sheet_width, 0, sheet_width]:
        penup()
        goto(horizontal, sheet_height // 2)
        pendown()
        setheading(270) # point south
        forward(sheet_height)
         
    # Mark the centre points of each sheet's location, if desired
    if mark_centre_points:
        penup()
        points = [[[round(-sheet_width * 1.5), 0], 'Location 1'],
                  [[round(-sheet_width * 0.5), 0], 'Location 2'],
                  [[round(sheet_width * 0.5), 0], 'Location 3'],
                  [[round(sheet_width * 1.5), 0], 'Location 4']]
        for centre_point, label in points:
            goto(centre_point)
            dot(4)
            write('  ' + label + '\n  (' + str(centre_point[0]) + ', 0)',
                  font = ('Arial', 12, 'normal'))
     
    # Reset everything ready for the student's solution
    color('black')
    width(1)
    penup()
    home()
    setheading(0)
    tracer(True)


# End the program by hiding the cursor and releasing the canvas
def release_drawing_canvas():
    tracer(True)
    hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data------------------------------------------------------#
#
# The list in this section contains the data sets you will use to
# test your code.  Each of the data sets is a list specifying the
# way in which sheets are pasted onto the billboard:
#
# 1. The name of the sheet, from 'Sheet A' to 'Sheet D'
# 2. The location to paste the sheet, from 'Location 1' to
#    'Location 4'
# 3. The sheet's orientation, either 'Upright' or 'Upside down'
#
# Each data set does not necessarily mention all four sheets.
#
# In addition there is an extra value, either 'X' or 'O' at the
# start of each data set.  The purpose of this value will be
# revealed only in Part B of the assignment.  You should ignore it
# while completing Part A.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Note that your solution must work for all the data sets below
# AND ANY OTHER DATA SETS IN THE SAME FORMAT!
#

data_sets = [
    # These two initial data sets don't put any sheets on the billboard
    # Data sets 0 - 1
    ['O'],
    ['X'],
    # These data sets put Sheet A in all possible locations and orientations
    # Data sets 2 - 9
    ['O', ['Sheet A', 'Location 1', 'Upright']],
    ['O', ['Sheet A', 'Location 2', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright']],
    ['O', ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 2', 'Upside down']],
    ['O', ['Sheet A', 'Location 3', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down']],
    # These data sets put Sheet B in all possible locations and orientations
    # Data sets 10 - 17
    ['O', ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet B', 'Location 2', 'Upright']],
    ['O', ['Sheet B', 'Location 3', 'Upright']],
    ['O', ['Sheet B', 'Location 4', 'Upright']],
    ['O', ['Sheet B', 'Location 1', 'Upside down']],
    ['O', ['Sheet B', 'Location 2', 'Upside down']],
    ['O', ['Sheet B', 'Location 3', 'Upside down']],
    ['O', ['Sheet B', 'Location 4', 'Upside down']],
    # These data sets put Sheet C in all possible locations and orientations
    # Data sets 18 - 25
    ['O', ['Sheet C', 'Location 1', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 3', 'Upright']],
    ['O', ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upside down']],
    ['O', ['Sheet C', 'Location 3', 'Upside down']],
    ['O', ['Sheet C', 'Location 4', 'Upside down']],
    # These data sets put Sheet D in all possible locations and orientations
    # Data sets 26 - 33
    ['O', ['Sheet D', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 2', 'Upright']],
    ['O', ['Sheet D', 'Location 3', 'Upright']],
    ['O', ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet D', 'Location 2', 'Upside down']],
    ['O', ['Sheet D', 'Location 3', 'Upside down']],
    ['O', ['Sheet D', 'Location 4', 'Upside down']],
    # These data sets place two sheets in various locations and orientations
    # Data sets 34 - 38
    ['O', ['Sheet D', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 1', 'Upright']],
    ['O', ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet C', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down']],
    # These data sets place three sheets in various locations and orientations
    # Data sets 39 - 43
    ['O', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet C', 'Location 2', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']], 
    ['O', ['Sheet B', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 2', 'Upside down'],
          ['Sheet C', 'Location 1', 'Upside down']], 
    ['X', ['Sheet A', 'Location 4', 'Upright'],
          ['Sheet D', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upright']],
    # These data sets place four sheets in various locations and orientations
    # Data sets 44 - 48
    ['O', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 1', 'Upright'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['O', ['Sheet C', 'Location 1', 'Upside down'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],
    ['O', ['Sheet C', 'Location 2', 'Upright'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down'],
          ['Sheet A', 'Location 4', 'Upright']],
    ['X', ['Sheet C', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upside down'],
          ['Sheet A', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upside down']],     
    # These data sets draw the entire image upside down
    # Data sets 49 - 50
    ['X', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    ['O', ['Sheet A', 'Location 4', 'Upside down'],
          ['Sheet B', 'Location 3', 'Upside down'],
          ['Sheet C', 'Location 2', 'Upside down'],
          ['Sheet D', 'Location 1', 'Upside down']],
    # These are the final, 'correct' arrangements of sheets
    # Data sets 51 - 52
    ['X', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']],
    ['O', ['Sheet A', 'Location 1', 'Upright'],
          ['Sheet B', 'Location 2', 'Upright'],
          ['Sheet C', 'Location 3', 'Upright'],
          ['Sheet D', 'Location 4', 'Upright']]
    ]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "paste_up" function.
#

# Paste the sheets onto the billboard as per the provided data set
setup()
def sheet_A(x,y):
    penup()
    color("black")
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    width(1)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)
    fillcolor("deepskyblue")#creating borders of cloud
    begin_fill()
    pendown()
    width(5)
    for curve in range(10):
        forward(20)
        left(15)
    setheading(180)
    for curve2 in range(35):
        forward(10)
        left(5)
    setheading(270)
    for curve3 in range(10):
        forward(10)
        left(10)
    goto(x+100,y-180)
    end_fill()
    penup()
    goto(x,0)#creating the letter S
    pendown()
    color("white")
    width(20)
    for low_s in range(25):
        forward(5)
        right(10)
    penup()
    goto(x,0)
    color("black")
    setheading(180)
    pendown()
    color("white")
    width(20)
    for upper_s in range(25):
        forward(5)
        right(10)
    penup()
    goto(x+95,y+200)#creating the side of K
    setheading(90)
    fillcolor("white")
    begin_fill()
    pendown()
    width(5)
    for side_k in range(11):
        forward(5)
        left(15)
    setheading(270)
    forward(300)
    for side_k2 in range(11):
        forward(5)
        left(15)
    goto(x+95,y+200)
    end_fill()
    penup()

def invertsheet_A(x,y):#changing setheadings and goto from original function sheet_A(x,y)
    penup()
    color("black")
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    width(1)
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(0)
    fillcolor("deepskyblue")#creating borders of cloud
    goto(x-100,y-250)
    begin_fill()
    pendown()
    width(5)
    for curve in range(10):
        forward(20)
        left(15)
    setheading(0)
    for curve2 in range(35):
        forward(10)
        left(5)
    setheading(-270)
    for curve3 in range(10):
        forward(10)
        left(10)
    goto(x-100,y+180)
    width(1)
    goto(x-100,y-250)
    end_fill()
    penup()
    goto(x,0)#creating the letter S
    pendown()
    color("white")
    width(20)
    for low_s in range(25):
        forward(5)
        right(10)
    penup()
    goto(x,0)
    color("black")
    setheading(0)
    pendown()
    color("white")
    width(20)
    for upper_s in range(25):
        forward(5)
        right(10)
    penup()
    goto(x-95,y-200)#creating the side of K
    setheading(-90)
    fillcolor("white")
    begin_fill()
    pendown()
    width(5)
    for side_k in range(11):
        forward(5)
        left(15)
    setheading(-270)
    forward(300)
    for side_k2 in range(11):
        forward(5)
        left(15)
    goto(x-95,y-200)
    end_fill()
    penup()


def sheet_B(x,y):
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)
    goto(x-100,y+250)#coloring the clouds
    setheading(0)
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    for curve in range(10):
        forward(15)
        right(10)
    setheading(0)
    for curve1 in range(5):
        forward(20)
        right(10)
    goto(x+100,y+100)
    width(1)
    goto(x+100,y-180)
    setheading(270)
    width(5)
    for curve2 in range(20):
        forward(10)
        right(10)
    setheading(270)
    for curve3 in range(9):
        forward(15)
        right(20)
    goto(x-100,y-180)
    width(1)
    goto(x-100,y+250)
    end_fill()
    penup()# writing the front of K
    goto(x-90,y+50)
    setheading(45)
    color("white")
    forward(15)
    pendown()
    width(30)
    forward(100)
    penup()
    goto(x-100,y+50)
    setheading(-60)
    goto(x-85,y+60)
    color("white")
    forward(5)
    pendown()
    width(30)
    forward(150)
    penup()#writing half of y
    goto(x+90,y-60)
    setheading(120)
    forward(20)
    pendown()
    width(25)
    forward(100)
    penup()
    goto(x+100,y-50)
    setheading(230)
    goto(x+85,y-50)
    pendown()
    width(25)
    forward(130)
    right(90)
    forward(20)
    penup()

def invertsheet_B(x,y):#changing setheadings and goto from original function sheet_B(x,y)
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)
    goto(x+100,y-250)#coloring the clouds
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    for curve in range(10):
        forward(15)
        right(10)
    setheading(180)
    for curve1 in range(5):
        forward(20)
        right(10)
    goto(x-100,y-100)
    width(1)
    goto(x-100,y+180)
    setheading(-270)
    width(5)
    for curve2 in range(20):
        forward(10)
        right(10)
    setheading(-270)
    for curve3 in range(9):
        forward(15)
        right(20)
    goto(x+100,y+180)
    width(1)
    goto(x+100,y-250)
    end_fill()
    penup()# writing the front of K
    goto(x+90,y-50)
    setheading(-135)
    color("white")
    forward(15)
    pendown()
    width(30)
    forward(100)
    penup()
    goto(x+100,y-50)
    setheading(120)
    goto(x+85,y-60)
    color("white")
    forward(5)
    pendown()
    width(30)
    forward(150)
    penup()#writing half of y
    goto(x-90,y+60)
    setheading(-60)
    forward(20)
    pendown()
    width(25)
    forward(100)
    penup()
    goto(x-100,y+50)
    setheading(50)
    goto(x-85,y+50)
    pendown()
    width(25)
    forward(130)
    right(90)
    forward(20)
    penup()


def sheet_C(x,y):
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)
    goto(x-100,y+100)#coloring the clouds
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    setheading(90)
    for curve in range(12):
        right(10)
        forward(20)
    goto(x+100,y+160)
    width(1)
    goto(x+100,y-100)
    width(5)
    setheading(270)
    for curve1 in range(5):
        right(20)
        forward(25)
    setheading(270)
    for curve2 in range(10):
        forward(15)
        right(15)
    goto(x-100,y-180)
    width(1)
    goto(x-100,y+100)
    end_fill()
    penup()# drawing the rest of letter y
    goto(x-85,y-35)
    setheading(50)
    pendown()
    color("white")
    width(25)
    forward(90)
    penup()# drawing letter P
    goto(x-20,y+150)
    setheading(270)
    pendown()
    color("white")
    forward(250)
    penup()
    goto(x-10,y+80)
    setheading(270)
    pendown()
    color("white")
    width(20)
    circle(50)
    penup()


def invertsheet_C(x,y):#changing setheadings and goto from original function sheet_C(x,y)
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)
    goto(x+100,y-100)#coloring the clouds
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    setheading(-90)
    for curve in range(12):
        right(10)
        forward(20)
    goto(x-100,y-160)
    width(1)
    goto(x-100,y+100)
    width(5)
    setheading(90)
    for curve1 in range(5):
        right(20)
        forward(25)
    setheading(-270)
    for curve2 in range(10):
        forward(15)
        right(15)
    goto(x+100,y+180)
    width(1)
    goto(x+100,y-100)
    end_fill()
    penup()# drawing the rest of letter y
    goto(x+85,y+35)
    setheading(-130)
    pendown()
    color("white")
    width(25)
    forward(90)
    penup()# drawing letter P
    goto(x+20,y-150)
    setheading(-270)
    pendown()
    color("white")
    forward(250)
    penup()
    goto(x+10,y-80)
    setheading(-270)
    pendown()
    color("white")
    width(20)
    circle(50)
    penup()
    

def sheet_D(x,y):
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)#coloring of clouds
    goto(x-100,y+160)
    setheading(0)
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    forward(20)
    for curve in range(10):
        forward(10)
        right(5)
    setheading(90)
    for curve1 in range(30):
        forward(6)
        right(10)
    setheading(270)
    for curve2 in range(10):
        forward(20)
        right(5)
    goto(x-100,y-100)
    width(1)
    goto(x-100,y+160)
    end_fill()
    penup()
    goto(x-5,y+50)#drawing letter e
    pendown()
    color("white")
    width(20)
    setheading(90)
    circle(42,300)
    penup()
    goto(x-5,y+50)
    setheading(180)
    pendown()
    forward(80)
    penup()#drawing TM
    goto(x+20,y+140)
    setheading(0)
    pendown()
    width(5)
    forward(10)
    right(90)
    forward(30)
    setheading(90)
    forward(30)
    setheading(0)
    forward(10)
    penup()
    goto(x+40,y+140)
    pendown()
    setheading(270)
    forward(30)
    setheading(90)
    forward(30)
    setheading(-60)
    forward(20)
    setheading(60)
    forward(20)
    setheading(270)
    forward(30)
    penup()


def invertsheet_D(x,y):#changing setheadings and goto from original function sheet_D(x,y)
    penup()
    color("black")
    width(1)
    goto(x+100,y+250)#coloring background of sheet
    setheading(180)
    fillcolor("Orange")
    begin_fill()
    pendown()
    forward(200)
    left(90)
    forward(500)
    left(90)
    forward(200)
    left(90)
    forward(500)
    end_fill()
    penup()
    setheading(180)#coloring of clouds
    goto(x+100,y-160)
    fillcolor("deepskyblue")
    begin_fill()
    pendown()
    width(5)
    forward(20)
    for curve in range(10):
        forward(10)
        right(5)
    setheading(-90)
    for curve1 in range(30):
        forward(6)
        right(10)
    setheading(-270)
    for curve2 in range(10):
        forward(20)
        right(5)
    goto(x+100,y+100)
    width(1)
    goto(x+100,y-160)
    end_fill()
    penup()
    goto(x+5,y-50)#drawing letter e
    pendown()
    color("white")
    width(20)
    setheading(-90)
    circle(42,300)
    penup()
    goto(x+5,y-50)
    setheading(0)
    pendown()
    forward(80)
    penup()#drawing TM
    goto(x-20,y-140)
    setheading(180)
    pendown()
    width(5)
    forward(10)
    right(90)
    forward(30)
    setheading(-90)
    forward(30)
    setheading(180)
    forward(10)
    penup()
    goto(x-40,y-140)
    pendown()
    setheading(-270)
    forward(30)
    setheading(270)
    forward(30)
    setheading(120)
    forward(20)
    setheading(-120)
    forward(20)
    setheading(90)
    forward(30)
    penup()


def graffitti():#drawing graffiti tag with initials KG
    penup()#drawing K initial
    color("springgreen")
    width(30)
    goto(-300,200)
    pendown()
    goto(-100,-200)
    penup()
    goto(-200,0)
    pendown()
    goto(-100,200)
    penup()
    goto(-200,0)
    pendown()
    goto(0,-100)
    penup()#drawing G initial
    goto(200,200)
    pendown()
    goto(0,100)
    goto(150,-200)
    goto(300,-100)
    goto(250,-10)
    penup()
    goto(300,10)
    pendown()
    goto(200,-30)
    penup()
    


    
    
    

def paste_up(data_sets):
    if data_sets[0]=="X":#draw graffiti
        for data in range(len(data_sets)):
            if data_sets[data][0]=="Sheet A":# for sheet A
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_A(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_A(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_A(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_A(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_A(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_A(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_A(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_A(300,0)
            elif data_sets[data][0]=="Sheet B":# for sheet B
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_B(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_B(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_B(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_B(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_B(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_B(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_B(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_B(300,0)
            elif data_sets[data][0]=="Sheet C":#for sheet C
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_C(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_C(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_C(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_C(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_C(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_C(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_C(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_C(300,0)
            elif data_sets[data][0]=="Sheet D":#for sheet D
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_D(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_D(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_D(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_D(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_D(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_D(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_D(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_D(300,0)
        graffitti()#graffiti function
    else:#dont draw graffiti
        for data in range(len(data_sets)):
            if data_sets[data][0]=="Sheet A":# for sheet A
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_A(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_A(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_A(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_A(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_A(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_A(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_A(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_A(300,0)
            elif data_sets[data][0]=="Sheet B":# for sheet B
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_B(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_B(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_B(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_B(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_B(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_B(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_B(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_B(300,0)
            elif data_sets[data][0]=="Sheet C":#for sheet C
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_C(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_C(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_C(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_C(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_C(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_C(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_C(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_C(300,0)
            elif data_sets[data][0]=="Sheet D":#for sheet D
                if data_sets[data][2]=="Upright":
                    if data_sets[data][1]=="Location 1":
                        sheet_D(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        sheet_D(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        sheet_D(100,0)
                    elif data_sets[data][1]=="Location 4":
                        sheet_D(300,0)
                elif data_sets[data][2]=="Upside down":
                    if data_sets[data][1]=="Location 1":
                        invertsheet_D(-300,0)
                    elif data_sets[data][1]=="Location 2":
                        invertsheet_D(-100,0)
                    elif data_sets[data][1]=="Location 3":
                        invertsheet_D(100,0)
                    elif data_sets[data][1]=="Location 4":
                        invertsheet_D(300,0)
    
            
            
   

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your billboard.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the centre points of each sheet on the backing
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with one that describes the image
# ***** displayed on your billboard when the sheets are pasted
# ***** correctly
title("Skype Logo")

### Call the student's function to display the billboard
### ***** Change the number in the argument to this function
### ***** to test your code with a different data set
paste_up(data_sets[51])



# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

