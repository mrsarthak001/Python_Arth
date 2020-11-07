import os
import getpass

print("\t\t\t Hello from Sarthak Jain")
print("\t\t\t'''''''''''''''''''''''''")

#Authentication

password = getpass.getpass('Enter Password')

if password == "1234":
   print("you are sucessfully login")  
else:
   print("Wrong Password")  

#Aws CLI

def AWS():
	print("WELCOME TO AWS CLOUD")
	print("Configure AWS")
	os.system('aws configure') 
	while True:
		print("\n \n")
		print("""
		Press 1: creating_a_key_pair
		Press 2: ec2
		Press 3: ebs
		Press 4: security_group
		Press 5: s3bucket
		Press 6: creating_cloudfront
		Press 7: to exit
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			key_pair()
		elif i==2:
			ec2()
		elif i==3:
			ebs()
		elif i==4:
			sg()
		elif i==5:
			s3()
		elif i==6:
			cloudfront()
		elif i==7:
			exit()
		else:
			menu()

#Making Key Pair 

def key_pair():
	key = input('Enter key name you want to create')
	os.system('aws ec2 create-key-pair --key-name {}'.format(key))

#EC2

def ec2():
	while True:
		print("\n \n")
		print("""
		Press 1: Describe_ec2
		Press 2: launching_ec2
		Press 3: stopping_ec2
		Press 4: starting_ec2
		Press 5: terminating ec2
		Press 6:return to menu
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Describe_ec2()
		elif i==2:
			launching_ec2()
		elif i==3:
			stopping_ec2()
		elif i==4:
			starting_ec2()
		elif i==5:
			terminate_ec2()
		elif i==10:
			menu()
		else:
			AWS()


def launching_ec2():
	a = input('Enter AMI_ID: ')
	i = input('Enter instance-type: ')
	c = int(input('Enter number of instance you want to launch: '))
	s = input('Enter subnet-ID: ')
	sg = input('Enter security-group: ')
	k = input('Enter key name: ')
	os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(a,i,c,s,sg,k))

def Describe_ec2():
	os.system('aws ec2 describe-instances')

def starting_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 start-instances --instance-ids {}'.format(a))

def stopping_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 stop-instances --instance-ids {}'.format(a))

def terminate_ec2():
	a = input('Enter ami-id: ')
	os.system('aws ec2 terminate-instances --instance-ids {}'.format(a))

#EBS

def ebs():
	while True:
		print("\n \n")
		print("""
		Press 1: creating_ebs_storage
		Press 2: describe_ebs
		Press 3: attaching_ebs
		Press 4: detaching_ebs
		Press 5: deleting_ebs
		Press 6: return to menu
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Creating_ebs()
		elif i==2:
			Describe_ebs()
		elif i==3:
			Attaching_ebs()
		elif i==4:
			Detaching_ebs()
		elif i==5:
			Deleting_ebs()
		elif i==6:
			menu()
		else:
			AWS()  

def Describe_ebs():
	os.system('aws ec2 describe-volumes')

def Attaching_ebs():
	a = input('Enter instance-id: ')
	v = input('Enter volume-id: ')
	d = input('Enter device-name: ')
	os.system('aws ec2 attach-volume --instance-id {} --volume-id {} --device {}'.format(a,v,d))

def Creating_ebs():
	t = input('Enter volume type eg. gp2: ')
	s = input('Enter volume-size: ')
	a = input('Enter availability-zone eg.ap-south-1a: ')
	os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(t,s,a))

def Detaching_ebs():
	v = input('Enter volume-id: ')
	os.system('aws ec2 detach-volume --volume-id {}'.format(v))

def Deleting_ebs():
	v = input('Enter volume-id: ')
	os.system('aws ec2 delete-volume --volume-id {}'.format(v))

def Security_group():
	n = input('Enter security_group_name: ')
	d = input('Add description: ')
	v = input('Enter vcp_id: ')
	os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(n,d,v))

#Security Group

def sg():
	while True:
		print("\n \n")
		print("""
		Press 1: creating_sg
		Press 2: describe_sg
		Press 3: adding_ingress_to_security_group
		Press 4: updating_egress_to_security_group
		Press 5: deleting_sg
		Press 6: return to menu
		Press 7: exit
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Security_group()
		elif i==2:
			Describe_sg()
		elif i==3:
			Ingress()
		elif i==4:
			Egress()
		elif i==5:
			Deleting_sg()
		elif i==6:
			menu()
		elif i==7:
			exit()
		else:
			exit()

def Security_group():
	n = input('Enter security_group_name: ')
	d = input('Add description: ')
	v = input('Enter vcp_id: ')
	os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(n,d,v))

