#!C:/Python36-32/python.exe

import pymysql
import cgi


connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='register_db',autocommit=True)
cur = connection.cursor()
form = cgi.FieldStorage()

def create_table():
    cur.execute("Create table user(id INT(20),name VARCHAR(255),"
            " email VARCHAR(50), password VARCHAR(255))")

def print_html(username,email):
    print("""
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Calculator</title>
    <style>
        h2 {
         color: red;
         }
    </style>
</head>
<body>
<h1>Registered Successfully %s</h1>
<h2>Email is %s</h2>
</body>
</html>
"""%(username,email))

def insert_query():

    username = form.getvalue("username")
    email = form.getvalue("email")
    pwd = form.getvalue("pwd")
    u_id = 0
    # username = "Ravi"
    # email = "ravi@gmail.com"
    # pwd = "1234abcd"
    u_id += 1

    sql = "INSERT INTO user(id,name,email,password) VALUES(%s, %s, %s, %s)"
    cur.execute(sql, (u_id,username,email,pwd))

    # cur.execute("INSERT INTO user(id,name,email,password) VALUES(2,'KK','kk@gmail.com','sdaas')")

    print_html(username, email)


insert_query()

cur.close()
connection.close()