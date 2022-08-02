a = open('fizzbuzz.txt')
for line in a:
    print('\n')
    string = line.split()
    fizz, buzz, numb = int(string[0]), int(string[1]), int(string[2])
    for i in range(1, numb + 1):
        if i % fizz == 0 and i % buzz == 0:
            print("FB ", end='')
        elif i % fizz == 0:
            print("F ", end='')
        elif i % buzz == 0:
            print("B ", end='')
        else:
            print(str(i) + ' ', end='')
a.close()