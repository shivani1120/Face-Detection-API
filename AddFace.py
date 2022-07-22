from zipfile import ZipFile
from fastapi import FastAPI, File, UploadFile, Form
import face_recognition
import os
from os import listdir
import psycopg2
import numpy as np
from pathlib import Path
from database import Database



class Addface:
        
        # to add single image
        def add_one(self, file:UploadFile):
                # file name
                img = file.filename
                # connect to database
                db = Database()
                name_of_file = ""
                # check file format
                try:

                        # load image
                        picture_of_me =  face_recognition.load_image_file(file.file)

                        
                        # check if image is very small or not a face image
                        

                        # find encoding
                        encoding =  face_recognition.face_encodings(picture_of_me)[0]
                        # convert encoding in str
                        file_data = ','.join([str(i) for i in encoding])
                        name =  os.path.splitext(img)[0]
                        name_of_file = name
                        # query for insertion
                        query = "INSERT INTO image (name, file_data) VALUES (%s, %s)"

                        # execution of query
                        db.execute(query, (name, file_data))
                        db.commit()
                        

                except:
                        return {"This is not a face Image"}
                return name
                
                



        # to add multiple images
        def add_bulk(self, myzip:UploadFile):
                file_name = myzip.filename
                db = Database()
                mylist = []
        
                try:
                        
                        # opening the zip file in READ mode
                        with ZipFile(myzip.file, 'r') as zip:
                        # printing all the contents of the zip file
                                
                                files = zip.namelist()
                                

                        for file in files:
                                # check for format
                                if (file.lower().endswith(('.png', '.jpg', '.jpeg'))):

                                        # load file
                                        picture_of_me =  face_recognition.load_image_file(file)
                                        # image isto small
                                        if len(face_recognition.face_locations(picture_of_me)) == 0:
                                                continue
                                        # check for encodings
                                        elif len(face_recognition.face_encodings(picture_of_me)) > 0:
                                                
                                                # find encodings
                                                encoding =  face_recognition.face_encodings(picture_of_me)[0]
                                                file_data = ','.join([str(i) for i in encoding])

                                                # get name of file
                                                name =  os.path.splitext(file)[0]
                                                
                                                mylist.append(name)
                                                # execute query
                                                db.execute("INSERT INTO image (name, file_data) VALUES (%s, %s)", (name, file_data))
                                                db.commit()
                                
                        
                except:
                        mylist.append("Not a zip file")

                return mylist



        











# for subdir in os.listdir(directory):
# for filename in os.listdir(f"{directory}/{subdir}"):
# img = f"{directory}/{subdir}/{filename}"
# if (img.endswith(".jpg")):
# picture_of_me = face_recognition.load_image_file(img)
# if len(face_recognition.face_encodings(picture_of_me)) > 0:
#         # find encoding
#         encoding = face_recognition.face_encodings(picture_of_me)[0]
#         file_data = np.array_str(encoding)
#         name = os.path.splitext(filename)[0]
#         # insert into database
#         mycursor.execute("INSERT INTO images (name, file_data) VALUES (%s, %s)", (name, file_data))
#         mydb.commit()

# mycursor.close()
# mydb.close()













# mydb = psycopg2.connect(host="localhost", user="apple", password="kumari12345", database="postgres")
# mycursor = mydb.cursor()
# # mycursor.execute("CREATE TABLE images  (name VARCHAR PRIMARY KEY, file_data TEXT NOT NULL);")
# folder_dir = "/Users/apple/Desktop/new1"
# for images in os.listdir(folder_dir):
 
#     # check if the image ends with png
#     if (images.endswith(".jpg")):
#         # f = open(images,'rb')
#         # filedata = f.read()
#         picture_of_me = face_recognition.load_image_file(images)
#         encoding = face_recognition.face_encodings(picture_of_me)[0]
#         file_data = np.array_str(encoding)
#         print(file_data)
        
#         mycursor.execute("INSERT INTO images (name, file_data) VALUES (%s, %s)", (name, filedata))
        # mydb.commit()
# mydb.commit()
# mycursor.close()
# mydb.close()


# picture_of_me = face_recognition.load_image_file("Aaron_Eckhart_0001.jpg")
# my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
# print(my_face_encoding)

# cur = mydb.cursor(cursor_factory=psycopg2.extras.Dictcursor)
# mycursor.execute("CREATE TABLE images  (name VARCHAR PRIMARY KEY, encoding text);")
# mycursor.execute("INSERT INTO books (id,name) VALUES (%s,%s)", (2, "Triogory",))






# import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", password="kumari12345", database="images")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE IF NOT EXISTS Img (name VARCHAR(100) NOT NULL PRIMARY KEY, pic LONGBLOB NOT NULL)")
# for i in mycursor:
#     print(i)
# sql = "INSERT INTO img (name, encoding) VALUES (%s, %s)"
        # val = (name, "Highway 21")



# import psycopg2

# l1 = [1.0,2.0,3.0]
# l2 = [2.0,2.0,4.0,5.0]
# mydb = psycopg2.connect(host="localhost", user="apple", password="kumari12345", database="postgres")
# mycursor = mydb.cursor()
# mycursor.execute("INSERT INTO images (name, encoding) VALUES (%s, %s)", ("pic1", l1))

# with mydb.cursor(cursor_factory=psycopg2.extras.Dictcursor) as cur:
#     cur.execute("SELECT * FROM books WHERE id = %s;",(1, ))
#     print(cur.fetchone()['id'])


# for i in mycursor:
#     print(i)


# get the path/directory














