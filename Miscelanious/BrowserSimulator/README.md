# simulate_browsing.py
Simple python script that runs get request against a cloudfront domain and an s3 bucket. 
Being using it to perform validation of s3 access logs and cloudfront metrics. Need to create
config.json file with the following parameters:

 {
   "cloudfront_domain": "<your cloudfront domain>",
   "s3_bucket": "<your bucket>",
   "images": ["image1.jpg","image2.jpg"],
   "request_count": 100,
   "distribution": 0.2
 }
