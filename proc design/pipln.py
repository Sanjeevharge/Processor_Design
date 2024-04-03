import dataclasses
from typing import Self
class with_pipeln:
    def __init__(self):
        
        self.EX_MEM = None
        self.MEM_WB = None
        self.IF_ID = None
        self.ID_EX = None


class mm_Sorting:
    def __init__(self):
        self.data_mm_Sorting = [0] * 1000

    def Get_ins(self):
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
        ]
    def set_dt_val(self, address, value):
        while len(self.data_mm_Sorting) <= address:
            self.data_mm_Sorting.append(0)
        self.data_mm_Sorting[address] = value
    def get_data_mm_Sorting(self):
        return self.data_mm_Sorting

    def get_dt_val(self, address):
        if 0 <= address < len(self.data_mm_Sorting):
            return self.data_mm_Sorting[address]
        return 0
class Register:
    def __init__(self):
        self.registers = {}

    def get_register_value(self, reg):
        return self.registers.get(reg, 0)

    def set_register_value(self, reg, value):
        self.registers[reg] = value
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
    

def Ex_Inst(instruction, rgs, pipeline_rgs):
      
        funct = instruction.funct
        imm = instruction.imm
        address = instruction.address
        opcode = instruction.opcode
        rs = instruction.rs
        rt = instruction.rt
        rd = instruction.rd

        if opcode == "000000":  # R-type instructions
            if funct == "100000":  # ADD
                result = rgs.get_Register_sort_value(rs) + rgs.get_Register_sort_value(rt)
                pipeline_rgs.EX_MEM = ExecutionResult(result, rd)
        elif opcode == "000100":  # BEQ
            branch_offset = int(imm, 2)
            if imm[0] == '1':
                branch_offset = -(65536 - branch_offset)
            branch_offset *= 4
            if rgs.get_Rg_Val(rs) == rgs.get_Rg_Val(rt):
                branch_address = rgs.get_Rg_Val("11111") + branch_offset + 4
                rgs.set_Rg_Val("11111", branch_address)
            else:
                rgs.set_Rg_Val("11111", rgs.get_Rg_Val("11111") + 4)
       
        elif opcode == "100011":  # LW
            base_value = rgs.get_Register__sort_value(rs)
            offset = int(imm, 2)
            mm_Sorting_address = base_value + offset
            loaded_value = Self.get_dt_val(mm_Sorting_address)
            pipeline_rgs.MEM_WB = ExecutionResult(loaded_value, rt)
        elif opcode == "001000":  # ADDI
            immediate_value = int(imm, 2)
            if 0 <= immediate_value <= 32767:
                result = rgs.get_Register__sort_value(rs) + immediate_value
                pipeline_rgs.EX_MEM = ExecutionResult(result, rt)
            else:
                negative_immediate = immediate_value - 65536
                result = rgs.get_Register__sort_value(rs) + negative_immediate
                pipeline_rgs.EX_MEM = ExecutionResult(result, rt)
        elif opcode == "001001":  # LI for the factorial part
            rgs.set_Rg_Val(rt, int(imm, 2))

        
        elif opcode == "011100":  # MUL
            result = rgs.get_Rg_Val(rs) * rgs.get_Rg_Val(rt)
            rgs.set_Rg_Val(rd, result)

        elif opcode == "101011":  # to SW the operation
            base_value_sw = rgs.get_Rg_Val(rs)
            offset_sw = int(imm, 2)
            memory_address_sw = base_value_sw + offset_sw
            value_to_store = rgs.get_Rg_Val(rt)
            dataclasses.set_dt_val(memory_address_sw, value_to_store)

        elif opcode == "000010":  # Jump instruction
            jump_address = int(address, 2) * 4
            rgs.set_Rg_Val("11111", jump_address)
        else:
            print("new opcode", opcode)

        # Handle data hazards and forwarding
        if pipeline_rgs.EX_MEM is not None and pipeline_rgs.EX_MEM.rd == instruction.rs:
            pipeline_rgs.ID_EX.rs_value = pipeline_rgs.EX_MEM.result
        elif pipeline_rgs.MEM_WB is not None and pipeline_rgs.MEM_WB.rd == instruction.rs:
            pipeline_rgs.ID_EX.rs_value = pipeline_rgs.MEM_WB.result
        else:
            pipeline_rgs.ID_EX.rs_value = rgs.get_Register__sort_value(instruction.rs)

        if pipeline_rgs.EX_MEM is not None and pipeline_rgs.EX_MEM.rd == instruction.rt:
            pipeline_rgs.ID_EX.rt_value = pipeline_rgs.EX_MEM.result
        elif pipeline_rgs.MEM_WB is not None and pipeline_rgs.MEM_WB.rd == instruction.rt:
            pipeline_rgs.ID_EX.rt_value = pipeline_rgs.MEM_WB.result
        else:
            pipeline_rgs.ID_EX.rt_value = rgs.get_Register__sort_value(instruction.rt)


