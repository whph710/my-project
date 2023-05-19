# MyProfile app

SEPARATOR = '-' * 42

# user profile
name = ''
age = 0
phone_number = ''
email = ''
info = ''  # Индекс
address = ''  # Адрес
add_info = ''  # Доп.инфо

# bank details
og = ''  # ОГРНИП
inn = ''  # ИНН
rs = ''  # Р/С
bank = ''  # Банк
bic = ''  # БИК
ks = ''  # Кор.счёт


def separator():
    print(SEPARATOR)


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, ii_parameter, di_parameter):
    separator()
    print('Имя:    ', n_parameter)
    if (
            11 <= a_parameter % 100 <= 19
            or a_parameter % 10 != 1
            and not 2 <= a_parameter % 10 <= 4
    ):
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    else:
        years_parameter = 'года'
    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', i_parameter)
    print('Адрес:  ', ii_parameter)
    if add_info:
        print('\nДополнительная информация:')
        print(di_parameter)
        print()


def full_info_user():
    general_info_user(name, age, phone_number, email, info, address, add_info)
    print('Информация о предпринимателе')
    print('ОГРНИП:  ', og)
    print('ИНН:     ', inn)
    print('Банковские реквизиты')
    print('Р/С:     ', rs)
    print('Банк:    ', bank)
    print('БИК:     ', bic)
    print('Кор.счёт:', ks)


def input_user_info():
    global name, age, phone_number, email, info, address, add_info
    name = input('Введите имя: ')
    while age < 18:
        age = int(input('Введите возраст: '))
    while True:
        phone_number = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
        if not phone_number.isdigit():
            print("Номер телефона должен содержать только цифры")
        else:
            break
    email = input('Введите email: ')
    info = input('Введите индекс: ')
    address = input('Введите адрес: ')
    add_info = input('Введите дополнительную информацию: ')


def input2_user_info():
    global og, inn, rs, bank, bic, ks
    while len(og) < 15:
        og = input('Введите ОГРНИП: ')
        if len(og) < 20:
            print("ОГРНИП должен содержать не менее 15 цифр")
    inn = input('Введите ИНН: ')
    while len(rs) < 20:
        rs = input('Введите Р/С: ')
        if len(rs) < 20:
            print("Р/С должен содержать не менее 20 цифр")
    bank = input('Введите Банк: ')
    bic = input('Введите БИК: ')
    ks = input('Введите Кор.счёт: ')


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    separator()
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')
    choice = int(input('Введите номер пункта меню: '))
    if choice == 0:
        break
    elif choice == 1:
        while True:
            separator()
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация об предпринимателе')
            print('0 - Назад')

            choice2 = int(input('Введите номер пункта меню: '))
            if choice2 == 0:
                break
            elif choice2 == 1:
                input_user_info()
            elif choice2 == 2:
                input2_user_info()
            else:
                print('Введите корректный номер пункта меню')
    elif choice == 2:
        while True:
            separator()
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            choice2 = int(input('Введите номер пункта меню: '))
            if choice2 == 0:
                break
            elif choice2 == 1:
                general_info_user(name, age, phone_number, email, info, address, add_info)
            elif choice2 == 2:
                full_info_user()
            else:
                print('Введите корректный номер пункта меню')
    else:
        print('Введите корректный номер пункта меню')
