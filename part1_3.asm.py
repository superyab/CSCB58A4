from codetypes import *

CODE = [
    Word(0xE3510000),  # CMP R1, #0
    Word(0x1A000002),  # BNE 2 (go return)
    Word(0xE3E05000),  # MVN R5, #0  
    Word(0xE3E06000),  # MVN R6, #0  
    Word(0xE1A0F00E),  # MOV R15, R14 (return)
    Word(0xE3A05000),  # divide: MOV R5, #0  
    Word(0xE1500001),  # CMP R0, R1
    Word(0xBA000002),  # BLT 2 (go return)
    Word(0xE0400001),  # SUB R0, R0, R1
    Word(0xE2855001),  # ADD R5, R5, #1
    Word(0xEAFFFFFA),  # B -6 (back to CMP)
    Word(0xE1A0F00E),  # MOV R15, R14 (return)
]