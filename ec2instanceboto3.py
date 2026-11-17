import boto3
# Step1: Create an EC2 resource object

ec2_resource = boto3.resource('ec2')

# Launch an ec2 instance

instances = ec2_resource.create_instances(
    ImageId='ami-0b71756f4d851f798',
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='ec2testboto',
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 8,
                'DeleteOnTermination': False
            }
        }
    ],
    UserData='''#!/bin/bash
    sudo yum update -y
    sudo yum install apache2 -y
    sudo systemctl start apache2
    sudo systemctl enable apache2
    echo "<h1>Welcome to my EC2 instance - Ravi Medarametla</h1>" > /var/www/html/index.html
    sudo ufw allow 'Apache Full'
    ''',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'FinalProjectInstance'
                },
                {
                    'Key': 'Environment',
                    'Value': 'Preproduction'
                }
            ]
        }
    ]               
)
print("EC2 instance launched successfully!")
