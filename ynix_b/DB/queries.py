from __init__ import alt_cur, cur, conn
import json
#----------------------------------------------------------------

def get_class_list_query():
    cur.execute('''SELECT * FROM classes''')
    return cur.fetchall()
#----------------------------------------------------------------

def get_class_query(class_id):
    cur.execute('''SELECT * FROM classes
                WHERE class_id= %s ;''', (class_id,))
    return cur.fetchall()
    
#-----------------------------------------------------------------
def get_zone_list_query():
    cur.execute('''SELECT * FROM zones''')
    return cur.fetchall()

#----------------------------------------------------------------
def get_zone_query(zone_id):
    cur.execute('''SELECT * FROM zones
                WHERE zone_id = %s ; ''', (zone_id,))
    return cur.fetchall()


#----------------------------------------------------------------
conn.commit()