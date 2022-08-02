import sys
filename = sys.argv[0]
f = open(filename, 'r')
char_in_file = len(f.read())
print(char_in_file)
for i in range(char_in_file - 1, -1, -1):
    f.seek(i)
    char = f.read(1)
    if char == '\t':
        print('\t')
    elif char == '\n':
        print('\n')
    else:
        print(char, end='')
f.close()

