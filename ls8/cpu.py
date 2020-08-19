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
        # running
        self.running = False



    # MAR == ADDRESS
    def ram_read(self, MAR):
        return self.ram[MAR]
    
    # MDR == VALUE
    def ram_write(self, MAR, MDR):
        self.ram[MAR] = MDR

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
        running = True
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001
        ADD = 0b10100000
        MUL = 0b10100010 
        PUSH = 0b01000101
        POP = 0b01000110


        while running:

            # read memory adderss in pc
            # store result in "IR" (variable) instruction register
            ir = self.ram[self.pc]

            # using ram_read , read bytes at PC+1 and PC+2
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            # if-elif?
            if ir == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3
            elif ir == PRN:
                print(self.reg[operand_a])
                self.pc += 2
            elif ir == HLT:
                running = False
                sys.exit()
                self.pc += 1
            elif ir == ADD:
                print(self.reg[operand_a] + self.reg[operand_b])
                self.pc += 3
            elif ir == MUL:
                print(self.reg[operand_a] * self.reg[operand_b])
                self.pc += 3
            elif ir == PUSH:
                reg_index = self.ram[self.pc + 1]
                value = self.reg[reg_index]
                # decrement for PUSH
                self.reg[self.sp] -= 1

                self.ram[self.reg[self.sp]] = value
                self.pc += 2
            elif ir == POP:
                reg_index = self.ram[self.pc + 1]
                value = self.ram[self.reg[self.sp]]

                self.reg[reg_index] = value
                # incremenet for POP
                self.reg[self.sp] += 1

                self.pc += 2
            else:
                print("command not available")
                sys.exit()