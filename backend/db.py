import mysql.connector
from mysql.connector import Error
hostname = 'localhost'
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
            
            for field in cursor:
                fields.append(field)

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
