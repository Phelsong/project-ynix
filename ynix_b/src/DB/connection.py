import psycopg
from dotenv import dotenv_values
from psycopg.rows import dict_row

# ----------------------------------------------------------------
config = dotenv_values("../../../.env")
my_user = config["USER_NAME"]
my_pass = config["PASS_WORD"]
lab_db = config["LAB_DB"]
lab_db_server = config["LAB_DB_SERVER"]
lab_db_port = config["LAB_DB_PORT"]

# ----------------------------------------------------------------
conn = psycopg.connect(
    hostaddr=lab_db_server,
    port=lab_db_port,
    dbname=lab_db,
    user=my_user,
    password=my_pass,
    row_factory=dict_row,
)
alt_conn = psycopg.connect(
    hostaddr=lab_db_server,
    port=lab_db_port,
    dbname=lab_db,
    user=my_user,
    password=my_pass,
)
alt_cur = alt_conn.cursor()
cur = conn.cursor()
