from lsystem import LSystem

### EXAMPLES DEFINITIONS ###

examples: dict[str, LSystem] = {
    "kochcurve": LSystem(
        axiom = "F",
        rules = {
            "F": "F+F-F-F+F"
        },
        angle = 90,
        lenght = 2
    ),
    "eviltree": LSystem(
        axiom = "Y",
        rules = {
            "X": "X[-FFF]+[+FFF]-FX",
            "Y": "YFX[+Y]-[-Y]+"
        },
        angle = 25.7,
        lenght = 0.5
    ),
    "eviltree2": LSystem(
        axiom = "Y",
        rules = {
            "X": "X[-FFF][+FFF][+FFF]-FX",
            "Y": "YFX[+Y][-Y][-Y]+"
        },
        angle = 25.7,
        lenght = 5
    )
}

### ACTUAL EXECUTED CODE ###

def main(argv: list):
    assoc = []
    for key in examples:
        assoc.append(key)
    
    for i, key in enumerate(assoc):
        print(f"{i}: {key}")
    print("---")
    
    i = int(input(">> "))
    if i >= len(assoc) or i<0:
        raise ValueError("index is too big or too small")
    
    print(f"drawing \"{assoc[i]}\"...")
    examples[assoc[i]].draw_lsyst(8)

if __name__=="__main__":
    from sys import argv
    main(argv[1:])
