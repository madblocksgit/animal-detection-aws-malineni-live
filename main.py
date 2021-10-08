import boto3
import pygame,time

f=open('animals.txt','r')
list_animals=f.readlines()
print(list_animals)
f.close()

service='rekognition'
region_name='eu-west-1'
aws_access_key=''
aws_secret=''

msg_client=boto3.client('sns',region_name='us-east-1',
	aws_access_key_id=aws_access_key,
	aws_secret_access_key=aws_secret)

client=boto3.client(service,region_name=region_name,
	aws_access_key_id=aws_access_key,
	aws_secret_access_key=aws_secret)
print('Client Connected')

image=open('tiger.jpg','rb')
imageBuffer={'Bytes':image.read()}

response=client.detect_labels(Image=imageBuffer)
response=dict(response)
response=response['Labels']
response=response[0]
response=response['Name'] + '\n'
print(response)

if response in list_animals:
	print('Target Animal Found!! Raise Alarm!')
	print('Send Notification to Owner')
	#playsound.playsound('gun.mp3')
	pygame.mixer.init()
	pygame.mixer.music.load("gun.mp3")
	pygame.mixer.music.set_volume(0.7)
	pygame.mixer.music.play()
	time.sleep(2)
	pygame.mixer.music.stop()
	time.sleep(1)
	pygame.quit()
	msg_client.publish(TopicArn='arn:aws:sns:us-east-1:496667932506:animal-detection',
		Message='Animal Detected in the field',Subject='Animal Notification')
