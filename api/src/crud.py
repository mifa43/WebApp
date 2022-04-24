# from enum import unique
# from click import echo
# import psycopg2 
# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# # # class Postgres():
# # # # Connect to your postgres DB
# # #     def __init__(self) -> None:
# # #         pass
# #         # self.conn = pg2.connect("dbname=userservice user=mifa53 password=koliko43")

# #     # Open a cursor to perform database operations
# #     # def getUser():
# #     #     lis_of_users = []
# #     #     try:
# #     #         connection = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), host=os.getenv("POSTGRES_HOST"), password=os.getenv("POSTGRES_PASSWORD"))
# #     #         cursor = connection.cursor()
# #     #         cursor.execute("select * from registration;")
# #     #         row_query = cursor.fetchall()
# #     #         connection.close()
# #     #         return {"User Created": row_query}
# #     #     except:
# #     #         return {"check" : False}
# class Postgres():
#     def alchemy():
#         engine = create_engine(
#             "postgresql+psycopg2://mifa43:koliko43@user-service-postgres-dev/userservice",
#             isolation_level="SERIALIZABLE",
#         )
#         db = scoped_session(sessionmaker(bind=engine))
#         # db.execute("""
#         # CREATE TABLE IF NOT EXISTS userservice.registration (
#         # id SERIAL PRIMARY KEY,
#         # name varchar(45) NOT NULL,
#         # lastName varchar(45) NOT NULL,
#         # mail varchar(45) NOT NULL,
#         # phoneNumber varchar(15) NOT NULL,
#         # password varchar(15) NOT NULL
#         # );
#         # """)
#         db.execute("""
#         INSERT INTO registration (name, lastName, mail, phoneNumber, password)
#         VALUES ('Milos', 'Zlatkovic', 'mifa43kotez@gmail.com', '0600977458', 'koliko1212');
#         """)
#         db.commit()
#         db.close()

#         return {"status": 1}