attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    password = input('Enter your password: ')
    if password == '98eaxc':
        print('Access granted')
        break
else:
    print('Access denied')

