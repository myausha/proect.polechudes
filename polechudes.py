while True: # главный цикл игры
    w = ['собака','кошка','корова','лошадь','овца','козел','панда','акула','заяц','водогрязеторфопарафинолечение','волк','енот','медведь','барсук','жираф','зебра','слон','стрекоза','пчела','бабочка','песец','сова','белка','паук']# w- список из которого выбираются слова 
    nomer_slova=int(input('Введи число от 1 до 25')) # переменная для выбора загаданного слова
    secret = w[nomer_slova - 1] # само загаданое слово            


    popitka = 0 # счетчик попыток
    user_letter = ' ' #переменная в которой будут хранится буквы короторые вводит игрок
    while True:
        missed = 0 
        letter = input('\nВведи букву или команду').lower() # переменная для ввода букв переводящая все что введет пользователь в нижний регистр 
        popitka += 1
        if len(letter)>1 and "/" not in letter : # проверка на то что игрок ввел не одну букву или все слово либо команду
            print('Ты ввел больше чем одну букву и меньше чем само слово')
        elif '/help' in letter: # команда с правилами
            print('правила игры:игрок вводит одну букву или все слово полностью,если буква введена не верно, игра напишет об ошибке ')
        elif '/funny' in letter: # команда с анекдотом 
            print('Второе сентября, начало первого урока, учительница говорит: - Дети, у вас есть еще вопросы? Вовочка: - А когда каникулы?')
        else:
            if letter in user_letter: # если буква введенная игроком уже была введена ранее
                print('такая буква уже есть')
            else:
                user_letter+=letter  
                for i in secret: # перебирает каждую букву в загаданном слове
                     if i in user_letter:  # проверка была ли эта буква уже введена
                        print(i,end=' ')
                     else: 
                        print('-',end =' ')
                        missed +=1
                if missed == 0: #проверка закончилась игра из за кол ва неправильных букв или нет
                   print('\n ты победил')
                   print('\n кол-во попыток:' ,popitka)  #подсчет попыток при выигрыше 
                   break     
         
