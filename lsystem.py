
import turtle

def turtle_setup():
    """Turtle initialisation procedure, put the turtle at the bottom of the window,
    in the middle, facing upwards, ready to draw a tree for example."""
    turtle.penup()
    turtle.goto(0, -turtle.window_height()//2-10)
    turtle.pendown()

    turtle.setheading(90)
    turtle.speed(0)

def turtle_end():
    """Turtle end procedure, keeps the window open and hides the cursor."""
    turtle.hideturtle()
    turtle.done()

def draw_instructions(instructions: str, lenght: float, angle: float):
    """Main drawing function, takes a string of instructions and draws it on the screen,
    WARNING: The function just draw the rules set, it does not initialize nor end the turtle,
    use `turtle_setup()` and `turtle_end()` procedures for this."""
    ALLOWED_INSTRUCTIONS = "FXY+-&^<>|[]"

    stack: list[turtle.Vec2D] = []

    for instruction in instructions:
        if instruction not in ALLOWED_INSTRUCTIONS:
            continue
        
        if instruction in "FXY": # Se déplacer d’un pas unitaire (∈ V) ;
            turtle.forward(lenght)
        elif instruction == "+": # Tourner à gauche d’angle α (∈ S) ;
            turtle.left(angle)
        elif instruction == "-": # Tourner à droite d’un angle α (∈ S) ;
            turtle.right(angle)
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

class LSystem:
    def __init__(self, axiom: str, rules: dict[str], angle: float, lenght: float) -> None:
        self.axiom: str         = axiom
        self.rules: dict[str]   = rules
        self.angle: float       = angle
        self.lenght: float      = lenght

    # L SYTEM GENERATION

    def geniterations(self, iterations: int) -> list[str]:
        """Generate a certain number of iterations of the rules set, then returns
        them in a list, where the Nth index of the list corresponds to the Nth iteration."""
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
        """Get the Nth iteration of the set of rules."""
        return self.geniterations(iterations=iteration)[-1]

    # L SYSTEM REPRESENTATION

    def draw_lsyst(self, iterations: int) -> None:
        """Main drawing function, takes in parameter a set of rules (`self`)
        and a number of `iterations` of the rules to draw."""
        
        turtle_setup()
        draw_instructions(
            instructions = self.getiteration(iterations),
            lenght = self.lenght,
            angle = self.angle
        )
        turtle_end()
    
    # TODO: LSYSTEM USER INPUT

