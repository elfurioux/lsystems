from lsystem import Plsystem

### EXAMPLES DEFINITIONS ###

examples: list[Plsystem] = [
    Plsystem(title = "kochcurve",
        axiom = "F",
        rules = {
            "F": "F+F-F-F+F"
        },
        angle = 90,
        lenght = 2
    ),
    Plsystem(title = "ogeviltree",
        axiom = "Y",
        rules = {
            "X": "X[-FFF][+FFF]FX",
            "Y": "YFX[+Y][-Y]"
        },
        angle = 25.7,
        lenght = 7
    ),
    Plsystem(title = "c-ogeviltree",
        axiom = "Y",
        rules = {
            "X": "X[>FFF][<FFF]FX",
            "Y": "YFX[<Y][>Y]"
        },
        angle = 25.7,
        lenght = 7
    ),
    Plsystem(title = "drunkeviltree",
        axiom = "Y",
        rules = {
            "X": "X[-FFF]+[+FFF]-FX",
            "Y": "YFX[+Y]-[-Y]+"
        },
        angle = 25.7,
        lenght = 7
    ),
    Plsystem(title = "sqrtree",
        axiom = "a",
        rules = {
            "F": ">F<",
            "a": "F[+x]Fb",
            "b": "F[-y]Fa",
            "x": "a",
            "y": "b"
        },
        angle = 45,
        lenght = 7
    ),
    Plsystem(title = "wk2-bintree",
        axiom = "0",
        rules = {
            "1": "11",
            "0": "1[-0]+0"
        },
        angle = 45,
        lenght = 3
    ),
    Plsystem(title = "wk5-sierpinsky",
        axiom = "F-G-G",
        rules = {
            "F": "F-G+F+G-F",
            "G": "GG"
        },
        angle = 120,
        lenght = 5
    ),
    Plsystem(title = "wk6-dcurve",
        axiom = "F",
        rules = {
            "F": "F+G",
            "G": "F-G"
        },
        angle = 90,
        lenght = 10
    ),
    Plsystem(title = "wk7-fractal-plant",
        axiom = "X",
        rules = {
            "X": "F+[[X]-X]-F[-FX]+X",
            "F": "FF"
        },
        angle = 25,
        lenght = 7
    )
]

### ACTUAL EXECUTED CODE ###

GENERATIONS = 6

def main(argv: list):
    assoc = []
    for e in examples:
        assoc.append(e.title)
    
    for i, key in enumerate(assoc):
        print(f"{i}: {key}")
    print("---")
    
    i = int(input(">> "))
    if i >= len(assoc) or i<0:
        raise ValueError("index is too big or too small")
    
    d: Plsystem = examples[i]
    print(f"drawing \"{d.title}\"...")
    # print(d.getiteration(GENERATIONS))
    d.lenght = d.lenght
    d.draw_lsyst(GENERATIONS,baseangle=15)

if __name__=="__main__":
    from sys import argv
    main(argv[1:])
    
