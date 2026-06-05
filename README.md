# AWS Lambda and Boto3 Automation Assignments

## Overview

This repository contains AWS automation assignments implemented using AWS Lambda and Boto3. The objective is to automate common AWS operational tasks including EC2 instance management, S3 bucket maintenance, security monitoring, and EBS snapshot management.

## Technologies Used

* AWS Lambda
* Python 3.x
* Boto3
* Amazon EC2
* Amazon S3
* Amazon EBS
* AWS IAM
* Amazon CloudWatch
* AWS EventBridge

---

## Assignments Completed

### 1. Automated EC2 Instance Management

Automated the starting and stopping of EC2 instances based on resource tags.

Features:

* Detect instances tagged with `Action=Auto-Stop`
* Stop matching instances
* Detect instances tagged with `Action=Auto-Start`
* Start matching instances
* Generate execution logs in CloudWatch

---

### 2. Automated S3 Bucket Cleanup

Automated deletion of files older than the configured retention period.

Features:

* List S3 objects
* Check object age
* Delete outdated objects
* Log cleanup operations

---

### 3. Monitor S3 Bucket Encryption Status

Implemented a Lambda function to monitor S3 bucket encryption settings.

Features:

* Scan all S3 buckets
* Check server-side encryption status
* Report encryption configuration through CloudWatch logs

**Note:** AWS automatically encrypts all new object uploads to Amazon S3 using SSE-S3 by default. This assignment demonstrates how bucket encryption settings can be monitored and validated programmatically.

---

### 4. Automatic EBS Snapshot and Cleanup

Automated EBS snapshot creation and lifecycle management.

Features:

* Create snapshots for specified EBS volumes
* Store snapshot details
* Remove outdated snapshots
* Log snapshot operations

---

## Repository Structure

```text
Assignment-1-EC2-AutoStartStop/
Assignment-2-S3-Cleanup/
Assignment-3-S3-Encryption-Monitor/
Assignment-4-EBS-Snapshot-Cleanup/
Documentation/
README.md
```

---

## Documentation

Detailed implementation steps, screenshots, architecture diagrams, Lambda source code, and testing results are provided in the attached project documentation.

---

## GitHub Repository

https://github.com/sahbu90/aws-cloud-automation-with-lambda-boto3

---

## Note

Modern Amazon S3 automatically encrypts newly uploaded objects by default. This implementation demonstrates how AWS Lambda and Boto3 can be used to programmatically monitor and validate S3 encryption settings.


## Author

Mohd Shahban