class ExecutionResult:
    def __init__(self, result, rd):
        self.result = result
        self.rd = rd


class Register__sort:
    def __init__(self):
        self.Register__sorts = {}

    def get_Register__sort_value(self, reg):
        return self.Register__sorts.get(reg, 0)

    def set_Register__sort_value(self, reg, value):
        self.Register__sorts[reg] = value


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


def main():
    scanner = input

    k = int(scanner())

    if k == 1:
        data = mm_Sorting()
        Register_sorts = Register__sort()

        instructions = data.Get_ins()
        dec_sortd_array = [Decode__sort(inst[0:6], inst[6:11], inst[11:16], inst[16:21],
                                inst[21:26], inst[26:32], inst[16:32], inst[16:31]) for inst in instructions]

        print("n= ")
        n = int(scanner())
        Register_sorts.set_Register_sort_value("01009", n)

        print("Enter the intpt add: ")
        input_address = scanner()
        Register_sorts.set_Register_sort_value("01010", int(input_address, 2))

        print("Enter the outpt add: ")
        output_address = scanner()
        Register_sorts.set_Register_sort_value("01011", int(output_address, 2))

        data_mm_Sorting_address = Register_sorts.get_Register_sort_value("01010")
        las = data_mm_Sorting_address

        for i in range(n):
            print(f"Enter integer value {i + 1}: ")
            input_value = int(scanner())
            data.set_dt_val(data_mm_Sorting_address, input_value)
            data_mm_Sorting_address += 4

        data.run_pipeline(instructions, Register__sort)

    elif k == 2:
        # ... (unchanged)
        data = Memory()
        registers = Register__sort()

        instructions = data.get_fact_instructions()
        decoded_array = [Decode__sort(inst[0:6], inst[6:11], inst[11:16], inst[16:21],
                                inst[21:26], inst[26:32], inst[16:32], inst[16:31]) for inst in instructions]

        cycles = 0

        while registers.get_register_value("11111") < len(instructions) * 4:
            cycles += 1
            instruction = decoded_array[registers.get_register_value("11111") // 4]

            if instruction.opcode == "000100":
                Ex_Inst(instruction, data, registers)
            elif instruction.opcode == "000010":
                Ex_Inst(instruction, data, registers)
            else:
                Ex_Inst(instruction, data, registers)
                if instruction.opcode != "000100":
                    registers.set_register_value("11111", ((registers.get_register_value("11111") // 4) + 1) * 4)

        instructions = data.get_fact_instructions()
        decoded_array = [Decode__sort(inst[0:6], inst[6:11], inst[11:16], inst[16:21],
         inst[21:26], inst[26:32], inst[16:32], inst[16:31]) for inst in instructions]

        cycles = 0

        while registers.get_register_value("11111") < len(instructions) * 4:
            cycles += 1
            instruction = decoded_array[registers.get_register_value("11111") // 4]

            if instruction.opcode == "000100":
                Ex_Inst(instruction, data, registers)
            elif instruction.opcode == "000010":
                Ex_Inst(instruction, data, registers)
            else:
                Ex_Inst(instruction, data, registers)
                if instruction.opcode != "000100":
                    registers.set_register_value("11111", ((registers.get_register_value("11111") // 4) + 1) * 4)

        print("Output Memory:")
        print(registers.get_register_value("01100"))

        print("Number of cycles taken:", cycles)

if __name__ == "_main_":
    main()