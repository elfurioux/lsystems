
import turtle

def turtle_setup(title: str):
    """Turtle initialisation procedure, put the turtle at the bottom of the window,
    in the middle, facing upwards, ready to draw a tree for example."""
    turtle.mode("logo")
    turtle.title(titlestring=title)

    turtle.penup()
    turtle.goto(0, -turtle.window_height()//2-5)
    turtle.pendown()

    turtle.speed(0)

def turtle_end():
    """Turtle end procedure, keeps the window open and hides the cursor."""
    turtle.hideturtle()
    turtle.done()


def draw_instructions(instructions: str, lenght: float, angle: float):
    """Main drawing function, takes a string of instructions and draws it on the screen,
    WARNING: The function just draw the rules set, it does not initialize nor end the turtle,
    use `turtle_setup()` and `turtle_end()` procedures for this.
    TODO: le reste des instructions"""

    NUMBERS = "0123456789"
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALLOWED_INSTRUCTIONS = "+-&^<>|[]" + LETTERS + LETTERS.lower() + NUMBERS

    stack: list[turtle.Vec2D] = []

    for i, instruction in enumerate(instructions):
        if instruction not in ALLOWED_INSTRUCTIONS:
            continue
        
        # print(f"{i}: {instruction}")

        ### MOVEMENT INSTRUCTIONS
        if instruction.upper() in LETTERS or instruction in NUMBERS: # Se déplacer d’un pas unitaire (∈ V) ;
            turtle.forward(lenght)
        
        ### ROTATION INSTRUCTIONS
        elif instruction == "|": # Tourner sur soi-même de 180° (∈ S) ;
            turtle.left(180)
        elif instruction == "+": # Tourner à gauche d’angle α (∈ S) ;
            turtle.right(angle)
        elif instruction == "-": # Tourner à droite d’un angle α (∈ S) ;
            turtle.left(angle)
        
        elif instruction == "<": # Roulez vers la gauche d’un angle α (∈ S) ;
            raise Exception("Not Implemented")
            # turtle.setheading(angle)
            # print("<: angle=",turtle.heading())
        elif instruction == ">": # Roulez vers la droite d’un angle α (∈ S) ;
            raise Exception("Not Implemented")
            # turtle.setheading(360-angle)
            # print(">: angle=",turtle.heading())
        elif instruction == "&": # Pivoter vers le bas d’un angle α (∈ S) ;
            raise Exception("Not Implemented")
        elif instruction == "^": # Pivoter vers le haut d’un angle α (∈ S) ;
            raise Exception("Not Implemented")
        
        ### SAVE/RESTORE INSTRUCTIONS
        elif instruction == "[": # Sauvegarder la position courante (∈ S) ;
            stack.append((turtle.pos(),turtle.heading()))
        elif instruction == "]": # Restaurer la dernière position sauvée (∈ S).
            pos, hd = stack.pop()
            turtle.penup()
            turtle.goto(pos[0],pos[1])
            turtle.setheading(hd)
            turtle.pendown()

class LSystem:
    def __init__(self, axiom: str, rules: dict[str], angle: float, lenght: float, title: str = "") -> None:
        self.axiom: str         = axiom
        self.rules: dict[str]   = rules
        self.angle: float       = angle
        self.lenght: float      = lenght
        self.title: str         = title

    ### L SYTEM GENERATION

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

    def draw_lsyst(self, iterations: int, baseangle = 0) -> None:
        """Main draturtle_setupwing function, takes in parameter a set of rules (`self`)
        and a number of `iterations` of the rules to draw."""
        
        turtle_setup(self.title + f" G:{iterations}; L:{self.lenght}; A:{self.angle}")
        turtle.setheading(baseangle)
        draw_instructions(
            instructions = self.getiteration(iterations),
            lenght = self.lenght,
            angle = self.angle
        )
        turtle_end()
    
    ### TODO: LSYSTEM USER INPUT
