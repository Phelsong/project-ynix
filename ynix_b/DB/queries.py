from __init__ import cur, conn
#----------------------------------------------------------------

def get_class_list():
    cur.execute('''SELECT * FROM classes''')
    class_list_fetch = cur.fetchall()
    return class_list_fetch
#----------------------------------------------------------------

def get_zone_list():
    cur.execute('''SELECT * FROM zones''')
    zone_list_fetch = cur.fetchall()
    return zone_list_fetch




#----------------------------------------------------------------
conn.commit()