import psycopg2
from hash_maker import hash_maker

def connect():
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "12345",port = 5432)
        return conn
    except (Exception,psycopg2.Error) as error:
        print(error)
        
def tablecheck2():
    try:
        connection = connect()
        cursor = connection.cursor()
        table_query = """CREATE TABLE IF NOT EXISTS accounts2(
            email VARCHAR(255),
            password VARCHAR(255)
            )"""
        cursor.execute(table_query)
        connection.commit()
    except (Exception,psycopg2.Error) as error:
        print(error)

def store_password2(email,password):
    password = hash_maker(password)
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck2()
        insert_query = """ INSERT INTO accounts2 (email, password) VALUES (%s, %s)"""
        record_to_insert = (email,password)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
    except (Exception,psycopg2.Error) as error:
        print(error)

def check_password(password):
    password = hash_maker(password)
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck2()
        insert_query = """SELECT * FROM accounts2 WHERE password = %s"""
        record_to_insert = (password,)
        cursor.execute(insert_query, record_to_insert)
        rows = cursor.fetchall()
        for row in rows:
            email = row[0] 
        connection.commit()
        return email
    except (Exception,psycopg2.Error) as error:
        return error

def check_email(email):
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck2()
        insert_query = """SELECT * FROM accounts2 WHERE email = %s"""
        record_to_insert = (email,)
        cursor.execute(insert_query, record_to_insert)
        rows = cursor.fetchall()
        for row in rows:
            email = row[0] 
        connection.commit()
        return email
    except (Exception,psycopg2.Error) as error:
         return error