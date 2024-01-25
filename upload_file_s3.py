import boto3
import constants

#Indica que servicio se va a utilizar
s3 = boto3.resource('s3')

#Se sube el archivo txt. al servicio S3
with open('./s3_prueba/prueba.txt', 'rb') as data:
    s3.Bucket(constants.BUCKET_NAME).put_object(Key='prueba.txt', Body=data)

print("Done")