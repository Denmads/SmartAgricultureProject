import mysql.connector
from mysql.connector import Error
from Field import Field
import sys

hostname = 'localhost'
db_module = sys.modules[__name__]
try:
    connection = mysql.connector.connect(host=hostname,
                                         database='hub',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ff;")
        
        for record in cursor:
            print(record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



def getAllDrones():
    drones = []
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM drone;")
            
            for drone in cursor:
                drones.append(drone)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return drones

def getAllField():
    fields = []
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ff;")
            result = cursor.fetchall
            
            for field in cursor:
                fields.append(Field(id=field[0], width=field[1], height=field[2], name=field[3]))

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return fields

def updatePos(DroneId, x, y):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"UPDATE drone SET x ={x}, y = {y} WHERE Droneid = {DroneId};")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def updateStatus(droneId, status):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"UPDATE drone SET DroneStatus = {status} WHERE Droneid = {droneId};")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_into_db(quary):
    a = -1
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(quary)
            a = cursor.lastrowid
        
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    return a

def delete_field(id):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM ff WHERE `Fieldid` = {id};")
            
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()