from Index import *
# ----------------------------------------------------------------

def drop_tables():
    cursor.execute('''DROP TABLE IF EXISTS users;
                   DROP TABLE IF EXISTS classes''')

def create_tables():
    cursor.execute('''CREATE TABLE users 
                    (user_id serial PRIMARY KEY
                    , username varchar(100),
                    password varchar(200))''')
    cursor.execute('''CREATE TABLE classes
                    (id serial PRIMARY KEY
                    , name varchar(150))''')

def class_seed():
    cursor.execute('''INSERT INTO classes (id, name)
                   VALUES
        (1, 'Warrior'),
        (2, 'Ranger'),
        (3, 'Sorceress'),
        (4, 'Berserker'),
        (5, 'Tamer'),
        (6, 'Musa'),
        (7, 'Maewha'),
        (8, 'Valkyrie'),
        (9, 'Kunoichi'),
        (10, 'Ninja'),
        (11, 'Wizard'),
        (12, 'Witch'),
        (13, 'Mystic'),
        (14, 'Striker'),
        (15, 'Dark Knight'),
        (16, 'Lahn'),
        (17, 'Archer'),
        (18, 'Shai'),
        (19, 'Guardian'),
        (20, 'Hashashin'),
        (21, 'Nova'),
        (22, 'Sage'),
        (23, 'Corsair'),
        (24, 'Drakania')''')


# ----------------------------------------------------------------
drop_tables()
create_tables()
class_seed()
connect.commit()
connect.close()
# ----------------------------------------------------------------
