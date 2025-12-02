#from time import sleep
from collections import deque
from core.process import Process
import inspect
from bin.ls import ls
from bin.echo import Echo
from bin.cat import cat    
from bin.cd import cd

class Kernel:
    def __init__(self):
        self.process_queue = deque()
        self._pid_counter = 0               # "pid" stands for "Process ID".

        try:
            from core.filesystem import FileSystem
            fs_kernal = FileSystem()
            self.disk_data = fs_kernal.load_disk()
            print("[KERNAL] Disk loaded and is ready for use.")

        except ImportError as e:
            print (f"[KERNAL] Faild to load Disk. Error: {e}")
            quit(f'{e}')

    def create_process(self, name, func, *args):
        """
        Loads a function as a process.
        The function HAS TO BE a generator.
        """
        gen_check = func(*args)
        if not inspect.isgenerator(gen_check):
            raise TypeError("The OS requires programs to be generators!")

        self._pid_counter += 1
        process = Process(
            pid=self._pid_counter,
            name=name,
            code_generator=gen_check
        )
        self.process_queue.append(process)
        print(f"[KERNAL] Process {process._pid} ({name}) created.")

    def run(self):
        print("[KERNAL] Booting up...")

        while self.process_queue:
            current_process = self.process_queue.popleft()
            current_process.state = "RUNNING"

            try:
                io_request = next(current_process._gen)

                # 1. Print only if there is text
                if io_request:
                    print(f"[SYSCALL] {current_process._name}: {io_request}")
                
                # 2. ALWAYS put the process back (unless it crashed or finished)
                current_process.state = "READY"
                self.process_queue.append(current_process)

            except StopIteration:
                current_process.state = "TERMINATED"
                print(f"[KERNAL] Process {current_process._pid} ({current_process._name}) finished.")

            except Exception as e:
                print(f"[KERNEL] CRASH: Process {current_process._pid} died. Error: {e}")


def process(disk_data, kernel_instance):

    commands_list = [
        "cat",
        "echo",
        "ls",
        "exit",
        "ps",
        "cd",
        ""
    ]

    current_path: list = []
    
    while True:
        
        path_str = "/" + "/".join(current_path)
        user_input = input(f"user@LightsOS: {path_str}/$> ")

        if user_input == "exit":
            break

        seperated_input = user_input.split(" ")
        command = seperated_input[0]
        
        path = ""        # ls command
        echo_output = []    # echo command
        
        if len(seperated_input) > 1:
            path = seperated_input[1]        # Common path for all commands except `echo`
            echo_output = seperated_input[1:]       # echo command
        
        else:
            path = ""

        try:
            if command not in commands_list:      # Command validity check
                yield f"Command: '{command}' not found."

            
            elif command == "cd":           # cd command
                
                yield from cd(path, current_path, disk_data)

            
            elif command == "ls":
                if path:
                    if path.startswith("/"):
                        replaced_ls_path = path.replace("/", "")
                        check_path = "/".join(current_path + [replaced_ls_path])
                    else:
                        check_path = "/".join(current_path + [path])
                else:
                    check_path = "/".join(current_path)

                yield from ls(check_path, disk_data)


            elif command == "echo":     # echo command
                if " | " in user_input:
                    piped_text = user_input.split("|")
                    clean_piped_file_name = piped_text[1].strip()
                    to_be_written_text = piped_text[0].replace("echo", "", 1).strip()
                    yield from Echo().pipe(to_be_written_text, clean_piped_file_name)
                else:
                    yield from Echo().echo(*echo_output)


            elif command == "ps":       # shows active processes
                active_processes = kernel_instance._pid_counter
                yield f"Total Active processes: {active_processes}"

            
            elif command == "cat":          # cat command
                if path:
                    check_path = path
                else:
                    check_path = "/".join(current_path)  
                yield from cat(check_path, current_path, disk_data)

        except Exception as e:
            yield f"Shell error hellooooo: {e}"

    yield None              # Gives the "Kernel" control again. 


if __name__ == "__main__":
    os_kernel = Kernel()
    os_kernel.create_process("Shell", process, os_kernel.disk_data, os_kernel)
    os_kernel.run()
