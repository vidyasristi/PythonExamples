import boto3
import sys
from botocore.exceptions import ClientError as botoErr


def ResumeSchedule(action, clusterName, scheduleName, iamRoleArn, cronEntry):
    client = boto3.client('redshift')
    if not clusterName or not scheduleName or not iamRoleArn or not cronEntry:
        sys.exit(2)
    if str(action).lower() == 'create':
        try:
            client.describe_clusters(ClusterIdentifier=clusterName)
            client.create_scheduled_action(
                ScheduledActionName=scheduleName,
                TargetAction={
                    'ResumeCluster': {
                        'ClusterIdentifier': clusterName
                    }},
                Schedule=cronEntry,
                IamRole=iamRoleArn,
                Enable=True
            )
        except botoErr as error:
            print('my error ' + error.response['Error']['Message'])
    elif str(action).lower() == 'delete':
        DeleteSchedule(scheduleName)
    else:
        print('Invalid Action')


def ResizeSchedule(action, clusterName, scheduleName, iamRoleArn, cronEntry, nodeType, isClassicresize, resizeToNodes):
    client = boto3.client('redshift')
    if not clusterName or not scheduleName or not iamRoleArn or not cronEntry:
        sys.exit(2)
    if str(action).lower() == 'create':
        try:
            client.describe_clusters(ClusterIdentifier=clusterName)
            client.create_scheduled_action(
                ScheduledActionName=scheduleName,
                TargetAction={
                    'ResizeCluster': {
                        'ClusterIdentifier': clusterName,
                        'NodeType': nodeType,
                        'NumberOfNodes': resizeToNodes,
                        'Classic': isClassicresize
                    }},
                Schedule=cronEntry,
                IamRole=iamRoleArn,
                Enable=True
            )
        except botoErr as error:
            print('my error ' + error.response['Error']['Message'])
    elif str(action).lower() == 'delete':
        DeleteSchedule(scheduleName)
    else:
        print('Invalid Action')


def DeleteSchedule(scheduleName):
    client = boto3.client('redshift')
    try:
        client.delete_scheduled_action(
            ScheduledActionName=scheduleName, )
    except botoErr as error:
        print('my error ' + error.response['Error']['Message'])

# cronEntry = 'cron(00 12 ? * MON-FRI *)'
# iamRoleArn = 'arn:aws:iam::464420198474:role/redshift_scheduler'
# scheduleName='RedshiftPause'
# clustername='redshift-cluster-1'

#(action, clusterName, scheduleName, iamRoleArn, cronEntry, nodeType, isClassicresize, resizeToNodes):

ResizeSchedule('create', 'redshift-cluster-1', 'RedshiftResizedown', 'arn:aws:iam::464420198474:role/redshift_scheduler',
               'cron(00 12 ? * MON-FRI *)',
               'dc2.large',bool('a'),1)
# ResumeSchedule('create', 'redshift-cluster-1', 'RedshiftResume3', 'arn:aws:iam::464420198474:role/redshift_scheduler',
# 'cron(TUE-FRI *)')

# DeleteSchedule('Vidya')