def Describe_sg():
	i = input('Enter security_group_id: ')
	os.system('aws ec2 describe-security-groups --group-ids {}'.format(i))

def Ingress():
	i = input('Enter security-group id: ')
	n = input('Enter security-group name: ')
	e = input('Enter protocol: ')
	p = int(input('Enter port number: '))
	c = input('Enter cidr-block: ')
	os.system('aws ec2 authorize-security-group-ingress --group-id {} --group-name {} --protocol {} --port {} --cidr {}'.format(i,n,e,p,c))

def Egress():
	i = input('Enter security-group id: ')
	e = input('Enter protocol: ')
	p = int(input('Enter port number: '))
	c = input('Enter cidr-block: ')
	os.system('aws ec2 authorize-security-group-egress --group-id {}  --protocol {} --port {} --cidr {}'.format(i,e,p,c))

def Deleting_sg():
	n = input('Enter security_group_id: ')
	os.system('aws ec2 delete-security-group --group-id {}'.format(n))



#S3

def s3():
	while True:
		print("\n \n")
		print("""
		Press 1: creating_s3_bucket
		Press 2: updating_content_to_s3
		Press 3: updating_put_acl_policy
		Press 4: delete_bucket
		Press 5: delete_object_from_bucket
		Press 6:return to menu
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			s3bucket()
		elif i==2:
			s3content()
		elif i==3:
			s3put()
		elif i==4:
			s3delete()
		elif i==5:
			s3deleteo()
		elif i==6:
			menu()
		else:
			menu()

def s3bucket():
	n = input('Enter a unique bucket name: ')
	r = input('Enter region: ')
	os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(n,r,r))

def s3delete():
	n = input('Enter bucket name: ')
	r = input('Enter region: ')
	os.system('aws s3api delete-bucket --bucket {} --region {}'.format(n,r))

def s3content():
	l = input('Enter local location: ')
	n = input('Enter bucket name: ')
	os.system('aws s3 sync "{}" s3://{}'.format(l,n))
def s3put():
	n = input('Enter bucket-name: ')
	k = input('Enter key or pic: ')
	os.system('aws s3api put-object-acl --bucket {} --key {} --acl public-read'.format(n,k))

def s3deleteo():
	n = input('Enter bucket-name: ')
	k = input('Enter key or pic: ')
	os.system('aws s3api delete-object --bucket {} --key {}'.format(n,k))

#cloudfront

def cloudfront():
	n = input('Enter bucket name: ')
	os.system('aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com'.format(n))


#Menu
def menu():
	while True:
		print("\n \n")
		print("""
		Press 1: Docker
		Press 2: AWS
		Press 3: Hadoop
		Press 4: exit
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Docker()
		elif i==2:
			AWS()
		elif i==3:
			Hadoop()
		elif i==4:
			exit()
		else:
			exit()

			
def list_images():
	os.system("docker images")
	
def list_con():
	os.system("docker ps")

def list_all_con():
	os.system("docker ps -a")
	
def con_launch():
	print("/n /n")
	a = input("Enter name of container : ")
	b = input("Enter image to be used : ")
	os.system("docker run -it --name {}  {}".format(a,b))
	
def search_img():
	a = input("Enter the image to be searched on docker hub: ")
	os.system("docker search {}".format(a))

def pull_img():
	a = input("Enter the name of image to be pulled from docker hub: ")
	os.system("docker pull {}".format(a))
	
def on_the_fly_con_run():
	a = input("Enter the image to be used: ")
	b = input("Enter the command to be run: ")
	os.system("docker run -i {} {}".format(a,b))

def con_stop():
	a = input("Name/Id of the container to be stopped: ")
	os.system("docker stop {}".format(a))
	
def con_start():
	a = input("Name/Id of the container to be started: ")
	os.system("docker start {}".format(a))
	
def get_console():
	a = input("Id of the running container: ")
	os.system("docker attach {}".format(a))

def del_con():
	a = input("Name/Id of of the container")
	os.system("docker rm {}".format(a))

def del_image():
	a = input("Image to be deleted")
	os.system("docker rmi {}".format(a))

def get_logs():
	a = input("Name of the container: ")
	os.system("docker logs {}".format(a))

def cp_base_con():
	a = input("Path of the file to be copied: ")
	b = input("Name of the container: ")
	c = input("Final destination path: ")
	os.system("docker cp {} {}:{}".format(a,b,c))
	
def cp_con_base():
	a = input("Name of the container: ")
	b = input("Initial path of the file in the container: ")
	c = input("Destination path: ")
	os.system("docker cp {}:{} {}".format(a,b,c))
	
def install():
	os.system("yum install docker-ce --nobest")

def start():
	os.system("systemctl start docker")
	
def docker():
	while True:
		print("\n \n")
		print("""
			Enter 100: To install docker container engine
			Enter 101: To start the docker services
			Press 1: List the images
			Press 2: List the running containers
			Press 3: List all the containers
			Press 4: Launch new container
			Press 5: Search new image
			Press 6: Pull new image
			Press 7: To launch a contanier run a command and then shutdown
			Press 8: Stop a running container
			Press 9: Start a stopped/exited container
			Press 10: Get the console of a running container
			Press 11: Delete a stopped container
			Press 12: Delete an image
			Press 13: Get the logs
			Press 14: Copy file from base os to container
			Press 15: Copy file from container to base os
			""")
		
		i = int(input("Enter your choice: "))
		if i==1:
			list_images()
		elif i==2:
			list_con()
		elif i==3:
			list_all_con()
		elif i==4:
			con_launch()
		elif i==5:
			search_img()
		elif i==6:
			pull_img()
		elif i==7:
			on_the_fly_con_run()
		elif i==8:
			con_stop()
		elif i==9:
			con_start()
		elif i==10:
			get_console()
		elif i==11:
			del_con()
		elif i==12:
			del_image()
		elif i==13:
			get_logs()
		elif i==14:
			cp_base_con()
		elif i==15:
			cp_con_base()
		elif i==100:
			install()
		elif i==101:
			start()

def clus_check():
	os.system("hadoop fs -ls /")
	
def clus_upload():
	a = input("Path of file to be uploaded: ")
	os.system("hadoop fs -put {} /".format(a))

def file_read():
	a = input("Path of file on filesystem to read: ")
	os.system("hadoop fs -cat {}".format(a))

def file_remove():
	a = input("Path of file on filesystem to remove: ")
	os.system("hadoop fs -rm {}".format(a))
	
def dir_create():
	a = input("Name of directory: ")
	os.system("hadoop fs -mkdir /{}".format(a))

def clus_upload_dir():
	a = input("Path of file to be uploaded: ")
	b = input("Name of directory where the file has to be uploaded: ")
	os.system("hadoop fs -put {} /{}".format(a,b))
	
def file_create():
	a = input("Name of file to be created: ")
	b = input("Destination path on the filesystem: ")
	os.system("hadoop fs -touchz {}  {}".format(a,b))
			
def Hadoop():
	while True:
		print("welcome to client console of hadoop")
		print("""
			Press 1: Check the cluster filesystem
			Press 2: Upload any file to filesystem
			Press 3: Read any file from the filesystem
			Press 4: Remove any file from the filesystem
			Press 5: Create a directory in the filesystem
			Press 6: Upload any file to any specific directory
			Press 7: Create an empty file on the filesystem
			""")
		i = int(input("Enter your choice: "))
		if i==1:
			clus_check()
		elif i==2:
			clus_upload()
		elif i==3:
			file_read()
		elif i==4:
			file_remove()
		elif i==5:
			dir_create()
		elif i==6:
			clus_upload_dir()
		elif i==7:
			file_create()


while True:
		print("\n \n")
		print("""
		Press 1: Docker
		Press 2: AWS
		Press 3: Hadoop
		Press 4: exit
		""")


		i = int(input("Enter ur choice : "))
		print(i)
		if i==1:
			Docker()
		elif i==2:
			AWS()
		elif i==3:
			Hadoop()
		elif i==4:
			exit()
		else:
			exit()



