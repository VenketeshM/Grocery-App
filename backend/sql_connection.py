import mysql.connector
__db = None


def get_sql_connection():
    global __db
    if __db is None:
        __db = mysql.connector.connect(
            user="root",
            password="2004",
            host="127.0.0.1",
            database="grocery_store")
    return __db
