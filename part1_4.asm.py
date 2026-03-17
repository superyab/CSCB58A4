from codetypes import *

CODE = [
    Word(0xE1A01600),  # MOV R1, R0, LSL #12  (R1 = v << 12)
    Word(0xE28F2008),  # ADD R2, PC, #8       (R2 = addr of ADD instr at 0x14)
    Word(0xE5923000),  # LDR R3, [R2]         (R3 = ADD instruction from memory)
    Word(0xE1833001),  # ORR R3, R3, R1       (modify Rd field to Rv)
    Word(0xE5823000),  # STR R3, [R2]         (write modified instruction back)
    Word(0xE08D0000),  # ADD R0, R13, R0      (modified at runtime to ADD Rv, R13, R0)
    Word(0xE1A0F00E),  # MOV PC, LR           (return)
]
