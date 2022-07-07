from pathlib import Path

# with open('file3.csv', 'r') as file:
#     content = file.read()

# print(content[:-1])
# modified_content = content[:-1]

# with open('newfile3.csv', 'w') as file:
#     file.write(modified_content)

# Will Remove 1 word in file each time
files_dir = Path('files')
files = files_dir.iterdir()
merged = ''
for filepath in files:
    # print(filepath)
    with open(filepath, 'r') as file:
        content = file.read()
    merged = merged + content
with open('new.csv', 'w') as file:
    file.write(merged)
