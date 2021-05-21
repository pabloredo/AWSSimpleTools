# HammerDB Instance

Deploy HammerDB on AWS EC2 Linux and a Test Database. This is for reference only. 
Consider removing database secrets from templates.

This repo also contains a template to deploy dms to perform cdc from RDS to S3. 

For reference on the HammerDB TPC test see https://www.hammerdb.com/docs/ch03s05.html

### 1. Deploy HammerDB template with AWS CLI
```
    aws cloudformation create-stack \
    --stack-name hammerdb \
    --template-body file://hammerdb_cloudformation_template.yaml \
    --capabilities CAPABILITY_IAM
````

### 2. Running hammerdb and initialize the tpcc schema

1. CD into HammerDB home directory
2. Run ``./hammerdbcli``
3. Run ``librarycheck``
4. Run ``dbset db pg``
5. Run ``buildschema``. Wait 2 - 5 min until you see message "ALL VIRTUAL USERS COMPLETE"
6. Exit the hammerdb cli by typing  ``exit``

### 3. Validate schema is there
```
psql -h <db_endpoint> -U awsuser HammerDBTestDB
```
Sample update command to test cdc
```
UPDATE district 
SET d_state='Ud' 
WHERE d_state='Ut';
```

### 4. Run the load test, monitor tps.

1. From the HammerDB home directory run ```./hammerdbcli auto ../pgrun.tcl```
2. Monitor tps from the cli.

