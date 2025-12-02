#!/usr/bin/env python3
import os
import sys
import runpy

def main():
    """
    Main entry point for the LightsOS launcher.
    This script ensures the Python path is correct and executes the kernel.
    """
    project_root = os.path.dirname(os.path.abspath(__file__))

    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    if sys.version_info < (3, 6):
        print(" Error: LightsOS requires Python 3.6 or higher.")
        sys.exit(1)

    print(f"[*] Launcher initializing... Root: {project_root}")
    
    try:
        runpy.run_module("core.kernal", run_name="__main__", alter_sys=True)
        
    except KeyboardInterrupt:
        print("\n\n[!] Force shutdown initiated by user. Goodbye!")
        sys.exit(0)
        
    except ImportError as e:
        print(f"\n Critical Error: Could not import system modules.\nDetails: {e}")
        print("Make sure you are running this from the main LightsOS directory.")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n Unknown Error during runtime: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()