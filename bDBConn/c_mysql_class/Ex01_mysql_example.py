import MySQLdb
import csv

conn = MySQLdb.connect(host='localhost',user='scott',passwd='tiger', db='pythondb')
# print(conn.version)

cur = conn.cursor()
sql = '''create table if not exists emp (
    empno integer,
    ename varchar(20),
    job varchar(20),
    mgr integer,
    hiredate date,
    sal float,
    comm float,
    deptno integer
)'''

cur.execute(sql)
# datas = cur.fetchall()
# for row in datas:
#     print(row[0], row[1], row[5])
cur.close()
conn.close()
