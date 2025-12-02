# LightsOS 💡

**LightsOS** is a conceptual Operating System simulator written in pure Python. 

It replicates the core architecture of a real OS, featuring a micro-kernel, a round-robin process scheduler, and a virtual JSON-based file system. It demonstrates how processes, system calls, and I/O management work under the hood.

## 🚀 Features

*   **Kernel Architecture:** Implements a generator-based process scheduler.
*   **Virtual Filesystem:** Uses `data/disk.json` to simulate a persistent disk drive.
*   **Shell Interface:** A working CLI with command parsing and state management.
*   **I/O Redirection:** Supports the pipe operator (`|`) to send output from one command to a file.
*   **Implemented Commands:**
    *   `ls`: List directory contents (supports absolute & relative paths).
    *   `cd`: Change directory with state tracking.
    *   `cat`: Read file contents.
    *   `echo`: Print text (or write to file via pipe).
    *   `ps`: View active kernel process stats.

## 🛠️ Installation & Usage

1.  **Create a python virtual enviroment:**
    ```bash
    python venv .venv
    ```

2.  **Activate it (windows):**
    ```bash
    ./.venv/Scripts/Activate
    ```

3.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/LightsOS.git
    cd LightsOS
    ```

4.  **Run the OS:**
    LightsOS requires no external libraries. Run it directly using Python's module flag:
    ```bash
    python -m core.kernel
    ```

## 📂 Architecture

The project is structured to mimic real OS components:

```text
LightsOS/
├── core/
│   ├── kernel.py       # The CPU Scheduler & Main Loop
│   ├── process.py      # Process Object Definition
│   ├── memory.py       # Memory for OS
│   └── filesystem.py   # Interface for the Virtual Disk (JSON)
├── bin/
│   ├── ls.py           # Directory Listing Logic
│   ├── cd.py           # Directory Navigation Logic
│   ├── echo.py         # Text Output & Piping Logic
│   └── cat.py          # File Reading Logic
├── data/
│   └── disk.json       # The "Hard Drive" storage
├── boot.py
└── README.md
```

## 🧠 How it Works
```text
    Boot: The Kernel initializes and loads disk.json into memory.

    Scheduling: The Kernel runs an infinite loop. It picks a process from the process_queue, runs it until it yields (StopIteration or IO Request), and then places it back in the queue.

    The Shell: The Shell is just a process! It runs in an infinite loop yielding control back to the Kernel after every command.
```

## 📝 Future Roadmap
```text
1. Implement mkdir and touch commands.

2. Add a user permission system (Root vs Guest).

3. Implement a shutdown command to save the JSON state back to the disk file.
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
code Code

    
---

### Step 3: The License (`LICENSE`)
GitHub projects usually need a license so people know if they can use your code. The **MIT License** is the standard "do whatever you want with this" license.

**File:** `LICENSE` (no extension)
**Location:** Main folder.
**Content:** (Copy/Paste this, but put **Your Name** and the **Year**).

```text
MIT License

Copyright (c) 2025 [YOUR NAME HERE]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```