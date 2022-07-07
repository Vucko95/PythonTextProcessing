from pathlib import Path

# with open('file3.csv', 'r') as file:
#     content = file.read()

# print(content[:-1])
# modified_content = content[:-1]

# with open('newfile3.csv', 'w') as file:
#     file.write(modified_content)

# Will Remove 1 word in file each time
files_dir = Path('files')
for filepath in files_dir.iterdir():
    # print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
        modified_content = content[:-1]
    with open(filepath, 'w') as file:
        file.write(modified_content)
