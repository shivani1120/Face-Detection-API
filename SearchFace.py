from heapq import heappop, heappush, heapify
import face_recognition
from fastapi import UploadFile
from database import Database
import numpy as np


class SearchFace:
    def searchFace(self, file:UploadFile, k:int,strictness:float):
        
        matches = {}
        # Load the jpg file into a numpy array
        try:
            test_image_name = file.file
            image = face_recognition.load_image_file(test_image_name)
            face_locations = face_recognition.face_locations(image)

            db = Database()
            query = "SELECT * FROM image"
            records = db.query(query)
            db_encodings = []

            # find encodings all the database images
            for row in records:
                str = row[2]
                arr = [float(i) for i in str.split(',')]
                encoding = np.array(arr)
                db_encodings.append(encoding)




            total_faces = len(face_locations)
            for i in range(total_faces):


                test_image_encoding = face_recognition.face_encodings(image)[i]
                face_distances = face_recognition.face_distance(db_encodings, test_image_encoding)
                
                heap = []
                heapify(heap)

                for j, face_distance in enumerate(face_distances):        
                    if(face_distance < strictness):
                        new_dis = -1.0 * face_distance
                        if(len(heap) < k):
                            heappush(heap, (new_dis,records[j][0],records[j][1]))
                        elif(new_dis > heap[0][0]):
                                heappop(heap)
                                heappush(heap,(new_dis,records[j][0],records[j][1]))
                
                face = 'face{}'.format(i)
                
                klist = []
                while len(heap) != 0:
                    mydic = {}
                    matching_test_image_name = heappop(heap)
                    mydic["id"] = matching_test_image_name[1]
                    mydic["name"] = matching_test_image_name[2]
                    klist.append(mydic)
                klist.reverse()
                matches[face] = klist
            print(matches)
        except:
            print("error")
        return matches













