import os
import shutil

cwd = os.getcwd()

os.makedirs("project_archive", exist_ok=True)
main_folder = 'project_archive'

files = ['jan.csv', 'feb.json', 'mar.txt', 'april.xml', 'may.xlsx', 'june.txt', 'july.json','aug.xml', 'sep.json']
for file in files:
    file_path = os.path.join(main_folder, file)
    with open(file_path, 'w') as wr:
        wr.write('hello world')

file_count = {".csv": 0,".json": 0,".txt": 0,".xml": 0,".xlsx": 0}
for file in os.listdir(main_folder):
    split_text = os.path.splitext(file)[1]
    if split_text in file_count:
        file_count[split_text] += 1

for split_text, count in file_count.items():
    print(f"  {split_text}: {count} file(s)")

os.makedirs('data_files', exist_ok=True)
os.makedirs('text_files', exist_ok=True)
text_folder = "text_files"
data_folder = "data_files"

for fil in os.listdir(main_folder):
    if fil.endswith('csv') or fil.endswith('json') or fil.endswith('xlsx'):
        shutil.move(os.path.join(main_folder, fil), data_folder)
    else:
        shutil.move(os.path.join(main_folder, fil), text_folder)


print(os.listdir(text_folder))
print(os.listdir(data_folder))

if len(os.listdir(text_folder)) > len(os.listdir(data_folder)):
    print('The folder with the most file is text_files')
if len(os.listdir(text_folder)) == len(os.listdir(data_folder)):
    print('Both text_files and data_files contain same amount of file')
else:
    print('The folder with the most file is data_files')