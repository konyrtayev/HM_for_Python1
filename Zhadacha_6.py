ticket_number = [int(i) for i in input("Введите номер билета: ")] # номер билета должно быть шестизначным числом
if len(ticket_number) == 6:
    print(["Увы, повезет в следующий раз.","У вас счатливый билет!!!"][sum(ticket_number[:3]) == sum(ticket_number[3:])])
else:
    print("Вы ввели не правильные данные.")