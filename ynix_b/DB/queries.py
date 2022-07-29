from __init__ import cur, conn
#----------------------------------------------------------------

def get_class_list_query():
    cur.execute('''SELECT * FROM classes''')
    class_list_fetch = cur.fetchall()
    return class_list_fetch
#----------------------------------------------------------------

def get_class_query(class_id):
    cur.execute('''SELECT * FROM classes
                WHERE class_id= %s ;''', (class_id,))
    class_info = cur.fetchall()
    return class_info
    
#-----------------------------------------------------------------
def get_zone_list_query():
    cur.execute('''SELECT * FROM zones''')
    zone_list_fetch = cur.fetchall()
    return zone_list_fetch

#----------------------------------------------------------------
def get_zone_query(zone_id):
    cur.execute('''SELECT * FROM zones
                WHERE zone_id = %s ; ''', (zone_id,))
    zone_info_fetch = cur.fetchall()
    return zone_info_fetch


#----------------------------------------------------------------
conn.commit()