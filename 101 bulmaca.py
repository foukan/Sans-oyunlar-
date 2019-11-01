import random
for i in range (1):
    d = random.randint(1,250)
    print('1. Deneme...')
    print(d)
    if d == 101:
        print('Tebrikler Kazandınız!')
        break
    elif d != 101:
        print ('2 Hakkın kaldı...')
        d = random.randint(95,300)
        print('2. Deneme...')
        print(d)
        if d == 101:
            print('Tebrikler Kazandınız!')
            break
        elif d != 101:
            print('1 Hakkın kaldı...')
            d = random.randint(65,2235)
            print('3. Deneme')
            print(d)
            if d == 101:
                print('Tebrikler Kazandınız!')
                break
            elif d != 101:
                print('Game Over')
                break
