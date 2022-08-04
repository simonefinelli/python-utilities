"""
    Read a file line by line.
"""

filename = "file1.txt"

# open the file and read it line by line
# the content stored like a list
with open(filename) as f:
    content = f.read().splitlines()

# show the content
for line in content:
    print(line)