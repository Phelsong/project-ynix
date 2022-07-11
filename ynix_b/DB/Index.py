import psycopg2
from dotenv import dotenv_values
# ----------------------------------------------------------------
config = dotenv_values("../../.env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']
# ----------------------------------------------------------------
connect = psycopg2.connect(database="ynix_db", user=myUser,
                           password=myPassword, host="localhost", port="5432")
cursor = connect.cursor()
# ----------------------------------------------------------------


def drop_tables():
    cursor.execute('''DROP TABLE IF EXISTS users''')


def create_tables():
    cursor.execute('''CREATE TABLE users 
                    (user_id serial PRIMARY KEY
                    , username varchar(100),
                    password varchar(100))''')


# ----------------------------------------------------------------
drop_tables()
create_tables()
connect.commit()
connect.close()
# ----------------------------------------------------------------
