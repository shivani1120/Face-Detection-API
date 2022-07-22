
from typing import Dict, List, Optional
from fastapi import FastAPI, File, UploadFile, Form
from AddFace import Addface
from SearchFace import SearchFace
from FaceInfo import FaceInfo



app = FastAPI()


@app.post("/search_faces/")
def search_faces(k: Optional[int]= 5, strictness: Optional[float] = 0.6, file: UploadFile = File(..., description="An image file, possible containing multiple human faces.")):
    searchFace = SearchFace()
    matches = searchFace.searchFace(file,k,strictness)
    return {"status": "200", "body": {"matches": matches}}



@app.post("/add_face/")
def add_face(file: UploadFile):
    AddFace = Addface()
    name = AddFace.add_one(file)
    return {"status":"200","body":name}



@app.post("/add_faces_in_bulk/")
def add_faces_in_bulk(file: UploadFile = File(..., description="A ZIP file containing multiple face images.")):
    addFace = Addface()
    images = addFace.add_bulk(file)
    return {"status":"200", "body":images }
    

@app.post("/get_face_info/")
def get_face_info(face_id: str = Form(...)):
    faceInfo = FaceInfo()
    face = faceInfo.faceinfo(face_id)
    return {"status":"200", "body":face}

























# # from add_face import *

# # @app.get("/")
# # def root():
# # #     return{"hello"}

# # @app.post("/search_faces/")
# # async def search_faces(file: UploadFile =
# #                       File(..., description="An image file, possible containing multiple human faces.")):
# #    # TODO: Implement the logic for performing the facial search
# #    # return {"status": "OK", "body": {"matches": [{"id": 112, "person_name": "JK Lal"}]}}
# #    return {"status": "ERROR", "body": "Not implemented yet"}


# # @app.post("/add_face/")
# # async def add_face(file: UploadFile = File(..., description="An image file having a single human face.")):

# #     # Connect to databse


    


# # @app.post("/add_faces_in_bulk/")
# # async def add_faces_in_bulk(file: UploadFile =
# #                            File(..., description="A ZIP file containing multiple face images.")):
# #    # TODO: Implement the logic for saving the face details in DB
# #    return {"status": "ERROR", "body": "Not implemented yet"}


# # @app.post("/get_face_info/")
# # async def get_face_info(api_key: str = Form(...), face_id: str = Form(...)):
# #    # TODO: Implement the logic for retrieving the details of a face record from DB.
# #    return {"status": "ERROR", "body": "Not implemented yet"}

