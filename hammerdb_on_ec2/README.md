# HammerDB Instance

Deploy HammerDB on AWS EC2 Linux and Test Database. 

## Deploy template with AWS CLI
```
    aws cloudformation create-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --capabilities CAPABILITY_IAM
```
## Update template with AWS CLI

```
    aws cloudformation update-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --capabilities CAPABILITY_IAM
```

