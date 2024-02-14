import turtle
from lsystem import LSystem

### EXAMPLES DEFINITIONS ###

kochcurve = LSystem(
    axiom = "F",
    rules = {
        "F": "F+F-F-F+F"
    },
    angle = 90,
    lenght = 2
)

eviltree = LSystem(
    axiom = "Y",
    rules = {
        "X": "X[-FFF]+[+FFF]-FX",
        "Y": "YFX[+Y]-[-Y]+"
    },
    angle = 25.7,
    lenght = 0.5
)

eviltree2 = LSystem(
    axiom = "Y",
    rules = {
        "X": "X[-FFF][+FFF][+FFF]-FX",
        "Y": "YFX[+Y][-Y][-Y]+"
    },
    angle = 25.7,
    lenght = 5
)

### ACTUAL EXECUTED CODE ###

if __name__=="__main__":
    eviltree.draw_lsyst(8)
