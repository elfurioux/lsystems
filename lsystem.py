import turtle
import os

MVAL = 0b11111111 # Max value <=> 255
NVAL = 0b00000000 # Min value <=> 0

C_PURE_WHITE     = (MVAL,MVAL,MVAL)
C_PURE_BLACK     = (0,0,0)

C_PURE_RED       = (MVAL,0,0)
C_PURE_GREEN     = (0,MVAL,0)
C_PURE_BLUE      = (0,0,MVAL)

C_PURE_YELLOW    = (MVAL,MVAL,0)
C_PURE_CYAN      = (0,MVAL,MVAL)
C_PURE_PURPLE    = (MVAL,0,MVAL)

C_DEFAULT        = C_PURE_BLACK
C_COLORID        = [
    C_DEFAULT,
    C_PURE_RED,
    C_PURE_GREEN,
    C_PURE_BLUE,
    (127,80,32), # BROWN
    C_PURE_YELLOW,
    (MVAL,127,0)  # ORANGE
]


def turtle_setup(title: str):
    """Turtle initialisation procedure, put the turtle at the bottom of the window,
    in the middle, facing upwards, ready to draw a tree for example."""
    turtle.mode("logo")
    turtle.title(titlestring=title)

    turtle.colormode(MVAL)
    turtle.color(C_DEFAULT)

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

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        if instruction not in ALLOWED_INSTRUCTIONS:
            i += 1
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
            stack.append((turtle.pos(),turtle.heading(),turtle.color()))
        elif instruction == "]": # Restaurer la dernière position sauvée (∈ S).
            pos, hd, c = stack.pop()
            turtle.penup()
            turtle.goto(pos[0],pos[1])
            turtle.setheading(hd)
            turtle.color(c)
            turtle.pendown()

        ### NONSTANDARD
        elif instruction == "@": # Color instruction
            i += 1
            if instructions[i] in "0123456":
                c = int(instructions[i])
                turtle.color(C_COLORID[c])
            else:
                print(f"Unknown color \"{instructions[i]}\"")
                turtle.color(C_DEFAULT)
        
        i += 1


class LSysFileError(OSError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class LSystem: ...
class LSystem:
    def __init__(self, axiom: str, rules: dict[str], angle: float, lenght: float) -> None:
        self.axiom: str         = axiom
        self.rules: dict[str]   = rules
        self.angle: float       = angle
        self.lenght: float      = lenght

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

    def draw_lsyst(self, iterations: int, baseangle = 0, title = "unnamed") -> None:
        """Main draturtle_setupwing function, takes in parameter a set of rules (`self`)
        and a number of `iterations` of the rules to draw."""
        
        turtle_setup(title, f"G:{iterations}; L:{self.lenght}; A:{self.angle}")
        turtle.setheading(baseangle)
        draw_instructions(
            instructions = self.getiteration(iterations),
            lenght = self.lenght,
            angle = self.angle
        )
        turtle_end()

    def save(self, path: str, filename: str) -> bool:
        """Saves in `path` the lsystem in a file named "`name`.lsys" ;
        Return `True` if success, `False` otherwise."""
        
        if not os.path.isdir(path):
            print(f"ERREUR: Le dossier \"{path}\" n'existe pas.")
            return False

        fpath = os.path.join(path, filename.removesuffix(".lsys")+".lsys")
        if os.path.isfile(fpath):
            print(f"ERREUR: Le fichier nommé \"{filename}\" existe déja dans le répertoire \"{path}\"")
            return False
        
        b: bytearray = b"\x00\x01" # Version du format de fichier: actuellement 1ere version 00 01
        b += len(self.axiom).to_bytes(2,'big') # Sur 2 octets: la longueur (en octets) de la chaine de char de l'axiome
        b += self.axiom.encode("ascii") # l'axiome encodé en ASCII: pour que chaque charactere prenne 1 octet

        b += len(self.rules).to_bytes(2,'big') # Sur 2 octets: le nombre (en octets) de regles.
        for r in self.rules:
            s = bytearray()
            s += r.encode("ascii") + b'\x00' + self.rules[r].encode("ascii") # met dans s la ligne self.rules[r] de l'axiome
            s = (len(s)+1).to_bytes(2,'big') + s + b'\x00'
            b += s # ajoute la ligne s dans b

        angleN, angleD = self.angle.as_integer_ratio()
        lenghtN, lenghtD = self.lenght.as_integer_ratio()

        b += angleN.to_bytes(8,'big') + angleD.to_bytes(8,'big')
        b += lenghtN.to_bytes(8,'big') + lenghtD.to_bytes(8,'big')

        with open(file=fpath, mode="wb") as fstream:
            fstream.write(b)
        
        return True

    @staticmethod
    def load(path: str, filename: str) -> LSystem:
        oAxiom = None
        oRules = {}
        oAngle = None
        oLenght = None

        fpath = os.path.join(path,filename.removesuffix(".lsys")+".lsys")
        if not os.path.isfile(fpath):
            print(f"ERREUR: Impossible de charger \"{fpath}\", le fichier n'existe pas.")
            raise FileNotFoundError()

        with open(file=fpath,mode="rb") as fstream:
            version = fstream.read(2)
            if version != b"\x00\x01":
                raise LSysFileError(f"ERREUR DE LECTURE: Numéro de version incorrect. (0x{version.hex()})")

            axiomLen = int.from_bytes(fstream.read(2),'big')
            s = bytearray()
            for _ in range(axiomLen):
                s += fstream.read(1)
            oAxiom = s.decode("ascii")

            dictLen = int.from_bytes(fstream.read(2),'big')
            for _ in range(dictLen):
                ruleLen = int.from_bytes(fstream.read(2),'big')
                nulByteReached = False
                ruleKey = bytearray()
                ruleValue = bytearray()
                for _ in range(ruleLen):
                    c = fstream.read(1)
                    if not nulByteReached:
                        if c == b'\x00':
                            nulByteReached = True
                            continue
                        ruleKey += c
                    else:
                        if c == b'\x00': continue
                        ruleValue += c
                oRules[ruleKey.decode("ascii")] = ruleValue.decode("ascii")
            
            angleN = int.from_bytes(fstream.read(8),'big')
            angleD = int.from_bytes(fstream.read(8),'big')
            oAngle = angleN/angleD

            lenghtN = int.from_bytes(fstream.read(8),'big')
            lenghtD = int.from_bytes(fstream.read(8),'big')
            oLenght = lenghtN/lenghtD

        return LSystem(axiom=oAxiom,rules=oRules,angle=oAngle,lenght=oLenght)

class Plsystem(LSystem):
    def __init__(self, /, axiom: str, rules: dict[str], angle: float, lenght: float, title: str = "unnamed", baseangle: float = 0.0) -> None:
        super().__init__(axiom, rules, angle, lenght)
        self.title: str         = title
        self.baseangle: float   = baseangle

    def draw_lsyst(self, iterations: int) -> None:
        return super().draw_lsyst(iterations, self.baseangle, self.title)

    def save(self, path: str) -> bool:
        return super().save(path=path, filename=self.title)
