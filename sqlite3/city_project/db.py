import sqlite3
from model import city, cityStatus


def addCityInfo(t):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """INSERT INTO city
                          (cityname,areaname,pincode) 
                           VALUES 
                          (?,?,?)"""

        data_tuple = (t.cityname,t.areaname,t.pincode,)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()

        cursor.close()
    
        c = 1

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def changeCityInfo(a,b):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """update city set cityname = (?) where cityname = (?)"""
        data = (b,a)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            c = 1

        cursor.close()
    

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    
    return c

def changeAreaInfo(a,b):
    c = 0
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """update city set areaname = (?) where areaname = (?)"""
        data = (b,a)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            c = 1

        cursor.close()
    

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    
    return c

def viewCityInfo(id):
    el = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from city where cityname = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        
        for row in records:
            t = city(row[0],row[1],row[2])
            i = (t.areaname,t.pincode)
            el.append(i)
            
        cursor.close()

    except sqlite3.Error as error:
        return 0
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el

def pincodeInfo(num):
    es = cityStatus(0,"Not found",None)
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from city where pincode = ?"""
        cursor.execute(sql_select_query, (num,))
        records = cursor.fetchall()

        for row in records:
            t = city(row[0],row[1],row[2])
            s = (t.cityname,t.areaname)
            es.statuscode = 1
            es.message = "City Found"
            es.cityobj = s
            
            
        cursor.close()

    except sqlite3.Error as error:
        es.message = f"{error}"

    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es

def sortCityInfo():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by cityname")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            t = city(row[0],row[1],row[2])
            c.append(t)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def sortAreaInfo():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by areaname")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            t = city(row[0],row[1],row[2])
            c.append(t)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c

def sortPinInfo():
    c = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT * FROM city order by pincode")
        records = cursor.fetchall()
        sqliteConnection.commit()
        
        cursor.close()
        for  row in records:
            t = city(row[0],row[1],row[2])
            c.append(t)

    except sqlite3.Error as error:
        return c
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return c