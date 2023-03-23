import sqlite3

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

msg = ifPresent(99)
print(msg)