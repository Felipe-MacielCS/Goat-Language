import sys

# read the argumest, interpret from this file
program_filepath = sys.argv[1]

# TOKENIZATION -------------------------------------------------------------------------------------------------------------------

# read lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]

program = [] # list of instructions
token_counter = 0 # keep tracks where we are in the program in parsing
label_tracker = {} # keep tracks of which index in our program list a label points to

for line in program_lines:
    parts = line.split(" ")
    opcode = parts[0]
    # check for empty line 
    if opcode == "":
        continue

    # check if it is a label
    if opcode.endswith(":"):
        label_tracker[opcode[:-1]] = token_counter
        continue

    # store opcode token
    program.append(opcode)
    token_counter += 1

    # handle each opcode
    if opcode == "EAT": # PUSH
        # expects a number
        number = int(parts[1])
        program.append(number)
        token_counter += 1
    elif opcode == "BLEAT": # PRINT
        # parse string literal (it might have spaces, so we add the rest of the string and remove "")
        string_literal = " ".join(parts[1:])[1:-1]
        program.append(string_literal)
        token_counter += 1
    elif opcode == "CHECK_FEET": #JUMP.EQ.0
        # reads the label
        label = parts[1]
        program.append(label)
        token_counter += 1
    elif opcode == "CHECK_HORNS": # JUMP.GT.0
        # reads the label
        label = parts[1]
        program.append(label)
        token_counter += 1    

# Interpret -------------------------------------------------------------------------------------------------------------------

class Stack:

    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.sp = -1

    def push(self, number):
        self.sp += 1 # sp = stack pointer
        self.buf[self.sp] = number

    def pop(self):
        number = self.buf[self.sp]
        self.sp -= 1
        return number
    
    # helper function, it does not take any arguments, it returns the top value of the stack without moving the stack pointer
    def top(self):
        return self.buf[self.sp]
    
pc = 0
stack = Stack (256)

while program[pc] != "SLAUGHTER": # Terminates
    opcode = program[pc]
    pc += 1
 
    if opcode == "EAT": # PUSH
        number = program[pc]
        pc += 1

        stack.push(number)
    elif opcode == "POOP": # POP
        stack.pop()
    elif opcode == "LACTATE": # ADD
        a = stack.pop()
        b = stack.pop()
        stack.push(a+b)
    elif opcode == "SHEAR": # SUB
        a = stack.pop()
        b = stack.pop()
        stack.push(b-a)
    elif opcode == "BLEAT": # PRINT
        print(stack.pop()) 
    elif opcode == "BUCKLING": # READ one character (buckling is a baby goat)
        char = input()
        stack.push(ord(char))
    elif opcode == "ABSORB": # READ 
        number = int(input())
        stack.push(number)
    elif opcode == "CHECK_FEET": # JUMP.EQ.0
        number = stack.pop()
        if number == 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "CHECK_HORNS": # JUMP.GT.0
        number = stack.pop()
        if number > 0:
            pc = label_tracker[program[pc]]
        else:
            pc += 1
    elif opcode == "GOAT_CHAR": # Print char
        value = stack.pop()
        print(chr(value), end="")
    elif opcode == "GOAT_INT": # Print int
        value = stack.pop()
        print(value)
    elif opcode == "BREED":  # MULTIPLY
        a = stack.pop()
        b = stack.pop()
        stack.push(a * b)
    elif opcode == "CLONE":  # DUPLICATION
        stack.push(stack.top())
    elif opcode == "HEADBUTT": # SWAP
        a = stack.pop()
        b = stack.pop()
        stack.push(a)
        stack.push(b)
    elif opcode == "HERD_AWAY": # Moves bottom to top
        bottom = stack.buf[0]
        for i in range(stack.sp):
            stack.buf[i] = stack.buf[i + 1]
        stack.buf[stack.sp] = bottom
    elif opcode == "HERD_HOME": # Moves top to bottom
        top = stack.buf[stack.sp]
        for i in range(stack.sp, 0, -1):
            stack.buf[i] = stack.buf[i - 1]
        stack.buf[0] = top