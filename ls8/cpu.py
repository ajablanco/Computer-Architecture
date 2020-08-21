"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        # memory
        self.ram = [0] * 256
        # registers
        self.reg = [0] * 8
        # program counter
        self.pc = 0
        # stack pointer
        self.sp = 7
        self.op_size = 1
        # running
        self.running = True

        # add flag
        self.fl = 0b00000000

        self.branchtable = {
            0b00000001: self.HLT,
            0b10000010: self.LDI,
            0b01000111: self.PRN,
            0b10100000: self.ADD,
            0b10100010: self.MUL,
            0b01000101: self.PUSH,
            0b01000110: self.POP,
            0b01010000: self.CALL,
            0b00010001: self.RET,
            0b10100111: self.CMP,
            0b01010100: self.JMP,
            0b01010101: self.JEQ,
            0b01010110: self.JNE,
            0b10101000: self.AND,
            0b10101010: self.OR,
            0b10101011: self.XOR
        }


    # MAR == ADDRESS
    def ram_read(self, MAR):
        return self.ram[MAR]
    
    # MDR == VALUE
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

    # op methods
    def HLT(self, operand_a, operand_b):
        self.running = False
        self.pc += 1

    def LDI(self, operand_a, operand_b):
        self.reg[operand_a] = operand_b
        self.pc += 3

    def PRN(self, operand_a, operand_b):
        num = self.reg[operand_a]
        print(num)
        self.pc += 2

    def ADD(self, operand_a, operand_b):
        self.alu("ADD", operand_a, operand_b)
        self.pc += 3

    def MUL(self, operand_a, operand_b):
        self.alu("MUL", operand_a, operand_b)
        self.pc += 3

    def PUSH(self, operand_a, operand_b):
        reg_index = self.ram[self.pc + 1]
        value = self.reg[reg_index]
        # decrement for PUSH
        self.reg[self.sp] -= 1

        self.ram[self.reg[self.sp]] = value
        self.pc += 2

    def POP(self, operand_a, operand_b):
        reg_index = self.ram[self.pc + 1]
        value = self.ram[self.reg[self.sp]]

        self.reg[reg_index] = value
        # incremenet for POP
        self.reg[self.sp] += 1

        self.pc += 2
    def CALL(self, operand_a, operand_b):
        self.reg[self.sp] -= 1
        self.ram[self.reg[self.sp]] = self.pc + 2
        reg_index = self.ram[self.pc + 1]
        self.pc = self.reg[reg_index]

    def RET(self, operand_a, operand_b):
        self.pc = self.ram[self.reg[self.sp]]
        self.reg[self.sp] += 1

    def CMP(self, operand_a, operand_b):
        self.alu("CMP", operand_a, operand_b)
        self.pc += 3

    def JMP(self, operand_a, operand_b):
        self.pc = self.reg[operand_a]

    def JEQ(self, operand_a, operand_b):
        if self.fl == 0b00000001:
            self.pc = self.reg[operand_a]
        else:
            self.pc += 2

    def JNE(self, operand_a, operand_b):
        if self.fl != 1:
            self.pc = self.reg[operand_a]
        else:
            self.pc += 2

    def AND(self, operand_a, operand_b):
        self.alu("AND", operand_a, operand_b)
        self.pc += 3

    def OR(self, operand_a, operand_b):
        self.alu("OR", operand_a, operand_b)
        self.pc += 3

    def XOR(self, operand_a, operand_b):
        self.alu("XOR", operand_a, operand_b)
        self.pc += 3

    def load(self, filename):
        """Load a program into memory."""
        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    split_comment = line.split("#")
                    n = split_comment[0].strip()
                    if n == '':
                        continue
                    value = int(n, 2)
                    self.ram[address] = value
                    address += 1
        except FileNotFoundError:
            print(f"{sys.argv[0]}: {filename} not found")

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
#         `FL` bits: `00000LGE`
        elif op == "CMP":
# * `L` Less-than: during a `CMP`, set to 1 if registerA is less than registerB,
#   zero otherwise.
            if self.reg[reg_b] > self.reg[reg_a]:
                self.fl = 0b00000100
# * `G` Greater-than: during a `CMP`, set to 1 if registerA is greater than
#   registerB, zero otherwise.
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.fl = 0b00000010
# * `E` Equal: during a `CMP`, set to 1 if registerA is equal to registerB, zero
#   otherwise.
            elif self.reg[reg_b] == self.reg[reg_a]:
                self.fl = 0b00000001
        elif op == "AND":
            self.reg[reg_a] &= self.reg[reg_b]

        elif op == "OR":
            self.reg[reg_a] |= self.reg[reg_b]

        elif op == "XOR":
            self.reg[reg_a] ^= self.reg[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc, #program counter
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running is True:

            # read memory adderss in pc
            # store result in "IR" (variable) instruction register
            ir = self.ram[self.pc]

            # using ram_read , read bytes at PC+1 and PC+2
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            self.branchtable[ir](operand_a, operand_b)