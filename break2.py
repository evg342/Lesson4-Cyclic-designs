name = None
while True:
    print('Menu: ')
    print('1. Enter name')
    print('2. Print greeting')
    print('3. Quit')

    response = input('Please choose an action: ')

    print()
    if response == '1':
        name = input('Enter your name: ')
    elif response == '2':
        if name:
            print('Helo', name, '!', sep="")
        else:
            print('I dont no your name')
    elif response == '3':
        break
    else:
        print('Incorrect input.')

print()



