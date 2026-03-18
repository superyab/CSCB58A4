#!/usr/bin/python3
import sys
from codetypes import *
from wordasm import *

def lowerAssemblyCode(code: list[AssemblyCode]) -> list[Word]:
    """ Lowers away AssemblyCode instructions. """
    for assemblyCode in code:
        match assemblyCode:
            case Add(rd, r1, op2, cond):
                cond_bits = cond.value       
                rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       

                opcode = 0b0100              
                S = 0                        

                if isinstance(op2, Reg):
                    rm_bits = op2.reg & 0xF  
                    I = 0                    
                    instruction = (
                        (cond_bits << 28) |
                        (0b00 << 26) |      
                        (I << 25) |          
                        (opcode << 21) |   
                        (S << 20) |          
                        (r1_bits << 16) |   
                        (rd_bits << 12) |    
                        rm_bits              
                    )
                else:
                    imm = op2.value & 0xFFF
                    I = 1                    

                    instruction = (
                        (cond_bits << 28) |
                        (0b00 << 26) |
                        (I << 25) |
                        (opcode << 21) |
                        (S << 20) |
                        (r1_bits << 16) |
                        (rd_bits << 12) |
                        imm                   
                    )
                code.append(Word(instruction))
            case Sub(rd, r1, op2, cond):
                cond_bits = cond.value       
                rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       

                opcode = 0b0010              
                S = 0
                type_bits = 0 & 0b00                        

                if isinstance(op2, Reg):
                    rm_bits = op2.reg & 0xF  
                    I = 0                    
                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |      
                        (I << 25) |          
                        (opcode << 21) |   
                        (S << 20) |          
                        (r1_bits << 16) |   
                        (rd_bits << 12) |    
                        rm_bits              
                    )
                else:
                    imm = op2.value & 0xFFF
                    I = 1                    

                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |
                        (I << 25) |
                        (opcode << 21) |
                        (S << 20) |
                        (r1_bits << 16) |
                        (rd_bits << 12) |
                        imm                   
                    )
                code.append(Word(instruction))
            case Cmp(r1, op2, cond):
                cond_bits = cond.value       
                #rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       

                opcode = 0b1010              
                S = 1
                type_bits = 0 & 0b00                        

                if isinstance(op2, Reg):
                    rm_bits = op2.reg & 0xF  
                    I = 0                    
                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |      
                        (I << 25) |          
                        (opcode << 21) |   
                        (S << 20) |          
                        (r1_bits << 16) |   
                        (0b0000 << 12) |    
                        rm_bits              
                    )
                else:
                    imm = op2.value & 0xFFF
                    I = 1                    

                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |
                        (I << 25) |
                        (opcode << 21) |
                        (S << 20) |
                        (r1_bits << 16) |
                        (0b0000 << 12) |
                        imm                   
                    )
                code.append(Word(instruction))
            case Mov(r1, op2, cond):
                cond_bits = cond.value       
                #rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       

                opcode = 0b1101              
                S = 1
                type_bits = 0 & 0b00                        

                if isinstance(op2, Reg):
                    rm_bits = op2.reg & 0xF  
                    I = 0                    
                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |      
                        (I << 25) |          
                        (opcode << 21) |   
                        (S << 20) |          
                        (r1_bits << 16) |   
                        (0b0000 << 12) |    
                        rm_bits              
                    )
                else:
                    imm = op2.value & 0xFFF
                    I = 1                    

                    instruction = (
                        (cond_bits << 28) |
                        (type_bits << 26) |
                        (I << 25) |
                        (opcode << 21) |
                        (S << 20) |
                        (r1_bits << 16) |
                        (0b0000 << 12) |
                        imm                   
                    )
                code.append(Word(instruction))
            case Mul(rd, r1, r2, cond):
                cond_bits = cond.value       
                rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       
                r2_bits = r2.reg & 0xF       
                opcode_and_s_bits = 0b00000000                        
              
                instruction = (
                    (cond_bits << 28) |
                    (opcode_and_s_bits << 20) |      
                    (rd_bits << 16) |
                    (0b0000 << 12) |
                    (r1_bits << 8) |
                    (0b1001 << 4 ) |
                    (r2_bits << 0)
                )
                code.append(Word(instruction))

            case SDiv(rd, r1, r2, cond):
                cond_bits = cond.value       
                rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       
                r2_bits = r2.reg & 0xF       
                big_type_bits = 0b01110011                        
              
                instruction = (
                    (cond_bits << 28) |
                    (big_type_bits << 20) |      
                    (r1_bits << 16) |
                    (rd_bits << 12) |
                    (0b1111 << 8) |
                    (0b0011 << 4 ) |
                    (r2_bits << 0)
                )
                code.append(Word(instruction))
            case UDiv(rd, r1, r2, cond):
                cond_bits = cond.value       
                rd_bits = rd.reg & 0xF       
                r1_bits = r1.reg & 0xF       
                r2_bits = r2.reg & 0xF       
                big_type_bits = 0b01110001                        
              
                instruction = (
                    (cond_bits << 28) |
                    (big_type_bits << 20) |      
                    (r1_bits << 16) |
                    (rd_bits << 12) |
                    (0b1111 << 8) |
                    (0b0001 << 4 ) |
                    (r2_bits << 0)
                )
                code.append(Word(instruction))
            case B(offset, cond):
                cond_bits = cond.value
                opt_code_bits = 0b101
                type_bits = 0b0
                imm_24 = offset.value & 0x00FFFFFF
                instruction = (
                    (cond_bits << 28) |
                    (opt_code_bits << 25) |
                    (type_bits << 24) |
                    imm_24
                )
                code.append(Word(instruction))
            case Bl(offset, cond):
                cond_bits = cond.value
                opt_code_bits = 0b101
                type_bits = 0b1
                imm_24 = offset.value & 0x00FFFFFF
                instruction = (
                    (cond_bits << 28) |
                    (opt_code_bits << 25) |
                    (type_bits << 24) |
                    imm_24
                )
                code.append(Word(instruction))
            case Bx(offset, cond):
                cond_bits = cond.value
                code.append(Word(0x00000000))
            case Blx(offset, cond):
                code.append(Word(0x00000000))
            case Ldr(rd, r1, off, cond):
                code.append(Word(0x00000000))
            case Ldrb(rd, r1, off, cond):
                code.append(Word(0x00000000))
            case Str(rd, r1, off, cond):
                code.append(Word(0x00000000))
            case Strb(rd, r1, off, cond):
                code.append(Word(0x00000000))
    return code

def assembleCode(code: list[AssemblyCode], out = sys.stdout.buffer):
    """ Assembles a List of AssemblyCode objects to the target file. """
    assembleWords(lowerAssemblyCode(code), out)

if __name__ == "__main__":
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(  ), os.O_BINARY)

    parser = argparse.ArgumentParser(
                    prog="labelasm",
                    description="Assembles a sequence of ssemblyCode objects")
    parser.add_argument("filename")
    args = parser.parse_args()
    
    spec = importlib.util.spec_from_file_location("code", args.filename)
    code = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(code)
    assembleCode(code.CODE) 
