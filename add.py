from models import Parcel
from settings import Session

tracking_code = input("Введите код отслеживания: ")
recipient = input("Имя: ")
weight_kg = int(input("Вес: "))

with Session() as session:
    parcel = Parcel(tracking_code=tracking_code, recipient=recipient, weight_kg=weight_kg)
    session.add(parcel)
    session.commit()