a = open('fizzbuzz.txt')
b = open('result.txt', 'w')
for line in a:
    b.write('\n')
    string = line.split()
    fizz, buzz, numb = int(string[0]), int(string[1]), int(string[2])
    for i in range(1, numb + 1):
        if i % fizz == 0 and i % buzz == 0:
            b.write("FB ")
        elif i % fizz == 0:
            b.write("F ")
        elif i % buzz == 0:
            b.write("B ")
        else:
            b.write(str(i) + ' ')
a.close()