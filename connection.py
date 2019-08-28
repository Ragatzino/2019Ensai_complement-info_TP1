import psycopg2

# Note : à la suite du TP 2 vous aurez les connaissances pour stocker ce grenre d'info dans un fichier de
# configuration externe.
MY_ID =
MY_PASSWORD =
HOST = "sgbd-eleves.domensai.ecole"
PORT = "5432"


def get_connection():
    return psycopg2.connect(host=HOST, port=PORT, database=MY_ID, user=MY_ID, password=MY_PASSWORD)
