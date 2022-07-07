from pathlib import Path

files_dir = Path('files')
files = files_dir.iterdir()
merged = ''
for index, filepath in enumerate(files):
    with open(filepath, 'r') as file:
        content = file.readlines()
        new_conent = content[1:]
    if index == 0:
        content = ''.join(content)
        merged = merged + content + '\n'
    else:
        new_conent = ''.join(new_conent)
        merged = merged + new_conent + '\n'
    print(merged)
    print('--')
    # merged = merged + content
    with open('new.csv', 'w') as file:
        file.write(merged)
