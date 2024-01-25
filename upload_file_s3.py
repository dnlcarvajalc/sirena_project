import boto3
import constants

def upload_file_s3(file, file_path):
    #Indica que servicio se va a utilizar
    s3 = boto3.resource('s3')

    #Se sube el archivo txt. al servicio S3
    with open('./' + file_path + '/' + file, 'rb') as data:
        s3.Bucket(constants.BUCKET_NAME).put_object(Key=file, Body=data)

    print("Done")

upload_file_s3('prueba.txt', 's3_prueba')