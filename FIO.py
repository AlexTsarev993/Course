surname = input("Введите фамилию: ")
name = input("Введите имя: ")
patronymic = input("Введите отчество: ")

surname = surname.capitalize()
name = name.capitalize()
patronymic = patronymic.capitalize()

print("{} {}.{}.".format(surname, name[0], patronymic[0]))
