from http import HTTPStatus
from anyio import Path
from click import Parameter, open_file
from fastapi import UploadFile
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
# without Parameter
def test_search_faces_withoutparams():
    
    response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            params={
            },
            files={"file": ("group.jpg", open('/Users/apple/Downloads/group.jpg','rb'), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "matches": {
                "face0": [
                    {
                        "id": 142,
                        "name": "Aishwarya_Rai_0001"
                    },
                    {
                        "id": 13186,
                        "name": "single"
                    },
                    {
                        "id": 13183,
                        "name": "single"
                    },
                    {
                        "id": 13180,
                        "name": "single"
                    },
                    {
                        "id": 10262,
                        "name": "Priyanka_Chopra_0001"
                    }
                ],
                "face1": [
                    {
                        "id": 8290,
                        "name": "Mahima_Chaudhari_0001"
                    },
                    {
                        "id": 9737,
                        "name": "Oxana_Fedorova_0002"
                    },
                    {
                        "id": 12978,
                        "name": "Winona_Ryder_0006"
                    }
                ]
            }
        }
    }


# with params
def test_search_faces_withparams():
    response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            params={
                "k":3,
                "strictness":0.5
            },
            files={"file": ("group.jpg", open('/Users/apple/Downloads/group.jpg','rb'), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "matches": {
                "face0": [
                    {
                        "id": 142,
                        "name": "Aishwarya_Rai_0001"
                    },
                    {
                        "id": 13183,
                        "name": "single"
                    },
                    {
                        "id": 13180,
                        "name": "single"
                    }
                ],
                "face1": []
            }
        }
    }


# with k only
def test_search_faces_withK():
    response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            params={
                "k":2,
            },
            files={"file": ("group.jpg", open('/Users/apple/Downloads/group.jpg','rb'), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "matches": {
                "face0": [
                    {
                        "id": 142,
                        "name": "Aishwarya_Rai_0001"
                    },
                    {
                        "id": 13180,
                        "name": "single"
                    }
                ],
                "face1": [
                    {
                        "id": 8290,
                        "name": "Mahima_Chaudhari_0001"
                    },
                    {
                        "id": 9737,
                        "name": "Oxana_Fedorova_0002"
                    }
                ]
            }
        }
    }



# strictness only
def test_search_faces_withStrictness():
    response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            params={
                "strictness":0.6,
            },
            files={"file": ("group.jpg", open('/Users/apple/Downloads/group.jpg','rb'), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "matches": {
                "face0": [
                    {
                        "id": 142,
                        "name": "Aishwarya_Rai_0001"
                    },
                    {
                        "id": 13189,
                        "name": "single"
                    },
                    {
                        "id": 13186,
                        "name": "single"
                    },
                    {
                        "id": 13183,
                        "name": "single"
                    },
                    {
                        "id": 13180,
                        "name": "single"
                    }
                ],
                "face1": [
                    {
                        "id": 8290,
                        "name": "Mahima_Chaudhari_0001"
                    },
                    {
                        "id": 9737,
                        "name": "Oxana_Fedorova_0002"
                    },
                    {
                        "id": 12978,
                        "name": "Winona_Ryder_0006"
                    }
                ]
            }
        }
    }

# invalid image for search face
def test_search_faces_invalidImageFormat():
    response = client.post(
            "http://127.0.0.1:8000/search_faces/",
            params={
            },
            files={"file": ("1.txt", open('/Users/apple/Documents/1.txt','rb'), "image/jpeg")})
    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "matches": {}
        }
    }

# for uploading sigle file
def test_add_face():
    response = client.post("http://127.0.0.1:8000/add_face/",files={"file":("single.jpg", open('/Users/apple/Downloads/single.jpg','rb'),'image/jpeg')})

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": "single"
    }


# invalid image format
def test_add_face_invalid():
    response = client.post("http://127.0.0.1:8000/add_face/",files={"file":("package-lock.json", open('/Users/apple/Documents/package-lock.json','rb'),'image/jpeg')})

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": [
            "This is not a face Image"
        ]
    }




