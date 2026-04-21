# Goat-Language

`EAT n` = Push number n onto the stack  
POOP = Pop the top value of the stack  
CLONE = Duplicate the top value of the stack  
HEADBUTT = Swap the top two values of the stack  
HERD_HOME = Move the top value to the bottom  
HERD_AWAY = Move the bottom value to the top  

LACTATE = Add top two values  
SHEAR = Subtract top from second (b - a)  
BREED = Multiply top two values  

ABSORB = Read integer input and push to stack  
SWALLOW = Read string and push characters (ASCII) to stack  
NOT_A_CAT = Read input and print it immediately  

GOAT_INT = Print top value as integer  
GOAT_CHAR = Print top value as character  
BLEAT "text" = Print string literal  

CHECK_FEET label = Jump if top value is 0  
CHECK_HORNS label = Jump if top value > 0  

CHOMP_ENDS = Compare first and last characters, remove both, push result  
DEPTH_LTE2 = Push 1 if stack size ≤ 2, else 0  

SLAUGHTER = Terminate program

How to run:

Type in terminal:
python goat.py examples/example.txt
