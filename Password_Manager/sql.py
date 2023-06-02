import psycopg2
import tkinter as tk
import customtkinter

def connect():
    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",password = "12345",port = 5432)
        return conn
    except (Exception,psycopg2.Error) as error:
        print(error)
        
def tablecheck():
    try:
        connection = connect()
        cursor = connection.cursor()
        table_query = """CREATE TABLE IF NOT EXISTS accounts1(
            password VARCHAR(255),
            user_email VARCHAR(255),
            username VARCHAR(255),
            url VARCHAR(255),
            app_name VARCHAR(255)
            )"""
        cursor.execute(table_query)
        connection.commit()
    except (Exception,psycopg2.Error) as error:
        print(error)
           
def store_password(password,user_email,username,url,app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck()
        insert_query = """INSERT INTO accounts1 (password, user_email, username, url, app_name) VALUES (%s, %s, %s, %s,%s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
    except (Exception,psycopg2.Error) as error:
        print(error)

def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck()
        select_query = """SELECT * FROM accounts1 WHERE user_email = %s"""
        record_to_insert = (user_email,)
        cursor.execute(select_query, record_to_insert)
        result = cursor.fetchall()
        for row in result:
            for i in range(0,len(row)):
                text = str(data[i] + row[i])
                return text 
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)
        

def delet_password(password,app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        tablecheck()
        select_query = """DELETE FROM accounts1 WHERE password = %s AND app_name = %s"""
        record_to_insert = (password,app_name)
        cursor.execute(select_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error) 

find_users("Aqib")        