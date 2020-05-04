import boto3

import importlib

# moduleName = input('Enter module name:')
# from AWS import Ec2InstanceList
from AWS.Ec2InstanceList import getinstanceid

# importlib.import_module(Ec2InstanceList)

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch')

# Create alarm with actions enabled
cloudwatch.put_metric_alarm(
    AlarmName='Web_Server_CPU_Utilization_3',
    ComparisonOperator='GreaterThanThreshold',
    EvaluationPeriods=1,
    MetricName='CalFunMetric',
    Namespace='CustomMetric',
    Period=300,
    Statistic='Sum',
    Threshold=1,
    ActionsEnabled=True,
    AlarmActions=[
      'arn:aws:sns:us-east-2:464420198474:Default_CloudWatch_Alarms_Topic'
    ],
    AlarmDescription='Alarm when server CPU exceeds 70%',
    # Dimensions=[
    #     {
    #       'Name': 'InstanceId',
    #       'Value': getinstanceid()
    #     },
    # ],
    Unit='Seconds'
)

# print(getinstanceid())


# aws cloudwatch put-metric-data --metric-name Buffers --namespace MyNameSpace --unit
# Bytes --value 231434333 --dimensions InstanceId=1-23456789,InstanceType=m1.small
