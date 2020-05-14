import json
import boto3
import zlib
from base64 import b64decode


def lambda_handler(event, context):
    client = boto3.client('cloudwatch')
    decodedEvent = zlib.decompress(b64decode(event['awslogs']['data']), 16 + zlib.MAX_WBITS).decode("utf-8")
    # decodedJson = json.load(decodedEvent)
    # logStreamName = decodedJson['logStream']
    print(decodedEvent)
    filteredAlarms = client.describe_alarms(
        AlarmNamePrefix='Final',
        AlarmTypes=['MetricAlarm'])

    if len(filteredAlarms['MetricAlarms']) == 0:
        filteredMetrics = listMetrics(client, 'CustomMetric', 'TemplateMetric11', 'SFJGJQQE11234X111')
        if filteredMetrics['Metrics'] == 0:
            print("Metric and alarm not found. Creating both.")
            putMetricData(client, 'CustomMetric', 'TemplateMetric11', 'SFJGJQQE11234X111')
            putMetricAlarm(client, 'FinalAlarm', 'TemplateMetric11', 'CustomMetric')
            putMetricData(client, 'CustomMetric', 'TemplateMetric11', 'SFJGJQQE11234X111')
        else:
            print("Alarm not found. Creating!!!")
            putMetricAlarm(client, 'FinalAlarm', 'TemplateMetric11', 'CustomMetric')
            putMetricData(client, 'CustomMetric', 'TemplateMetric11', 'SFJGJQQE11234X111')
    else:
        putMetricData(client, 'CustomMetric', 'TemplateMetric11', 'SFJGJQQE11234X111')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }


def putMetricData(client, metricNamespace, metricName, replicationTaskName):
    return client.put_metric_data(
        Namespace=metricNamespace,
        MetricData=[
            {
                'MetricName': metricName,
                'Dimensions': [
                    {
                        'Name': 'ReplicationTaskName',
                        'Value': replicationTaskName
                    },
                ],
                'StatisticValues': {
                    'SampleCount': 1.0,
                    'Sum': 1.0,
                    'Minimum': 1.0,
                    'Maximum': 1.0
                },
                'Unit': 'Seconds',
                'StorageResolution': 1
            }])


def putMetricAlarm(client, alarmName, metricName, metricNamespace):
    return client.put_metric_alarm(
        AlarmName=alarmName,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        EvaluationPeriods=1,
        MetricName=metricName,
        Namespace=metricNamespace,
        Period=60,
        Statistic='Sum',
        Threshold=1,
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-2:464420198474:Default_CloudWatch_Alarms_Topic'
        ],
        Dimensions=[
            {
                'Name': 'ReplicationTaskName',
                'Value': 'SFJGJQQE11234X111'
            }
        ],
        AlarmDescription='Task alarm')


def listMetrics(client, metricNamespace, metricName, replicationTaskName):
    return client.list_metrics(
        Namespace=metricNamespace,
        MetricName=metricName,
        Dimensions=[
            {
                'Name': 'ReplicationTaskName',
                'Value': replicationTaskName
            }])


if __name__ == '__main__':
    lambda_handler({}, {})
