import json
import boto3

region = 'us-east-1'
ec2 = boto3.resource('ec2', region_name=region)

def lambda_handler(event, context):
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']},{'Name': 'tag:ENV','Values':['DEV']}])
    for instance in instances:
        id=instance.id
        ec2.instances.filter(InstanceIds=[id]).stop()
        print("Instance ID is stopped :- "+instance.id)
    return "success"