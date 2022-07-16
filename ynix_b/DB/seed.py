from Index import *
# ----------------------------------------------------------------

def drop_tables():
    cursor.execute('''DROP TABLE IF EXISTS users,
                   DROP TABLE IF EXISTS classes''')


def create_tables():
    cursor.execute('''CREATE TABLE users 
                    (user_id serial PRIMARY KEY
                    , username varchar(100),
                    password varchar(200))''')
    cursor.execute('''CREATE TABLE classes
                    (user_id serial PRIMARY KEY
                    , name varchar(100))''')


# ----------------------------------------------------------------
drop_tables()
create_tables()
connect.commit()
connect.close()
# ----------------------------------------------------------------
