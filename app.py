import sqlite3

def create_db():
    try:
        with sqlite3.connect("db.sqlite") as con:
            sql_cmd = f"""
                CREATE TABLE person(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    firstname text,
                    lastname text,
                    account_name text,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            con.execute(sql_cmd)
    except Exception as e:
        print(f'Error (create_db) -> {e}')

def insert_db(params):
    try:
        with sqlite3.connect("db.sqlite") as con:
            sql_cmd = f"""
                INSERT INTO person(
                    firstname,
                    lastname,
                    account_name
                ) values (?, ?, ?)
            """
            con.execute(sql_cmd, params)

    except Exception as e:
        print(f'Error (insert_db) -> {e}')    

def select_db():
    try:
        with sqlite3.connect("db.sqlite") as con:
            sql_cmd = f"""
                SELECT
                id,
                firstname,
                lastname,
                account_name,
                datetime(timestamp, 'localtime')
                from 
                person
            """
            for row in con.execute(sql_cmd):
                print(row)

    except Exception as e:
        print(f'Error (select_db) -> {e}')    

def delete_db():
    try:
        with sqlite3.connect("db.sqlite") as con:
            sql_cmd = f"""
                DELETE FROM person WHERE name = 'user1'
            """
            con.execute(sql_cmd)

    except Exception as e:
        print(f'Error (delete_db) -> {e}')    

if __name__ == "__main__":
    create_db()
    insert_db(["firstname", "lastname", "account_name"])
    select_db()
    # delete_db()