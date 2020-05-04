import boto3

ec2 = boto3.resource('ec2')


def getinstanceid():
    instances = ec2.instances.filter(
        Filters=[{
            'Name': 'tag:Name',
            'Values': ['MyInstance']
        }])
    instanceid = ''
    for instance in instances:
        # print(instance.id, instance.instance_type)
        instanceid = instance.id
    # print('printing instance id' + instanceid)
    return instanceid


# print(getinstanceid())
