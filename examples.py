import turtle
from lsystem import LSystem

kochcurve = LSystem(
    axiom = "F",
    rules = {
        "F": "F+F-F-F+F"
    },
    angle = 90,
    length = 10
)

eviltree = LSystem(
    axiom = "Y",
    rules = {
        "X": "X[-FFF]+[+FFF]-FX",
        "Y": "YFX[+Y]-[-Y]+"
    },
    angle = 25.7,
    length = 3
)

# kochcurve.draw_lsyst(4)
eviltree.draw_lsyst(6)
turtle.done()
