#!C:/Python36-32/python.exe

import pymysql
import cgi


connection = pymysql.connect(host='localhost', port=3306, user='root',
                       passwd='', db='register_db',autocommit=True)
cur = connection.cursor()
form = cgi.FieldStorage()

def print_html(cur):

    for username in cur:
        pass

    print("""
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Login</title>
    <link type="text/css" rel="stylesheet" href='/Py_Batch/RegisterDB/main.css'>
</head>
<body>
<h1>Logged in {}</h1>
</body>
</html>
""".format(username[1]))



def insert_query():

    email = form.getvalue("email")
    pwd = form.getvalue("pwd")

    # email = 'john@gmail.com'
    # pwd = 'johnyjohny'

    sql = "Select * from user WHERE email = %s AND password = %s"
    cur.execute(sql, (email,pwd))

    # for row in cur:
    #     print(row[1])

    print_html(cur)

insert_query()

cur.close()
connection.close()