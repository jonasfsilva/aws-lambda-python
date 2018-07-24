import boto3

# region="sa-east-1"
s3 = boto3.resource('s3')
client = boto3.client('rekognition')
import json


def detect_faces():
    faces_detects = client.index_faces(
        CollectionId='faces',
        DetectionAttributes=["DEFAULT"],
        ExternalImageId="TEMPORARIA",
        Image={
            'S3Object': {
                'Bucket': "fa-images-test-2",
                'Name': "_analise.jpg",
            }
        },
    )
    return faces_detects

def creating_faceid_faces_detects(faces_detects):
    faces_ids_detects = []
    for i in range(len(faces_detects['FaceRecords'])):
        faces_ids_detects.append(faces_detects['FaceRecords'][i]['Face']['FaceId'])
    return faces_ids_detects

faces_detects = detect_faces()
faces_ids_detects = creating_faceid_faces_detects(faces_detects)
print(faces_ids_detects)