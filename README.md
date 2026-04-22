# Goat-Language

| Instruction | Description |
|------------|------------|
| `EAT n` | Push number n onto the stack |
| `POOP` | Pop the top value of the stack |
| `SHEAR` | Subtract top from second (b - a) |
| `BLEAT "text"` | Print string literal |
| `NOT_A_CAT` | Pop value and print it as a character |
| `SWALLOW` | Read string input and push characters (ASCII) onto the stack (ends with 0) |
| `ABSORB` | Read integer input and push to stack |
| `CHECK_FEET label` | Jump to label if top value is 0 (pops value) |
| `CHECK_HORNS label` | Jump to label if top value > 0 (pops value) |
| `GOAT_CHAR` | Pop value and print it as a character (no newline) |
| `GOAT_INT` | Pop value and print it as an integer |
| `BREED` | Multiply top two values |
| `CLONE` | Duplicate the top value of the stack |
| `HEADBUTT` | Swap the top two values of the stack |
| `HERD_AWAY` | Move bottom value of the stack to the top |
| `HERD_HOME` | Move top value of the stack to the bottom |
| `HORN_AND_FOOT` | Compare top and bottom values, remove both, push 1 if equal else 0 |
| `CHECK_GOAT_PAIRS` | Push 1 if stack size ≤ 2, else push 0 |
| `SLAUGHTER` | Terminate the program |

How to run:

Type in terminal:
`python goat.py examples/example.txt`
