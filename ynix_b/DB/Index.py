import psycopg2
from dotenv import dotenv_values
#----------------------------------------------------------------
config = dotenv_values(".env")
print(config['USER_NAME'])
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']
print(config)
#----------------------------------------------------------------
connect = psycopg2.connect(database = "py-lab", user = myUser, password = myPassword, host="localhost", port="5432")
cursor = connect.cursor()
#----------------------------------------------------------------

def drop_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (user_id serial PRIMARY KEY''')

def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (user_id serial PRIMARY KEY''')
    
##----------------------------------------------------------------    
drop_tables() 
create_tables()
connect.commit()
connect.close()
#----------------------------------------------------------------
