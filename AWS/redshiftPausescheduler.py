import boto3
from datetime import date, datetime


def pauseRedshiftResume(clustername):
    client = boto3.client('redshift')
    client.create_scheduled_action(
        ScheduledActionName='RedshiftResume',
        TargetAction={

            'ResumeCluster': {
                'ClusterIdentifier': clustername
            }},
        Schedule='cron(00 12 ? * MON-FRI *)',
        IamRole='arn:aws:iam::464420198474:role/redshift_scheduler',
        # StartTime=datetime(2020, 5, 8),
        # EndTime=datetime(2020, 5, 9),
        Enable=True
    )

    client = boto3.client('redshift')
    client.create_scheduled_action(
        ScheduledActionName='RedshiftPause',
        TargetAction={

            'PauseCluster': {
                'ClusterIdentifier': clustername
            }},
        Schedule='cron(00 02 ? * TUE-SAT *)',
        IamRole='arn:aws:iam::464420198474:role/redshift_scheduler',
        # StartTime=datetime(2020, 5, 8),
        # EndTime=datetime(2020, 5, 9),
        Enable=True
    )

pauseRedshiftResume('redshift-cluster-1')