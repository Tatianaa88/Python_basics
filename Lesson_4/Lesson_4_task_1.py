from sys import argv
param = argv[1:]

if 'h' in param:
    print('h - help\n1st parameter - amount of hours\n2nd parameter - pay per hour\n3rd parameter - bonus')
else:
    income = int(param[0]) * int(param[1]) + int(param[2])
    print(income)
