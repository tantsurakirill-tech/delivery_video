from sqlalchemy import text, select
from sqlalchemy.sql.operators import and_

from models import Parcel
from settings import engine, Session

# with engine.connect() as connection:
#     result = connection.execute(text("select 1+5, current_user, current_database()"))
#     print(result.one())

with Session() as session:
    result = session.get(Parcel, 1)
    print(result)

    stmt = select(Parcel).where(Parcel.tracking_code=='PK-1002')
    parcel= session.scalars(stmt).one()
    print(parcel)


    stmt = select(Parcel).where(and_(Parcel.status=="created", Parcel.recipient=="Анна")).order_by(Parcel.recipient)
    parcels = session.scalars(stmt).all()
    print(parcels)
