# DevOps-Training-practice_file1.3

1. Creates a folder named project_archive
This folder holds a mix of file types, simulating a real-world archive.

2. Generates sample files
The script creates the following files with placeholder content:
jan.csv, feb.json, mar.txt, april.xml, may.xlsx, june.txt, july.json, aug.xml, sep.json

3. Counts file types
The script counts how many files of each type exist:
.csv, .json, .txt, .xml, .xlsx

4. Creates organized folders
Two folders are created in the root directory:
data_files/ for .csv, .json, .xlsx
text_files/ for .txt, .xml

5. Moves files into categorized folders
.csv, .json, .xlsx → data_files/
.txt, .xml → text_files/

6. Prints final folder contents

7. Lists the contents of both data_files/ and text_files/

8. Compares folder sizes
Outputs which folder contains the most files.

SAMPLE OUTPUT
  .csv: 1 file(s)
  .json: 3 file(s)
  .txt: 2 file(s)
  .xml: 2 file(s)
  .xlsx: 1 file(s)
['mar.txt', 'april.xml', 'june.txt', 'aug.xml']
['jan.csv', 'feb.json', 'may.xlsx', 'july.json', 'sep.json']
The folder with the most file is data_files
