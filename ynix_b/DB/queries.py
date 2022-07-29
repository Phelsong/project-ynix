from __init__ import cur, conn
#----------------------------------------------------------------

    
def get_class_list():
    cur.execute('''SELECT * FROM classes''')
    class_list_fetch = cur.fetchall()
    print(class_list_fetch)
    return class_list_fetch

get_class_list()

conn.commit()