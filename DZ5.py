def Fizz_Buzz(fizz, buzz, numb):
    result = ()
    for i in range(1, numb + 1):
        if not i % fizz and not i % buzz:
            result += ("FB",)
        if not i % fizz:
            result += ("F",)
        elif not i % buzz:
            result += ("B",)
        else:
            i = str(i)
            result += (i,)
    return(result)


file_name = open('fizzbuzz.txt')
result_file = open("result.txt", 'w')
for line in file_name:
    string = line.split()
    fizz, buzz, numb = int(string[0]), int(string[1]), int(string[2])
    result_file.write(str(Fizz_Buzz(fizz, buzz, numb)) + "\n")


