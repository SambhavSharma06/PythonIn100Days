# Creating a command-line utility in Python!!
import argparse

parser = argparse.ArgumentParser(description="Example CLI tool")

parser.add_argument("--name", help="Your name")
parser.add_argument("--age", type=int, help="Your age")

args = parser.parse_args()

print(f"Hello {args.name}, you are {args.age} years old.")
