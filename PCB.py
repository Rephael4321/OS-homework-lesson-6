from State import State


class PCB:

    def __init__(
        self,
        state: str,
        pid: int,
        program_counter: int,
        registers: list[bool],
        memory_limits: tuple[int, int],
        open_files_list: list[str],
    ) -> None:
        self._state = state
        self._pid = pid
        self._program_counter = program_counter
        self._registers = registers
        self._memory_limits = memory_limits
        self._open_files_lst = open_files_list

    def __str__(self):
        string = f"""STATE:           {self._state}
PID:             {self._pid}
PROGRAM COUNTER: {self._program_counter}
REGISTERS:       {self._registers}
MEMORY LIMITS:   {self._memory_limits}
OPEN FILES LIST: {self._open_files_lst}
"""
        return str(string)
