import boto3

client = boto3.client('redshift')
response = client.resume_cluster(
    ClusterIdentifier='redshift-cluster-1'
)
