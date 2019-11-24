import sqlite3
import csv

def createDBtable(db):
    # conn = sqlite3.connect(db)
    # cur = conn.cursor()
    # sql = '''
    #         CREATE TABLE if not exists supply
    #         (supplier_name varchar(30),
    #         invoice_number varchar(30),
    #         part_number varchar(20),
    #         cost integer,
    #         purchase_date date)
    #
    #     '''
    # print("생성완료")
    # cur.execute(sql)
    # conn.commit()
    # conn.close()
    pass

def saveDBtable(db, data):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = '''INSERT INTO supply(supplier_name,invoice_number,part_number,cost,purchase_date)
             VALUES(?,?,?,?,?)
            '''
    cur.execute(sql,data)
    conn.commit()
    conn.close()


def viewDBdata(db, table):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = 'SELECT * FROM {0}'.format(table)
    cur.execute(sql)

    rows = cur.fetchall()
    print(rows)
    for row in rows:
        print(row)
    conn.close()


if __name__ == '__main__':

    db_name = '../db/supplyDB.db'

    # (1) DB에 테이블 생성
    # createDBtable(db_name)

    # ------------------------------------------------------
    # (2) csv파일을 읽어서 DB에 테이블 입력
    # file_name='../files/supply.csv'
    # file = csv.reader(open(file_name,'r'), delimiter=',')
    # header = next(file,None)
    # print(header)
    # for row in file:
    #      saveDBtable(db_name,row)

    # ------------------------------------------------------
    # (3) DB에 저장되어 있는 테이블값 출력
    viewDBdata(db_name, 'supply') # 디비명, 테이블명
