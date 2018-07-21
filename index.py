import boto3

# region="sa-east-1"
s3 = boto3.resource('s3')
client = boto3.client('rekognition')

def lista_imagens():
    imagens = []
    bucket = s3.Bucket('fa-images-test-2')
    for imagem in bucket.objects.all():
        imagens.append(imagem.key)
    return imagens

def index_imagens(imagens):
    for i in imagens:
        print(i)
        response = client.index_faces(
            CollectionId='faces',
            DetectionAttributes=[
            ],
            Image={
                'S3Object': {
                    'Bucket': "fa-images-test-2",
                    'Name': i,
                }
            },
            ExternalImageId=i[:-4],
        )

imagens = lista_imagens()
index_imagens(imagens)

# aws rekognition create-collection --collection-id nome-da-colecao