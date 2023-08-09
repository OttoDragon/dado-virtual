import random

response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')


if response == "y":
    while response == "y":
        no = random.randint(1, 6)
        if no == 1:
            print('[-----]')
            print('[     ]')
            print('[  0  ]')
            print('[     ]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

        if no == 2:
            print('[-----]')
            print('[    0]')
            print('[     ]')
            print('[0    ]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

        if no == 3:
            print('[-----]')
            print('[    0]')
            print('[  0  ]')
            print('[0    ]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

        if no == 4:
            print('[-----]')
            print('[0   0]')
            print('[     ]')
            print('[0   0]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

        if no == 5:
            print('[-----]')
            print('[0   0]')
            print('[  0  ]')
            print('[0   0]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

        if no == 6:
            print('[-----]')
            print('[0   0]')
            print('[0   0]')
            print('[0   0]')
            print('[-----]')
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')
        if response == 'n':
            print("você não jogou o dado")
            response = input('jogar um dado? Digite "y" para jogar, digite "n" para não jogar: ')

























































