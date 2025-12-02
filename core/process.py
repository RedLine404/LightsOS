class Process:
    def __init__(self, pid, name, code_generator): # "pid" stands for "Process ID".
        self._pid = pid
        self._name = name
        self._gen = code_generator
        self.state = "READY"                       # READY, RUNNING, TERMINATED
