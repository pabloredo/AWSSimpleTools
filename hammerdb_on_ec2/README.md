
## Deploy template with AWS CLI

`
    aws cloudformation create-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml
`