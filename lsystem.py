
import turtle

class LSystem:
    def __init__(self, axiom: str, rules: dict[str], angle: float, length: int) -> None:
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.length = length

    # L SYTEM GENERATION

    def geniterations(self, iterations: int) -> list[str]:
        chains = [self.axiom]
        for n in range(iterations):
            newchain = ""
            for char in chains[n]:
                if char in self.rules:
                    newchain += self.rules[char]
                else:
                    newchain += char
            chains.append(newchain)
        return chains
    
    def getiteration(self, iteration: int) -> str:
        return self.geniterations(iterations=iteration)[-1]

    # L SYSTEM REPRESENTATION

    def draw_lsyst(self, iterations: int):
        ALLOWED_INSTRUCTIONS = "FXY+-&^<>|[]"

        stack: list[turtle.Vec2D] = []

        turtle.penup()
        turtle.goto(0, -turtle.window_height()//2-10)
        turtle.pendown()

        turtle.setheading(90)
        turtle.speed(0)
        for instruction in self.getiteration(iterations):
            if instruction not in ALLOWED_INSTRUCTIONS:
                continue
            
            if instruction in "FXY": # Se déplacer d’un pas unitaire (∈ V) ;
                turtle.forward(self.length)
            elif instruction == "+": # Tourner à gauche d’angle α (∈ S) ;
                turtle.left(self.angle)
            elif instruction == "-": # Tourner à droite d’un angle α (∈ S) ;
                turtle.right(self.angle)
            elif instruction == "&": # Pivoter vers le bas d’un angle α (∈ S) ;
                raise Exception("Not Implemented")
            elif instruction == "^": # Pivoter vers le haut d’un angle α (∈ S) ;
                raise Exception("Not Implemented")
            elif instruction == "<": # Roulez vers la gauche d’un angle α (∈ S) ;
                raise Exception("Not Implemented")
            elif instruction == ">": # Roulez vers la droite d’un angle α (∈ S) ;
                raise Exception("Not Implemented")
            elif instruction == "|": # Tourner sur soi-même de 180° (∈ S) ;
                turtle.left(180)
            elif instruction == "[": # Sauvegarder la position courante (∈ S) ;
                stack.append(turtle.pos())
            elif instruction == "]": # Restaurer la dernière position sauvée (∈ S).
                pos = stack.pop()
                turtle.penup()
                turtle.goto(pos[0],pos[1])
                turtle.pendown()
    
    # TODO: LSYSTEM USER INPUT


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
