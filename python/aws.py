import boto3


ec2 = boto3.resource('ec2')

instances = ec2.create_instances(

    ImageId='ami-02a49d5edf356e898',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='NewKeyPair'
)