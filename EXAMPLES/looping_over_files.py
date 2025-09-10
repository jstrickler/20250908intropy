import sys

# sys.argv is ALL cmd line arguments including script name

for file_path in sys.argv[1:]:  # skip script name
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        pass   #  read each file here

#  python foo.py a.txt b.txt c.txt