# for upload zip file 
def test_add_faces_in_bulk():
    response = client.post("http://127.0.0.1:8000/add_faces_in_bulk/",files={"file":("images.zip", open('/Users/apple/Downloads/images.zip','rb'),'image/jpeg')})

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": [
            "Zydrunas_Ilgauskas_0001",
            "Zurab_Tsereteli_0001"
        ]
    }

# not a zip file
def test_add_faces_in_bulk_invalidfile():
    response = client.post("http://127.0.0.1:8000/add_faces_in_bulk/",files={"file":("package-lock.json", open('/Users/apple/Documents/package-lock.json','rb'),'image/jpeg')})

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": [
            "Not a zip file"
        ]
    }


# get face info with valid id
def test_get_face_info():
    response = client.post("http://127.0.0.1:8000/get_face_info/",
    data={"face_id":"3000",}
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {
            "id": "3000",
            "name": "Donald_Pettit_0003",
            "encoding": "-0.176704540848732,0.053831811994314194,0.08885607123374939,-0.047113969922065735,-0.09783285856246948,-0.035520412027835846,0.012959372252225876,-0.023627251386642456,0.12838546931743622,-0.038373325020074844,0.20606544613838196,0.031055763363838196,-0.186794251203537,0.04706375300884247,-0.09658420830965042,0.1139010637998581,-0.09659379720687866,-0.0821417048573494,-0.15059185028076172,-0.13723453879356384,-0.06690609455108643,0.06002058833837509,-0.03112674504518509,0.01374952495098114,-0.05183251202106476,-0.25697654485702515,-0.008803650736808777,-0.11816735565662384,0.1914733648300171,-0.12547245621681213,0.01981443166732788,-0.021318458020687103,-0.1388530284166336,-0.06536072492599487,0.049012474715709686,0.09115281701087952,-0.055215924978256226,-0.05855705589056015,0.30114829540252686,0.02892202138900757,-0.1345197856426239,0.030301585793495178,0.08369851857423782,0.3479548990726471,0.16013272106647491,0.04456277936697006,0.03343307971954346,-0.08972384035587311,0.13125866651535034,-0.2737799882888794,0.08369727432727814,0.11435038596391678,0.13882067799568176,0.06669143587350845,0.07657592743635178,-0.2290130853652954,0.07159662246704102,0.08038052916526794,-0.27316007018089294,0.11852667480707169,0.08522792905569077,0.012969285249710083,-0.1141052395105362,0.008820019662380219,0.17587099969387054,0.1002768725156784,-0.10266479104757309,-0.13504737615585327,0.16890497505664825,-0.21129463613033295,0.05278594791889191,0.08971411734819412,-0.06309861689805984,-0.15042375028133392,-0.17480944097042084,0.07861451804637909,0.3459405303001404,0.17128823697566986,-0.10503749549388885,0.04966156929731369,-0.012393936514854431,-0.06834661960601807,0.0592464879155159,0.03947332501411438,-0.16157279908657074,-0.019784554839134216,-0.0028732512146234512,0.06917767226696014,0.1109330803155899,0.04746047407388687,0.026542101055383682,0.1576872169971466,0.05140251666307449,-0.066971056163311,0.004764465615153313,0.0787072628736496,-0.14523200690746307,-0.0009096786379814148,-0.07982958108186722,-0.01868884265422821,0.13773617148399353,-0.09119930118322372,0.12815773487091064,0.07290337979793549,-0.26726776361465454,0.1818818300962448,-0.07377679646015167,-0.036980271339416504,0.04628632962703705,-0.014474421739578247,-0.02955978736281395,0.02177460491657257,0.21928220987319946,-0.20665590465068817,0.23938027024269104,0.21889780461788177,-0.0180859062820673,0.09559426456689835,0.10093402862548828,-0.006656095385551453,0.07255208492279053,0.04880409687757492,-0.15827050805091858,-0.06751323491334915,-0.06123246252536774,-0.13375836610794067,0.0458560436964035,0.04306744039058685"
        }
    }


# get face info with invalid id
def test_get_face_info_invalid():
    response = client.post("http://127.0.0.1:8000/get_face_info/",
    data={"face_id":"14000",}
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "200",
        "body": {}
    }
    
