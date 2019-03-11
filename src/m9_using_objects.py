"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and MAddie Sorensen
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    #two_circles()
    #circle_and_rectangle()
    lines()
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:


def two_circles():
    window1 = rg.RoseWindow(300, 300, )
    cir = rg.Circle(rg.Point(200,40),6)
    second=rg.Circle(rg.Point(125,125),100)
    second.fill_color='red'
    second.attach_to(window1)
    cir.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()


    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------


def circle_and_rectangle():
    window1 = rg.RoseWindow(300, 300, )
    point1 = rg.Point(150, 150)
    point2 = rg.Point(210, 50)
    rec = rg.Rectangle(point1, point2)
    second = rg.Circle(rg.Point(120, 200), 50)
    second.fill_color = 'blue'
    second.attach_to(window1)
    rec.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()
    print("1")
    print("blue")
    print("Point (120,200)")
    print("120")
    print("200")
    print("1")
    print("none")
    print("Point (180,100)")
    print("180")
    print("100")
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------

import math
def lines():
    window1 = rg.RoseWindow(300, 300, )
    point1 = rg.Point(150, 150)
    point2 = rg.Point(210, 50)
    line1=rg.Line(point1,point2)
    line1.attach_to(window1)
    point11 = rg.Point(50, 170)
    point22 = rg.Point(175, 65)
    line11 = rg.Line(point11, point22)
    line11.thickness=10
    line11.attach_to(window1)
    xc = math.sqrt(50**2+175**2)
    ycenter = math.sqrt(170**2+65**2)
    print("Point(xc, ycenter)")
    print("xcenter")
    print("ycenter")
    window1.render()
    window1.close_on_mouse_click()
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
