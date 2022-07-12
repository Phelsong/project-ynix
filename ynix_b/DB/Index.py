import psycopg2
from dotenv import dotenv_values
# ----------------------------------------------------------------
config = dotenv_values("../../.env")
myUser = config['USER_NAME']
myPassword = config['PASS_WORD']
# ----------------------------------------------------------------
connect = psycopg2.connect(database="ynix_db", user=myUser,
                           password=myPassword, host="localhost", port="5432")
cursor = connect.cursor()
# ----------------------------------------------------------------

