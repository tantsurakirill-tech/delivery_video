from models import Parcel
from settings import Session


with Session() as session:
    parcel = session.get(Parcel, 9)
    if parcel is not None:
        parcel.delete()
        session.commit()

    else:
        print("Посылка не найдена")