numb = int(input('Enter sum pls:'))
L = '1000 500 200 100 50 20 10 5 2 1'.split()
for i in range(0, 10):
    count = 0
    while numb >= int(L[i]):
        numb -= int(L[i])
        count += 1
    print(L[i], ' = ', count)



