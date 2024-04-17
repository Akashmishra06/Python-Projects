print("Hello Everyone, This is me....")

def college(section):
    return section

yourSection = college("IT'A")
print(f"yourSectionIs: {yourSection}")



# Python script to demonstrate the steps involved in the conversion of Python source code into executable code

# Step 1: Writing Python Code
# Python source code written in a code editor
def greet(name):
    print("Hello, " + name + "!")

# Step 2: Saving as .py File
# Python code saved as greet.py
# Step 3: Compilation to Bytecode
# The Python compiler converts the source code into bytecode and generates greet.pyc
# No explicit action required in the script for this step

# Step 4: Interpretation by Python Virtual Machine (PVM)
# Python interpreter reads and executes the bytecode
# No explicit action required in the script for this step

# Step 5: Conversion to Machine Code
# The Python Virtual Machine further processes the bytecode to generate machine-executable code
# No explicit action required in the script for this step

# Step 6: Execution by CPU
# The CPU executes the machine code produced by the Python Virtual Machine
# The final output is displayed based on the executed instructions

# Example of calling the greet function
greet("John")


import os

print(os.getcwd())