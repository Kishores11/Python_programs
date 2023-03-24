import sqlite3
from model import employee, employeeStatus


def getEmployeeInfo(num):
    es = employeeStatus(0, "Not found", None)
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from employee where empno = ?"""
        cursor.execute(sql_select_query, (num,))
        records = cursor.fetchall()

        for row in records:
            t = employee(row[0], row[1], row[2])
            es.statuscode = 1
            es.message = "Employee Found"
            es.empobj = t

        cursor.close()

    except sqlite3.Error as error:
        es.message = f"{error}"

    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es


def getDeptInfo(id):
    el = []
    try:
        sqliteConnection = sqlite3.connect('test.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from employee where deptid = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()

        for row in records:
            t = employee(row[0], row[1], row[2])
            el.append(t)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el
