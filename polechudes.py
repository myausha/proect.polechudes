while True:
    w = ['собака','кошка']
    nomer_slova=int(input('Введи число от 1 до 25'))
    secret = w[nomer_slova - 1]                      


    popitka = 0
    user_letter = ' '
    while True:
        missed = 0
        letter = input('\nВведи букву или команду').lower()
        popitka += 1
        if len(letter)>1 and "/" not in letter :
            print('Ты ввел больше чем одну букву и меньше чем само слово')
        elif '/help' in letter:
            print('правиолаа')
        elif '/funny' in letter:
            print('Второе сентября, начало первого урока, учительница говорит: - Дети, у вас есть еще вопросы? Вовочка: - А когда каникулы?')
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
                   break
                     
         
