-> What does this program do?
    This program implements an application to do "facial search" on a database of images.
    The application provides a secure API service that gets invoked by sending a HTTP POST request.
    API endpoint is provided to search the database of images and find top-k match with a minimum confidense level.
    Api endpoints are provided to add faces to the database one by one or from a zip file, where all images in the zip file get added to the database.
    Api endpoints are also provided to get meta-data of a particular image as well as to add meta data to a particular image of the database.


->To run the server, first install all the dependecies
    pip3 install fastapi
    pip3 install uvicorn [standard]
    pip3 install dlib cmake face_recognition psycogy2

->Command to run the server
    uvicorn main:app --reload

->To run the testcases, first install pytest
    pip3 install pytest

->Command to run the testcases
    pytest
    pytest -vv (this commmad is used to see more details)


->main.py contain is basically our server.It is starting point of our program.

CONNECTION TO DATABSES
->databse.by contains all the logic for connecting to databse.It contains a Database class to which contains various methods for connection to database and query execution.
    We can import this module in other module to hide the complexity for connection. It allows to perform all the database operation again again without rewriting the code. 

POPULATE IMAGES IN DATABSES
->To populate one image at a time in the database add_face api should used.The logic for populating images is written in AddFace.py
    AddFace.py have a class AddFace which have two method:
    1. add_one() to populate one image at one time
    2. add_bulk() to populate images from a zip file. add_faces_in_bulk api should be used to populate a zip file containing images.

GET INFORMATION ABOUT IMAGES
->To get infromation about images get_face_info api is available. The logic to get information is imlementes in FaceInfo.py
    This file have a FaceInfo  class. This class have a method which takes id of an image an retrun its details.

SEARCH FACES
->To search face in a database search_faces api is used. It calls the searchFace function present in SearchFace.py file.
    In searchFace method, First we find out the number of faces in the given images. Then we extract encoding of all images present in database.
    By using face distance ,we find out top k matches with given strictness for each face one by one. Priority queue is used to store all top k matches.
    And then  result is returned.

TESTCASES
->test_main.py contains all the testcases
