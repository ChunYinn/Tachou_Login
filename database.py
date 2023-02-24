from flask import Flask, render_template, url_for, request, redirect
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from datetime import datetime
import MySQLdb.cursors
import pymysql

def database_connection():
    conn = None
    try:
        conn=pymysql.connect(
            host='localhost',
            user='root',
            password="",
            db='dachou'
        )

    except Exception:
        print("Error in database connection")
        return None

    return conn

# login verification
def verify_login():
    inpt_username = request.form.get("username")
    inpt_passward = request.form.get("password")

    conn = database_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    cursor.execute("select * from account")
    data=cursor.fetchall()

    for i in range(len(data)):
        if data[i][1]==inpt_username and \
            data[i][2]==inpt_passward:
            return data[i][3] #name
    return None

def get_rework_list():
    conn = database_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    sql ="""
       SELECT return_date, customer_name, product_name, rework_quantity, product_specification, product_color, return_reason 
       FROM Customer, Rework, Product, ReturnT, orders 
       WHERE customer.customer_id = orders.customer_id 
            AND rework.return_id = returnt.return_id 
            AND rework.product_id = product.product_id 
            AND rework.orders_id = orders.orders_id;
        """
    cursor.execute(sql)
    data=cursor.fetchall()

    return data