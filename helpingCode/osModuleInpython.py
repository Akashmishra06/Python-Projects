import os

# Specify the folder path
folder_path = '/workspaces/Python-With-Projects/conditionalsInPython/questions'

# Create the directory if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create 10 files named problem_1.py to problem_10.py
for i in range(1, 11):
    file_name = os.path.join(folder_path, f'problem_{i}.py')
    with open(file_name, 'w') as file:
        file.write(f"# Question_{i}")

# List all files in the directory
print("Files in the directory:")
files = os.listdir(folder_path)
for file in files:
    print(file)

# Rename the files from problem_1.py to problem_10.py to question_1.py to question_10.py
for i in range(1, 11):
    old_name = os.path.join(folder_path, f'problem_{i}.py')
    new_name = os.path.join(folder_path, f'question_{i}.py')
    os.rename(old_name, new_name)

# List all files in the directory after renaming
print("\nFiles in the directory after renaming:")
files = os.listdir(folder_path)
for file in files:
    print(file)

# Remove the files question_1.py to question_10.py
for i in range(1, 11):
    file_name = os.path.join(folder_path, f'question_{i}.py')
    os.remove(file_name)

# List all files in the directory after removing
print("\nFiles in the directory after removing:")
files = os.listdir(folder_path)
if not files:
    print("Directory is empty.")
else:
    for file in files:
        print(file)

# Remove the directory
os.rmdir(folder_path)
print("\nDirectory removed.")