from main import cur, conn
from pve_data import zone_list
from class_list import class_list
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
                zone_evasion INT,
                mob_type VARCHAR(200) NOT NULL,;''')


def class_seed():
    for char in class_list.values():
        cur.execute('''INSERT INTO classes (class_id, class_name)
                   VALUES ({char.id}, {char.name})''')


def zone_seed():
    for zone in zone_list.values():
        cur.execute('''INSERT INTO zones (zone_id, zone_name, region, zone_dr, zone_evasion, mob_type) VALUES (?,
                VALUES ({zone.id}, {zone.name}, {zone.region}, {zone.dr}, {zone.evasion}, {zone.mob_type}''')


# ----------------------------------------------------------------
drop_tables()
create_tables()
class_seed()
zone_seed()
conn.commit()
conn.close()
# ----------------------------------------------------------------
