class Memory_sort:
    def __init__(self):
        self.data_Memory_sort = [0] * 1000

    def get_instructions(self):
        return [
            "00000000000010100110000000100000",
            "00000000000010010111000000100000",
            "00000001110010010111000000100000",
            "00000001110010010111000000100000",
            "00000001110010010111000000100000",
            "00000001110010100111000000100000",
            "00000000000011100111100000100000",
            "00100001111011111111111111111100",
            "00010001100011100000000000010001",
            "00000000000010100110100000100000",
            "00010001101011010000000000000011",
            "00100001100011000000000000000100",
            "00100001111011111111111111111100",
            "00010001100011001111111111111010",
            "00010001101011111111111111111100",
            "10001101101110000000000000000100",
            "10001101101110010000000000000000",
            "00000011000110011100100000101010",
            "00100011001110011111111111111111",
            "00010011001000000000000000000010",
            "00100001101011010000000000000100",
            "00010001101011011111111111111000",
            "10001101101110010000000000000000",
            "10101101101110010000000000000100",
            "10101101101110000000000000000000",
            "00010011001110011111111111111010"
            
            # "00100100000011000000000000000000", 
            # "00100100000010000000000000000001",
            # "00100100000011100000000000000000",
            # "00100001100011000000000000000001",
            # "00100001000010000000000000001010",
            # "00100001110011100000000000000001",
            # "00010001000011100000000000000110",
            # "00000001100000000110000000100000",
            # "00100001000010001111111111111111", 
            # "00000001100000000110000000100000",
            # "01110001100010000110000000000010", 
            # "00100001000010000000000000000000",
            # "00010001000010001111111111111001",
            # "00100001111011110000000000000000"
        ]

    def data_memory(self):
        return self.data_Memory_sort

    def data_values(self, address):
        if 0 <= address < len(self.data_Memory_sort):
            return self.data_Memory_sort[address]
        return 0

    def setdatavalue(self, address, value):
        while len(self.data_Memory_sort) <= address:
            self.data_Memory_sort.append(0)
        self.data_Memory_sort[address] = value


class _Register__Sorts_:
    def __init__(self):
        self._Register__Sorts_s = {}

    def register_value(self, reg):
        return self._Register__Sorts_s.get(reg, 0)

    def set__Register__Sorts__value(self, reg, value):
        self._Register__Sorts_s[reg] = value


class Decode__sort:
    def __init__(self, opcode, rs, rt, rd, shamt, funct, imm, address):
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct
        self.imm = imm
        self.address = address


def execute_sort_(instruction, data, _Register__Sorts_s):
    opcode = instruction.opcode
    rs = instruction.rs
    rt = instruction.rt
    rd = instruction.rd
    funct = instruction.funct
    imm = instruction.imm
    address = instruction.address

    if opcode == "000000":  # R-type instructions
        if funct == "100000":  # ADD
            print("i am in add")
            _Register__Sorts_s.set__Register__Sorts__value(rd, _Register__Sorts_s.register_value(rs) + _Register__Sorts_s.register_value(rt))
            
            print(_Register__Sorts_s.register_value(rs))
            print(_Register__Sorts_s.register_value(rt))
            
        
        elif funct == "101010":  # SLT
            print("i am slt")
            if _Register__Sorts_s.register_value(rs) < _Register__Sorts_s.register_value(rt):
                _Register__Sorts_s.set__Register__Sorts__value(rd, 1)
                print(_Register__Sorts_s.register_value(rs))
                print(_Register__Sorts_s.register_value(rt))
            else:
                _Register__Sorts_s.set__Register__Sorts__value(rd, 0)
                print(_Register__Sorts_s.register_value(rs))
                print(_Register__Sorts_s.register_value(rt))

    elif opcode == "001000":  # ADDI
        print("i am in addi")

        # Decode__sort the immediate value from binary to integer
        _immediatevalue_ = int(imm, 2)

        # Handle negative immediate values
        if _immediatevalue_ >= 0 and _immediatevalue_ <= 32767:
            _Register__Sorts_s.set__Register__Sorts__value(rt, _Register__Sorts_s.register_value(rs) + _immediatevalue_)
        else:
            # If the immediate value is negative, convert it to a negative integer
            negative_immediate = _immediatevalue_ - 65536
            _Register__Sorts_s.set__Register__Sorts__value(rt, _Register__Sorts_s.register_value(rs) + negative_immediate)

        # Print the result
        print(_Register__Sorts_s.register_value(rt))


    

    elif opcode == "100011":  # LW
        print("lw")
        base_value = _Register__Sorts_s.register_value(rs)
        offset = int(imm, 2)
        Memory_sort_address = base_value + offset
        loaded_value = data.get_data_value(Memory_sort_address)
        _Register__Sorts_s.set__Register__Sorts__value(rt, loaded_value)
        print(_Register__Sorts_s.register_value(rs))
        print(_Register__Sorts_s.register_value(rt))
        
    elif opcode == "011100":  # MUL
        result = _Register__Sorts_s.register_value(rs) * _Register__Sorts_s.register_value(rt)
        _Register__Sorts_s.set__Register__Sorts__value(rd, result)

    elif opcode == "101011":  # SW
        print("sw")
        base_value_sw = _Register__Sorts_s.register_value(rs)
        offset_sw = int(imm, 2)
        Memory_sort_address_sw = base_value_sw + offset_sw
        value_to_store = _Register__Sorts_s.register_value(rt)
        data.set_data_value(Memory_sort_address_sw, value_to_store)
        print(_Register__Sorts_s.register_value(rs))
        print(_Register__Sorts_s.register_value(rt))


    if opcode == "000100":  # BEQ
        print("i am in beq")
        branch_offset = int(imm, 2)
        
        # Check if the branch offset is negative
        if imm[0] == '1':
           branch_offset -= 65536
    
        branch_offset *= 4
    
        offseta =branch_offset
        print(_Register__Sorts_s.register_value(rs), _Register__Sorts_s.register_value(rt))
    
        if _Register__Sorts_s.register_value(rs) == _Register__Sorts_s.register_value(rt):
            branch_address = _Register__Sorts_s.register_value("11111") + offseta + 4
            _Register__Sorts_s.set__Register__Sorts__value("11111", branch_address)
        else:
            _Register__Sorts_s.set__Register__Sorts__value("11111", _Register__Sorts_s.register_value("11111") + 4)

    
    elif opcode == "001001":  # LI
        _Register__Sorts_s.set__Register__Sorts__value(rt, int(imm, 2))
        
    else:
        print("wrng opcode", opcode)
        
