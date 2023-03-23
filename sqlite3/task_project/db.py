import sqlite3
from model import Task



def ifPresent(t):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT taskid FROM task_project where taskid = ?",(t,))
        row = cursor.fetchone()
        if row:
            return 1

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    



def addTaskInfo(t):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO task_project
                          (taskid,taskname,taskdesc,taskpriority) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (t.id,t.name,t.desc,t.priority)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def updateTaskInfo(t):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """Update task_project set (taskname,taskdesc,taskpriority) = (?,?,?)  where taskid = ?"""
        data = (t.name,t.desc,t.priority,t.id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            return 1

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def viewTaskInfo(num):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from task_project where taskid = ?"""
        cursor.execute(sql_select_query, (num,))
        records = cursor.fetchall()

        for row in records:
            t = Task(row[0],row[1],row[2],row[3])
            
        cursor.close()

    except sqlite3.Error as error:
         print("error")

    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return t

def removeTaskInfo(t):
    es = 0
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_delete_query = """delete from task_project where taskid = ?"""
        cursor.execute(sql_delete_query, (t,))
        sqliteConnection.commit()

            
        cursor.close()

        es = 1

    except sqlite3.Error as error:
         print("error",error)

    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es

    

