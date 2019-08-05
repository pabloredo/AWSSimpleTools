# ############################################################################
#
# Built this quick script to keep my sandbox account buckets clean, during
# experimentation and testing tend to create too many buckets and data that
# is not really required and costs money.
#
# The script takes a list of buckets to keep (whitelist) and removes any other
# buckets. Use with caution, you might loose important data. Thus I only use
# with my sandbox account.
#
# Version
# 1.0 - 2019-07-05 - First Version
#
# ############################################################################

import boto3
import json

whitelist = [
    'aws-glue-scripts-166588134205-us-east-1',
    'aws-glue-temporary-166588134205-us-east-1',
    'cloudtrail-awslogs-166588134205-6xoc2a1m-isengard-do-not-delete',
    'do-not-delete-gatedgarden-audit-166588134205'
    'myinstantreplay-backup'
    'pablo-ad-quickstart',
    'pablo.billing.cur',
    'pablo.cloudformation.templates',
    'pablo.cloudtrail.logs',
    'pablo.config.bucket',
    'pablo.corporate.datalake',
    'pablo.data.samples',
    'pablo.network.logs',
    'pablo.pipeline.ecscluster-repo',
    'pablo.sagemaker.data',
    'pablo.shared.public',
    'pablo.textract.input',
    'pablo.transfer.sftp'
]
# Use 'Run' to delete, any other value will run a simulation.
mode = 'Dev'

def main():
    print('STARTING PROCESS...')
    delete_buckets(whitelist)
    print('PROCESS COMPLETED')

def delete_buckets(buckets_to_ignore):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        if should_i_delete_bucket(bucket['Name'],buckets_to_ignore):
            print (bucket['Name'] + " DELETING...")
            if mode == 'Run':
                delete_bucket(bucket['Name'])
        else:
            print(bucket['Name'] + " KEEPING")

def should_i_delete_bucket(bucket_name, buckets_to_ignore):
    for ignore_bucket in buckets_to_ignore:
        if ignore_bucket == bucket_name:
            return False
    return True

def delete_bucket(bucket_name):
    try:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        print('DELETED')
    except Exception as e:
        print('ERROR: ' + str(e))

if __name__ == '__main__':
    main()
