import psycopg

from settings import DB_CONFIG

with psycopg.connect(**DB_CONFIG) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
            select tracking_code, recipient, status from parcels
            order by id desc
        """)
        rows = cursor.fetchall()
        for row in rows:
            tracking_code, recipient, status = row
            print(f"{tracking_code}, {recipient}, {status}")