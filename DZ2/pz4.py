#Ввести число, вывести его

numb = str(input('Input number pls: '))
for i in range(1, len(numb) + 1):
    print(i, 'digits is: ', numb[-i])
numb = int(numb)
for j in range(numb, 0, -1):
    if not numb % j:
        print('factor: ', int(numb / j))




