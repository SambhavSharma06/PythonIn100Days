#Import OS in Python!!

import os
#def welcome():
#The os module in Python is used to interact
#with
#the operating system. It lets your Python
#programs work with files, directories,
#environment variables, and system-level
#operations in a cross-platform way
#(Windows, macOS, Linux).
#What the os module is used for
#1. Working with files & directories
#import os
#os.getcwd()          # Get current working directory
#os.chdir("path")     # Change directory
#os.listdir(".")      # List files and folders
#os.mkdir("test")     # Create a directory
#os.makedirs("a/b")   # Create nested directories
#os.remove("file.txt")# Delete a file
#os.rmdir("test")     # Remove empty directory
#2. Path operations (commonly used)
#Although still available,
#os.path is often replaced by pathlib,
#but you’ll see it a lot.
#os.path.exists("file.txt")
#os.path.isfile("file.txt")
#os.path.isdir("folder")
#os.path.join("folder", "file.txt")
#os.path.abspath("file.txt")
#os.path.basename("/a/b/c.txt")
#3. Environment variables
#os.environ["PATH"]# Read an environment variable
#os.environ["MY_VAR"] = "123"# Set environment variable
#os.getenv("HOME")# Safer way to read
#4. Running system commands
#os.system("ls") # macOS / Linux
#os.system("dir") # Windows
#os.system() is simple but limited.
#For real applications, use subprocess instead.
#5. Process & OS information
#os.name          # 'nt' (Windows),
#'posix' (Linux/macOS)
#os.getpid()      # Current process ID
#os.cpu_count()   # Number of CPUs
#6. File permissions (Unix-like systems)
#os.chmod("file.txt", 0o644)
#Common beginner example
#Create a folder only if it doesn’t exist:
#import os
#if not os.path.exists("data"):
#os.mkdir("data")
#os vs pathlib (important)
#os → older, very common, procedural style
#pathlib → modern, object-oriented, cleaner
#Example with pathlib:
#from pathlib import Path
#p = Path("data")
#p.mkdir(exist_ok=True)
#In new projects, prefer pathlib,
#but you must still understand os
#because it’s everywhere.
#When to use os
#✔ File/directory handling
#✔ Environment variables
#✔ Checking OS type
#✔ Simple system commands
