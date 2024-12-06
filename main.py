import random
from MenuOptions import MenuOptions
from CreateOptions import CreateOptions
from utils import isInDict
from getters import (
    getState,
    getPid,
    getProgramCounter,
    getRegisters,
    getMemoryLimits,
    getOpenFilesList,
)
from PCB import PCB
from State import State
from UniqueInteger import UniqueInteger


def createProcess(
    processes_lst: list,
    pid_to_index_dict: dict,
    pid_gen: UniqueInteger,
    address_gen: UniqueInteger,
    file_number_gen: UniqueInteger,
) -> None:
    while True:
        for create_option in CreateOptions:
            print(f"{create_option.value}. {create_option.name}")
        option = input("Select option: ")

        try:
            option_obj = CreateOptions(int(option))
        except ValueError:
            print(f"{option_obj} is not a valid option! Please select from the list.")
            continue

        if option_obj == CreateOptions.AUTO:
            createProcessAuto(
                processes_lst, pid_to_index_dict, pid_gen, address_gen, file_number_gen
            )
        elif option_obj == CreateOptions.MANUAL:
            createProcessManual(processes_lst, pid_to_index_dict)

        break


def createProcessAuto(
    processes_lst: list,
    pid_to_index_dict: dict,
    pid_gen: UniqueInteger,
    address_gen: UniqueInteger,
    file_number_gen: UniqueInteger,
) -> None:
    state = State(random.randint(1, len(State))).name
    pid = next(pid_gen)
    program_counter = random.randint(1, 1000)
    registers = [random.choice([True, False]) for _ in range(0, random.randint(1, 7))]
    memory_limits = (next(address_gen), next(address_gen))
    open_files_list = [
        f"./file_{next(file_number_gen)}.{random.choice(("txt", "py", "docx", "csv"))}"
        for _ in range(0, random.randint(1, 7))
    ]

    processes_lst.append(
        PCB(state, pid, program_counter, registers, memory_limits, open_files_list)
    )
    pid_to_index_dict[pid] = len(processes_list) - 1


def createProcessManual(processes_lst: list, pid_to_index_dict: dict) -> None:
    state = getState()
    pid = getPid()
    program_counter = getProgramCounter()
    registers = getRegisters()
    memory_limits = getMemoryLimits()
    open_files_list = getOpenFilesList()

    processes_lst.append(
        PCB(state, pid, program_counter, registers, memory_limits, open_files_list)
    )
    pid_to_index_dict[pid] = len(processes_list) - 1


def searchProcess(
    processes_lst: list,
    pid_to_index_dict: dict,
) -> None:
    search_pid = getPid()
    if isInDict(search_pid, pid_to_index_dict):
        print(processes_lst[pid_to_index_dict[search_pid]])


def deleteProcess(
    processes_lst: list,
    pid_to_index_dict: dict,
) -> None:
    delete_pid = getPid()
    if isInDict(delete_pid, pid_to_index_dict):
        delete_index = pid_to_index_dict.pop(delete_pid)
        processes_lst.pop(delete_index)


def printAllProcesses(processes_lst: list) -> None:
    for index, process in enumerate(processes_lst):
        print(index)
        print(process)


def exitProgram() -> None:
    command = input("exit? (y/n)")
    while True:
        if command == "y":
            exit(0)
        elif command == "n":
            return
        else:
            command = input("exit? (y/n)")


processes_list: list[str] = []
pid_to_index_dictionary: dict[int, int] = {}
pid_generator = UniqueInteger(4)
address_generator = UniqueInteger(16)
file_number_generator = UniqueInteger(6)

while True:
    for menu_option in MenuOptions:
        print(f"{menu_option.value}. {menu_option.name}")
    option = input("Select option: ")

    try:
        option_obj = MenuOptions(int(option))
    except ValueError:
        print(f"{option_obj} is not a valid option! Please select from the list.")
        continue

    if option_obj == MenuOptions.CREATE_PROCESS:
        createProcess(
            processes_list,
            pid_to_index_dictionary,
            pid_generator,
            address_generator,
            file_number_generator,
        )
    elif option_obj == MenuOptions.SEARCH_PROCESS:
        searchProcess(
            processes_list,
            pid_to_index_dictionary,
        )
    elif option_obj == MenuOptions.DELETE_PROCESS:
        deleteProcess(
            processes_list,
            pid_to_index_dictionary,
        )
    elif option_obj == MenuOptions.PRINT_ALL_PROCESSES:
        printAllProcesses(processes_list)
    elif option_obj == MenuOptions.EXIT_PROGRAM:
        exitProgram()

    input("Press enter to continue")
