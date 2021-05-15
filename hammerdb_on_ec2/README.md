# HammerDB Instance

Deploy HammerDB on AWS EC2 Linux and a Test Database. This is for reference only. 
Consider removing database secrets from templates.

### Deploy template with AWS CLI
```
    aws cloudformation create-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --capabilities CAPABILITY_IAM
```
### Update template with AWS CLI

```
    aws cloudformation update-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --capabilities CAPABILITY_IAM
```

### Using client on EC2

```
psql -h <db_endpoint> -U awsuser HammerDBTestDB
```

### Running hammerdb and initialize the tpcc schema
1. Set host and users under config/postgres.xml
2. CD into HammerDB home directory
3. Run './hammerdbcli'
3. Run: 
    'librarycheck'
    'dbset db pg'
    'buildschema'
4. 

### Sample update command to test cdc
```
UPDATE district 
SET d_state='Ud' 
WHERE d_state='Ut';
```