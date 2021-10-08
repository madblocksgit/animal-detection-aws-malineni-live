import boto3

list_animals=['Tiger','Elephant','Bird']

service='rekognition'
region_name='eu-west-1'
aws_access_key=''
aws_secret=''

client=boto3.client(service,region_name=region_name,
	aws_access_key_id=aws_access_key,
	aws_secret_access_key=aws_secret)
print('Client Connected')

image=open('table.jpg','rb')
imageBuffer={'Bytes':image.read()}

response=client.detect_labels(Image=imageBuffer)
response=dict(response)
response=response['Labels']
response=response[0]
response=response['Name']
print(response)

if response in list_animals:
	print('Target Animal Found!! Raise Alarm!')
	print('Send Notification to Owner')
