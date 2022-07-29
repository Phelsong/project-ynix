import psycopg
from dotenv import dotenv_values
# ----------------------------------------------------------------
config = dotenv_values("../../.env")
my_user = config['USER_NAME']
my_pass = config['PASS_WORD']
lab_db = config['LAB_DB']
lab_db_server = config['LAB_DB_SERVER']
lab_db_port = config['LAB_DB_PORT']

# ----------------------------------------------------------------
conn = psycopg.connect(hostaddr=lab_db_server, port=lab_db_port, dbname=lab_db, user=my_user, password=my_pass )
cur = conn.cursor()