#code for factorial
class Memory:
    def __init__(self):
        self.data_memory = [0] * 1000

    def get_fact_instructions(self):
        return [
            "00100100000011000000000000000000", "00100100000010000000000000000001",
            "00100100000011100000000000000000", "00100001100011000000000000000001",
            "00100001000010000000000000001010", "00100001110011100000000000000001",
            "00010001000011100000000000000110", "00000001100000000110000000100000",
            "00100001000010001111111111111111", "00000001100000000110000000100000",
            "01110001100010000110000000000010", "00100001000010000000000000000000",
            "00010001000010001111111111111001", "00100001111011110000000000000000"
        ]

    def get_data_memory(self):
        return self.data_memory

    def data_values(self, address): #to get the data value
        if 0 <= address < len(self.data_memory):
            return self.data_memory[address]
        return 0

    def set_data_value(self, address, value):#to set data values
        while len(self.data_memory) <= address:
            self.data_memory.append(0)
        self.data_memory[address] = value

#defining,setting,getting registers
class Register:
    def __init__(self):
        self.registers = {}

    def get_register_value(self, reg):
        return self.registers.get(reg, 0)

    def set_register_value(self, reg, value):
        self.registers[reg] = value

#to decode the instruction to opcode,rs,rt and so on for r,i,j type instructions
class Decode:
    def __init__(self, opcode, rs, rt, rd, shamt, funct, imm, address):
        self.opcode = opcode
        self.rs = rs
        self.rt = rt
        self.rd = rd
        self.shamt = shamt
        self.funct = funct
        self.imm = imm
        self.address = address

