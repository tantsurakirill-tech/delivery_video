from models import Parcel

from settings import Session


tracking_code = input("Выберите посылку для внесения изменений: ")
field = int(input("Выберите поле для изменения(Имя - 1, Вес - 2): "))
value = input("Введите новое значение: ")


with Session() as session:

    parcel = session.get(Parcel, tracking_code)
    if parcel is not None:
        parcel.FIELDS[field] = value
        session.commit()

    else:
        print("Посылка не найдена")

"""
Доделать программу: пользователь выбирает посылку(программа предлагает) 
Программа предлагает какое поле поменять (1, 2, 3) и затем программа предлагает 
ввести новое значение для этого поля
и потом успешно меняет 
"""
