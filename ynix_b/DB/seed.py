from Index import *
# ----------------------------------------------------------------


def drop_tables():
    cur.execute('''DROP TABLE IF EXISTS users;
                   DROP TABLE IF EXISTS classes;
                   DROP TABLE IF EXISTS class_skills;''')

def create_tables():
    cur.execute('''CREATE TABLE users 
                    (user_id serial PRIMARY KEY
                    , username varchar(100) NOT NULL,
                    password varchar(200))''')
    cur.execute('''CREATE TABLE classes
                    (class_id SERIAL PRIMARY KEY ,
                    class_name VARCHAR(150) NOT NULL)''')
    cur.execute('''CREATE TABLE class_skills
                   (skill_id SERIAL PRIMARY KEY,
                   "class_id" INT REFERENCES classes(class_id) NOT NULL,
                   skill_name VARCHAR(200) NOT NULL,
                   skill_acc INT NOT NULL,
                   skill_details JSONB);
                   ''')

def class_seed():
    cur.execute('''INSERT INTO classes (class_id, class_name)
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
        (13, 'Dark Knight'),
        (14, 'Striker'),
        (15, 'Mystic'),
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
conn.commit()
conn.close()
# ----------------------------------------------------------------