#here we start to execute by identifying the opcode decoding it and doing that particular operation.
def execute_instruction(instruction, data, registers):
    opcode = instruction.opcode
    rs = instruction.rs
    rt = instruction.rt
    rd = instruction.rd
    funct = instruction.funct
    imm = instruction.imm
    address = instruction.address

    if opcode == "000000":  # R-type instructions
        if funct == "100000":  #  to ADD 2 numbers
            registers.set_register_value(rd, registers.get_register_value(rs) + registers.get_register_value(rt))
        elif funct == "100010":  # to SUB 2 numbers
            registers.set_register_value(rd, registers.get_register_value(rs) - registers.get_register_value(rt))
        elif funct == "011000":  # to MUL 2 numbers
            registers.set_register_value(rd, registers.get_register_value(rs) * registers.get_register_value(rt))
        elif funct == "101010":  #  for SLT
            if registers.get_register_value(rs) < registers.get_register_value(rt):
                registers.set_register_value(rd, 1)
            else:
                registers.set_register_value(rd, 0)

    elif opcode == "001000":  # ADDI
        _immediatevalue_ = int(imm, 2)
        if 0 <= _immediatevalue_ <= 32767:
            registers.set_register_value(rt, registers.get_register_value(rs) + _immediatevalue_)
        else:
            negative_immediate = _immediatevalue_ - 65536
            registers.set_register_value(rt, registers.get_register_value(rs) + negative_immediate)

    elif opcode == "100011":  # to LW the operation
        base_value = registers.get_register_value(rs)
        offset = int(imm, 2)
        memory_address = base_value + offset
        loaded_value = data.get_data_value(memory_address)
        registers.set_register_value(rt, loaded_value)

    elif opcode == "011100":  # MUL
        result = registers.get_register_value(rs) * registers.get_register_value(rt)
        registers.set_register_value(rd, result)

    elif opcode == "101011":  # to SW the operation
        base_value_sw = registers.get_register_value(rs)
        offset_sw = int(imm, 2)
        memory_address_sw = base_value_sw + offset_sw
        value_to_store = registers.get_register_value(rt)
        data.set_data_value(memory_address_sw, value_to_store)

    elif opcode == "000010":  # Jump instruction
        jump_address = int(address, 2) * 4
        registers.set_register_value("11111", jump_address)

    elif opcode == "000100":  # BEQ
       branch_offset = int(imm, 2)
       if imm[0] == '1':
            branch_offset = -(65536 -branch_offset)
       branch_offset *= 4
       if registers.get_register_value(rs) == registers.get_register_value(rt):
            branch_address = registers.get_register_value("11111") +branch_offset + 4
            registers.set_register_value("11111", branch_address)
       else:
            registers.set_register_value("11111", registers.get_register_value("11111") + 4)

    elif opcode == "001001":  # LI for the factorial part
        registers.set_register_value(rt, int(imm, 2))

    else:
        print("new opcode", opcode)



def main():
    
    scanner = input
    
    k=int(scanner())
    
    if k==1:
        data = Memory_sort()
        _Register__Sorts_s = _Register__Sorts_()

        instructions = data.get_instructions()
        Decode__sortd_array = [Decode__sort(inst[0:6], inst[6:11], inst[11:16], inst[16:21],
                                inst[21:26], inst[26:32], inst[16:32], inst[16:31]) for inst in instructions]
    # the number of integers for sorting
        print("n= ")
        n = int(scanner())
        _Register__Sorts_s.set__Register__Sorts__value("01001", n)
    #for the input of inpt address
        print("Enter the intpt add: ")
        input_address = scanner()
        _Register__Sorts_s.set__Register__Sorts__value("01010", int(input_address, 2))
    #for the inpt of output addrress
        print("Enter the outpt add: ")
        output_address = scanner()
        _Register__Sorts_s.set__Register__Sorts__value("01011", int(output_address, 2))

        data_Memory_sort_address = _Register__Sorts_s.register_value("01010")
        las = data_Memory_sort_address

        for i in range(n):
            print(f"Enter integer value {i + 1}: ")
            input_value = int(scanner())
            data.set_data_value(data_Memory_sort_address, input_value)
            data_Memory_sort_address += 4

        cycles = 0

        while _Register__Sorts_s.register_value("11111") < len(instructions) * 4:
            cycles += 1
            instruction = Decode__sortd_array[_Register__Sorts_s.register_value("11111") // 4]

            if instruction.opcode == "000100":
                execute_sort_(instruction, data, _Register__Sorts_s)
            elif instruction.opcode == "000010":
                execute_sort_(instruction, data, _Register__Sorts_s)
            else:
                execute_sort_(instruction, data, _Register__Sorts_s)
                if instruction.opcode != "000100":
                    _Register__Sorts_s.set__Register__Sorts__value("11111", ((_Register__Sorts_s.register_value("11111") // 4) + 1) * 4)

        print("Output Memory_sort:")
        for i in range(n):
            output_value = data.get_data_value(las)
            print(f"Output {i + 1}: {output_value}")
            las += 4

        print("Number of cycles taken:", cycles)
    elif k==2:
        data = Memory()
        registers = Register()

        instructions = data.get_fact_instructions()
        decoded_array = [Decode(inst[0:6], inst[6:11], inst[11:16], inst[16:21],
                                inst[21:26], inst[26:32], inst[16:32], inst[16:31]) for inst in instructions]

        cycles = 0

        while registers.get_register_value("11111") < len(instructions) * 4:
            cycles += 1
            instruction = decoded_array[registers.get_register_value("11111") // 4]

            if instruction.opcode == "000100":
                execute_instruction(instruction, data, registers)
            elif instruction.opcode == "000010":
                execute_instruction(instruction, data, registers)
            else:
                execute_instruction(instruction, data, registers)
                if instruction.opcode != "000100":
                    registers.set_register_value("11111", ((registers.get_register_value("11111") // 4) + 1) * 4)

        print("Output Memory:")
        print(registers.get_register_value("01100"))

        print("Number of cycles taken:", cycles)

if __name__ == "__main__":
    main()
