#Virtual Environment in Python!!

#1-Minute Explanation: Python Virtual Environment
#A Python virtual environment is a **separate, isolated workspace for a project.
#When you create it using:
#bash
#python -m venv venv
#python makes a private copy of the interpreter and a package folder.
#When you activate it:
#bash
#source venv/bin/activate #macOS/Linux
#venv\Scripts\activate #Windows
#your system’s `PATH` changes so that:
#`python` points to the venv’s Python
#`pip` installs packages **only inside the venv
#This prevents conflicts between projects that need **different library versions**.
#You install packages normally:
#bash
#pip install requests
#and they stay isolated.
#To exit:
#bash
#deactivate
#In short:
#Virtual environments keep each Python project’s dependencies separate, clean, and conflict-free.
