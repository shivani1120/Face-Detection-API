
from database import Database

# apikey, face_id
class FaceInfo:
    def faceinfo(self,face_id):
        img_details = {}
        try:
            # connect to database
            db = Database()
            # convert id to int
            id = int(face_id)

            query = "SELECT * FROM image WHERE id= %s;"

            # if id is grater than table size 
            try:
                # fetch all the records
                records = db.query(query,(id,))

                for row in records:
                    img_details["id"] = str(row[0])
                    img_details["name"] = row[1]
                    img_details["encoding"] = row[2]  
            except:
                print("Invalid id")
        except:
            print("Unable to connect to Database")
        
        # return the image details
        return img_details
        






