w = ['собака','кошка']
nomer_slova=int(input('веди число от 1 до 25'))
secret = w[nomer_slova - 1]                      


popitka = 0
user_letter = ' '
while True:
    missed = 0
    letter = input('\nВведи букву').lower()
    popitka += 1
    if len(letter)>1:
        print('Ты ввел больше чем одну букву и меньше чем само слово')
    else:
        if letter in user_letter:
            print('такая буква уже есть')
        else:
            user_letter+=letter  
            for i in secret:
                 if i in user_letter:
                    print(i,end=' ')
                 else:
                    print('-',end =' ')
                    missed +=1
                    
    if missed == 0:
        print('\n ты победил')
        print('\n кол-во попыток:' ,popitka)
          
