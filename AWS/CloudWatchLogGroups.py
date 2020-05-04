import boto3

client = boto3.client('logs')
cloudwatch = boto3.client('cloudwatch')

response = client.describe_log_groups(logGroupNamePrefix='/aws/lambda', limit=1)
nextToken = response.get('nextToken', None)


def processLogGroups(logGroupResponse):
    logGrpNames = []
    for p in logGroupResponse["logGroups"]:
        # print(p['logGroupName'])
        #    if '/aws/lambda/Cal' in str(p['logGroupName']):
        logGrpNames.append(p['logGroupName'])
    print(logGrpNames)

    for eachLogGrpName in logGrpNames:
        metricName = eachLogGrpName + 'Test'
        client.put_metric_filter(
            logGroupName=eachLogGrpName,
            filterName='FilStart',
            filterPattern='START',
            metricTransformations=[
                {
                    'metricName': metricName,
                    'metricNamespace': 'MatchStart',
                    'metricValue': '1',
                    'defaultValue': 0
                },
            ]
        )

        cloudwatch.put_metric_alarm(
            AlarmName=eachLogGrpName + '-alarm',
            ComparisonOperator='GreaterThanThreshold',
            EvaluationPeriods=1,
            MetricName=metricName,
            Namespace='MatchStart',
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


while True:
    if nextToken:
        print(response)
        processLogGroups(response)
        print("has more tokens: " + nextToken)
        response = client.describe_log_groups(logGroupNamePrefix='/aws/lambda', nextToken=nextToken, limit=1)
        nextToken = response.get('nextToken', None)

    else:
        print(response)
        processLogGroups(response)
        print("No more tokens.")
        break
