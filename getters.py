from State import State
from utils import isDigit


def getState() -> str:
    for state_option in State:
        print(f"{state_option.value}. {state_option.name}")
    state = input("Select state: ")
    while True:
        try:
            return State(int(state)).name
        except ValueError:
            print(f"Error: {state} is not a valid state! Please select from the list.")
            state = input("Select state: ")


def getPid() -> int:
    pid = input("Enter PID (int): ")
    while True:
        if isDigit(pid, "PID"):
            return int(pid)
        else:
            pid = input("Enter PID (int): ")


def getProgramCounter() -> int:
    program_counter = input("Enter program counter (int): ")
    while True:
        if isDigit(program_counter, "Program counter"):
            return int(program_counter)
        else:
            program_counter = input("Enter program counter (int): ")


def getRegisters() -> list:
    registers = input("Enter registers (bool, bool, ...): ")
    while True:
        registers_list = registers.split(", ")
        for register in registers_list:
            register = register.strip()
            if register not in ["True", "False"]:
                print(f"Error: {register} is not a valid register.")
                print("Input example: 'True, False, False'")
                break
        else:
            return [
                True if register.strip() == "True" else False
                for register in registers_list
            ]
        registers = input("Enter registers (bool, bool, ...): ")


def getMemoryLimits() -> tuple:
    memory_limits = input("Enter memory limits (int, int): ")
    while True:
        memory_limits_list = memory_limits.split(", ")
        if (
            len(memory_limits_list) != 2
            or not memory_limits_list[0].isnumeric()
            or not memory_limits_list[0].isnumeric()
        ):
            print("Error: Memory limits has to have exactly two integers!")
        else:
            return int(memory_limits_list[0]), int(memory_limits_list[1])
        memory_limits = input("Enter memory limits (int, int): ")


def getOpenFilesList() -> list:
    open_files_list = input("Enter files (str, str, ...): ")
    return open_files_list.split(", ")
