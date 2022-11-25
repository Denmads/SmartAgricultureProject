import mysql.connector
import sys
from Drone import Drone
from Field import Field
from job import Job
from mysql.connector import Error
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



def getAllDrones(fields):
    drones = []
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM drone;")
            result = cursor.fetchall()

            for drone in result:

                if drone[4] == -1:
                    drones.append(Drone(None, drone[0], db_module))
                else:
                    field = list(filter(lambda field: field.id == drone[4], fields))[0]
                    drones.append(Drone(field, drone[0]))

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
            result = cursor.fetchall()
            
            for field in result:
                fields.append(Field(id=field[0], width=field[1], height=field[2], name=field[3], db=db_module))

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return fields

def getAllJobs(fields, drones):
    jobs = []
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM job;")
            result = cursor.fetchall()
            
            for job in result:
                jobId = job[0]
                job_list = list(filter(lambda job: job.id == jobId, jobs))
                if len(job_list) > 0: 
                    da_drone = list(filter(lambda drone: drone.id == job[1], drones))[0]
                    job_list[0].droneslist.append(da_drone)
                else:
                    da_drone = list(filter(lambda drone: drone.id == job[1], drones))[0]
                    da_field = list(filter(lambda field: field.id == job[2], fields))[0]
                    job = Job(db_module, da_field, [da_drone], jobId)
                    jobs.append(job)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return jobs

def updatePos(DroneId, x, y):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"UPDATE drone SET x ={x}, y = {y} WHERE Droneid = '{DroneId}';")
            connection.commit()

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
            cursor.execute(f"UPDATE drone SET DroneStatus = '{status}' WHERE Droneid = '{droneId}';")
            connection.commit()

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
            cursor.execute(f"DELETE FROM ff WHERE Fieldid = {id};")

            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_job(id):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM job WHERE jobId = {id};")

            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def save_image(self, id, image):
    try:
        connection = mysql.connector.connect(host=hostname,
                                            database='hub',
                                            user='root',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"UPDATE drone SET Camera = '{image}' WHERE Droneid = '{droneId}';")
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()