from __init__ import cur
#----------------------------------------------------------------

    
async def get_class_list():
    class_list_fetch = await cur.execute('''SELECT * FROM classes''')
    return class_list_fetch

print(get_class_list().count())