import psycopg2

# Note : à la suite du TP 2 vous aurez les connaissances pour stoker ce grenre d'info dans un fichier de
# configuration externe.
MY_ID = ...
HOST = "sgbd-eleves.domensai.ecole"
PORT = "5432"

connection = psycopg2.connect(host=HOST, port=PORT,
                              database=MY_ID, user=MY_ID, password=MY_ID)