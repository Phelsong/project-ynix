from Index import *
# ----------------------------------------------------------------


def drop_tables():
    cur.execute('''
                   DROP TABLE IF EXISTS zones;
                   DROP TABLE IF EXISTS class_skills;
                   DROP TABLE IF EXISTS class_data;
                   DROP TABLE IF EXISTS classes;
                   DROP TABLE IF EXISTS users;
                   ''')

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
                   skill_details JSON);
                   ''')
    cur.execute('''CREATE TABLE class_data
                (class_id REFERENCES classes(class_id) NOT NULL,
                pvp_class_mods json);''')
    cur.execute('''CREATE TABLE zones
                (zone_id INT PRIMARY KEY,
                zone_name VARCHAR(200) NOT NULL,
                region VARCHAR(200) NOT NULL,
                zone_dr INT,
                zone_ev INT,
                mob_type VARCHAR(200) NOT NULL,;''')

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

def zone_seed():
    
    cur.execute('''INSERT INTO TABLE zones
                (zone_id SERIAL PRIMARY KEY,
                zone_name VARCHAR(200) NOT NULL,
                region VARCHAR(200) NOT NULL,
                zone_dr INT,
                zone_ev INT,
                mob_type VARCHAR(200) NOT NULL;''')
    

# ----------------------------------------------------------------
drop_tables()
create_tables()
class_seed()
conn.commit()
conn.close()
# ----------------------------------------------------------------
