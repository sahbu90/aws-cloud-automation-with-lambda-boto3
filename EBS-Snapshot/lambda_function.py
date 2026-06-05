import boto3

ec2 = boto3.client('ec2')

VOLUME_IDS = [
    'vol-07d03801549e5d325',
    'vol-0766dc7bf5c7cd2bf'
]

def lambda_handler(event, context):

    created_snapshots = []

    for volume_id in VOLUME_IDS:

        snapshot = ec2.create_snapshot(
            VolumeId=volume_id,
            Description=f'Snapshot for {volume_id}'
        )

        created_snapshots.append(
            snapshot['SnapshotId']
        )

        print(
            f"Created snapshot {snapshot['SnapshotId']} for {volume_id}"
        )

    return {
        'statusCode': 200,
        'created_snapshots': created_snapshots
    }