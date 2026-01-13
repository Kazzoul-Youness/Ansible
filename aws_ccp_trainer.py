import random
import time

import streamlit as st


st.set_page_config(page_title="AWS CCP Trainer", layout="centered")

# =============================
# DATA
# =============================

EXAMS = {
    # ==================================================================================================
    #                  Cloud Concepts
    # ==================================================================================================
    "Cloud Concepts": [
        {
            "id": 1,
            "question": "Which AWS service lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources?",
            "choices": ["Amazon VPC", "AWS Elastic Beanstalk", "Internet Gateway", "Amazon EC2"],
            "answer": [0],
        },
        {
            "id": 2,
            "question": "What AWS service provides low-cost storage option for retaining database backups which allows occasional data retrieval in minutes?",
            "choices": ["Amazon EFS", "Amazon S3 Glacier Flexible Retrieval", "Amazon EBS", "Amazon S3"],
            "answer": [1],
        },
        {
            "id": 3,
            "question": "A company is in the process of choosing the most suitable AWS Region to migrate its applications. Which factors should they consider?",
            "choices": [
                "Enhance customer experience by reducing latency to users",
                "Availability Zone security",
                "Support country-specific data sovereignty compliance requirements",
                "Proximity to on-site infrastructure",
                "Potential volume discounts for the specific AWS Region",
            ],
            "answer": [0, 2],
        },
        {
            "id": 4,
            "question": "Which statement below is correct regarding the components of the AWS Global infrastructure?",
            "choices": [
                "An edge location contains multiple AWS Regions",
                "An Availability Zone contains edge locations",
                "An AWS Region contains multiple Availability Zones",
                "An Availability Zone contains multiple AWS Regions",
            ],
            "answer": [2],
        },
        {
            "id": 5,
            "question": "Which of the following is one of the benefits of migrating your systems from an on-premises data center to AWS Cloud?",
            "choices": [
                "Eliminates the need to implement client-side encryption",
                "Completely eliminates administrative overhead",
                "Eliminates IT infrastructure costs",
                "Enables focus on business activities rather than managing infrastructure",
            ],
            "answer": [3],
        },
        {
            "id": 6,
            "question": "What cloud computing model deals with services such as EC2 instances?",
            "choices": ["PaaS", "IaaS", "SaaS", "DaaS"],
            "answer": [1],
        },
        {
            "id": 7,
            "question": "Which of the following is not a standard design principle when designing systems in AWS?",
            "choices": [
                "Design for failure",
                "Disposable resources instead of fixed servers",
                "Servers, not services",
                "Loose coupling",
            ],
            "answer": [2],
        },
        {
            "id": 8,
            "question": "The use of multi-threading in Amazon S3 requests via the Multipart Upload API is an example of which AWS cloud best practice?",
            "choices": [
                "Think parallel",
                "Allow for evolutionary architectures",
                "Implement elasticity",
                "Decouple your components",
            ],
            "answer": [0],
        },
        {
            "id": 9,
            "question": "What is the correct arrangement of the AWS Global infrastructure components according to their geographical coverage area, in descending order?",
            "choices": [
                "Edge Locations, Availability Zones, Regions",
                "Availability Zones, Edge Locations, Regions",
                "Regions, Availability Zones, Edge Locations",
                "Regions, Edge Locations, Availability Zones",
            ],
            "answer": [2],
        },
        {
            "id": 10,
            "question": "Which of the following infrastructure correlates to a VPC's subnet?",
            "choices": ["Availability Zone", "Server", "Edge location", "AWS Region"],
            "answer": [0],
        },
        {
            "id": 11,
            "question": "A startup is developing a mobile app with a database service to store user data. The app is expected to grow rapidly and needs a flexible and scalable database service. Which service should they use?",
            "choices": ["Amazon Redshift", "Amazon DynamoDB", "Amazon S3", "Amazon RDS"],
            "answer": [1],
        },
        {
            "id": 12,
            "question": "Which AWS service is suitable for launching a highly scalable MySQL OLTP database?",
            "choices": ["Amazon Aurora", "Amazon DynamoDB", "Amazon Redshift", "Amazon Timestream"],
            "answer": [0],
        },
        {
            "id": 13,
            "question": "How is expense related when moving from traditional servers to the Cloud?",
            "choices": [
                "Capital expense is traded for operational expense",
                "Variable expense is traded for capital expense",
                "Capital expense is traded for variable expense",
                "Operational expense is traded for variable expense",
            ],
            "answer": [2],
        },
        {
            "id": 14,
            "question": "Which of the following are pillars of the AWS Well-Architected Framework?",
            "choices": ["Agility", "Scalability", "Sustainability", "Performance Efficiency"],
            "answer": [2, 3],
        },
        {
            "id": 15,
            "question": "An e-commerce company is considering migrating its website to the AWS Cloud to improve scalability and reduce costs. Which statements explain the business value of migration to AWS Cloud?",
            "choices": [
                "Applications redesigned before migration require re-architecting and rewriting all enterprise applications",
                "Migrating to AWS Cloud offers advanced analytics and machine learning capabilities",
                "Enterprise applications become automatically available on mobile devices",
                "Migrating to AWS Cloud reduces infrastructure costs by right-sizing and eliminating unused resources",
                "Migrating to AWS Cloud benefits from improving service-level agreements and reducing risk",
            ],
            "answer": [3, 4],
        },
        {
            "id": 16,
            "question": "Which of the following design principles supports growth in users, traffic, or data with no drop in performance?",
            "choices": [
                "Design for failure",
                "Decouple your components",
                "Scalability",
                "Go serverless to reduce compute footprint",
            ],
            "answer": [2],
        },
        {
            "id": 17,
            "question": "Which of the following is a fully managed database in AWS that can be used to store JSON documents?",
            "choices": ["Amazon Redshift", "Amazon Aurora", "Amazon DynamoDB", "Amazon ElastiCache"],
            "answer": [2],
        },
        {
            "id": 18,
            "question": "A company is planning to deploy a high-frequency trading HTTP application with constantly changing financial data and requires low-latency access. Which AWS services should be used?",
            "choices": [
                "Amazon RDS",
                "Amazon S3",
                "Amazon EFS",
                "AWS Snowball Edge",
                "Amazon S3 Glacier Flexible Retrieval",
            ],
            "answer": [0, 2],
        },
        {
            "id": 19,
            "question": "Which of the following is used to enable instances in a public subnet to connect to the public internet?",
            "choices": ["NAT Gateway", "NAT Instance", "API Gateway", "Internet Gateway"],
            "answer": [3],
        },
        {
            "id": 20,
            "question": "Which of the following cloud best practices reinforces the use of Service-Oriented Architecture design principles?",
            "choices": [
                "Decouple your components",
                "Implement elasticity",
                "Design for failure",
                "Think parallel",
            ],
            "answer": [0],
        },
        {
            "id": 21,
            "question": "Which of the following perspectives includes the foundational capabilities of the AWS Cloud Adoption Framework?",
            "choices": ["Security", "Sustainability", "Scalability", "Reliability"],
            "answer": [0],
        },
        {
            "id": 22,
            "question": "A company plans to launch a Microsoft SQL Server database on AWS. The database must be managed by the company DBA and use an existing SQL Server license. Which option is the most cost-effective?",
            "choices": [
                "Launch EC2 and install SQL Server with a new license",
                "Launch Amazon Aurora with SQL Server compatibility",
                "Use Windows Server with SQL Server Standard bundled AMI",
                "Launch Amazon RDS for SQL Server using BYOL",
            ],
            "answer": [3],
        },
        {
            "id": 23,
            "question": "A company reduced time to market after migrating to AWS and deploying services within days. Which AWS Cloud benefit is demonstrated?",
            "choices": ["Agility", "Cost savings", "Deploy globally in minutes", "Elasticity"],
            "answer": [0],
        },
        {
            "id": 24,
            "question": "Which of the following does AWS automatically handle for customers?",
            "choices": [
                "Providing web application firewall protection",
                "Applying updates and patches to EC2 hypervisors",
                "Applying updates and patches to EC2 guest operating systems",
                "Securing AWS data centers from environmental hazards",
            ],
            "answer": [1, 3],
        },
        {
            "id": 25,
            "question": "Which AWS Cloud Adoption Framework perspective ensures cloud initiatives support business outcomes?",
            "choices": [
                "Operations perspective",
                "People perspective",
                "Business perspective",
                "Governance perspective",
            ],
            "answer": [2],
        },
        {
            "id": 26,
            "question": "Which of the following is the responsibility of the customer in the AWS Cloud?",
            "choices": [
                "Disposal of disk drives",
                "Ensuring AWS services comply with required standards",
                "Managing data stored in AWS resources",
                "Managing users in their AWS account",
            ],
            "answer": [2, 3],
        },
        {
            "id": 27,
            "question": "Which AWS applications help improve business communication and customer service?",
            "choices": [
                "Amazon Chime",
                "AWS Transfer Family",
                "AWS Marketplace",
                "Amazon Connect",
                "Amazon WorkSpaces",
            ],
            "answer": [0, 3],
        },
        {
            "id": 28,
            "question": "What does AWS do when a storage device reaches the end of its lifespan?",
            "choices": [
                "Simply wipes the device and disposes it",
                "Archives the device for future use",
                "Returns the device to the manufacturer",
                "Follows a strict decommissioning process as defined in compliance procedures",
            ],
            "answer": [3],
        },
        {
            "id": 29,
            "question": "Which of the following are defined as global services in AWS?",
            "choices": [
                "AWS Identity and Access Management",
                "AWS Batch",
                "Amazon DynamoDB",
                "Amazon CloudFront",
                "Amazon RDS",
            ],
            "answer": [0, 3],
        },
        {
            "id": 30,
            "question": "Which of the following are regarded as regional services in AWS?",
            "choices": ["AWS Batch", "AWS Security Token Service", "Amazon Route 53", "Amazon EC2", "Amazon EFS"],
            "answer": [0, 4],
        },
    ],
    # ==================================================================================================
    #                  Cloud Technology and Services
    # ==================================================================================================
    "Cloud Technology and Services": [
        {
            "id": 1,
            "question": "Which of the following options allows customers to find, buy, and immediately start using the software and services that run on AWS?",
            "choices": [
                "AWS IQ",
                "AWS Partner Network",
                "AWS Marketplace",
                "Reserved Instance Marketplace",
            ],
            "answer": [2],
        },
        {
            "id": 2,
            "question": "A group of software engineers is working on a project that requires a new Microsoft SQL Server database to be hosted in AWS. The team needs to ensure that the database can be set up quickly and efficiently to meet urgent deadlines. Which AWS services should they use?",
            "choices": [
                "Amazon Aurora",
                "Amazon EC2",
                "Amazon Redshift",
                "Amazon Aurora Backtrack",
                "Amazon Relational Database Service (Amazon RDS)",
            ],
            "answer": [1, 4],
        },
        {
            "id": 3,
            "question": "Which of the following are true regarding Amazon Relational Database Service (Amazon RDS)?",
            "choices": [
                "Provides 99.999999999% reliability and durability",
                "Automatically scales up the relational database instance based on incoming workload",
                "Simplifies the management of time-consuming database administration tasks",
                "Makes it easy to set up, operate, and scale a relational database",
                "It is a fully managed nonrelational database service",
            ],
            "answer": [2, 3],
        },
        {
            "id": 4,
            "question": "Which service allows the addition of powerful visual analysis features to applications, enabling the search, verification, and organization of millions of images?",
            "choices": [
                "Amazon OpenSearch Service",
                "Amazon Macie",
                "Amazon Rekognition",
                "Amazon SageMaker AI",
            ],
            "answer": [2],
        },
        {
            "id": 5,
            "question": "A customer has a popular website that has millions of viewers from all over the world and has read-heavy database workloads. Which option is the best to use to increase the read throughput of their database?",
            "choices": [
                "Enable Multi-AZ deployments",
                "Use Amazon S3 to queue up requests",
                "Enable Amazon RDS Standby Replicas",
                "Enable Amazon RDS Read Replicas",
            ],
            "answer": [3],
        },
        {
            "id": 6,
            "question": "You are planning to create point-in-time backups of your Amazon EBS volumes. Which of the following are correct statements?",
            "choices": [
                "Instances will have to be stopped first to start the EBS backup",
                "EBS backups are stored durably in Amazon S3",
                "You can take EBS backups by creating Amazon Machine Images (AMIs)",
                "Backing up the same EBS volume will create a new backup of the whole volume",
                "You can create point-in-time backups through EBS snapshots",
            ],
            "answer": [1, 4],
        },
        {
            "id": 7,
            "question": "A customer in North Virginia, USA, is doing some drone work and collecting environmental data. Which of the following offline data transfer services allows access to terabytes of data storage for use in a space-constrained environment and allows data transfer to AWS?",
            "choices": [
                "AWS Storage Gateway",
                "AWS Snowcone",
                "AWS Direct Connect",
                "AWS Transit Gateway",
            ],
            "answer": [1],
        },
        {
            "id": 8,
            "question": "Due to high demand, an Auto Scaling group of EC2 instances is running behind an Elastic Load Balancer. Which Trusted Advisor categories will help you identify this issue?",
            "choices": ["Cost Optimization", "Service Limits", "Performance", "Fault Tolerance", "Security"],
            "answer": [1, 2],
        },
        {
            "id": 9,
            "question": "Which service offers virtual private cloud traffic monitoring?",
            "choices": ["Amazon CloudFront", "AWS CloudTrail", "Amazon VPC", "Amazon S3"],
            "answer": [2],
        },
        {
            "id": 10,
            "question": "A company wants to migrate their on-premises MySQL database to Amazon RDS. Which AWS service should they use for this task?",
            "choices": [
                "AWS Schema Conversion Tool (AWS SCT)",
                "AWS Database Migration Service (AWS DMS)",
                "AWS Application Migration Service",
                "AWS Glue",
            ],
            "answer": [1],
        },
        {
            "id": 11,
            "question": "Which AWS storage service offers faster disk read and write performance and provides temporary block-level storage for your instance?",
            "choices": [
                "EBS Provisioned IOPS SSD",
                "EBS",
                "Instance Store",
                "EBS Throughput Optimized HDD",
            ],
            "answer": [2],
        },
        {
            "id": 12,
            "question": "A company has a customized EC2 instance running in their latest web application. How can they create an exact copy of this instance in another region?",
            "choices": [
                "Create a local backup with an auto scaling group and link it between two regions",
                "Create a golden AMI of the instance and copy it to the other region",
                "There is no way to do this in AWS, you will have to perform the transfer manually",
                "Create backups of all EBS volumes and copy them to another region",
            ],
            "answer": [1],
        },
        {
            "id": 13,
            "question": "Which service in AWS supports various business intelligence tools such as Apache Spark so that you may perform data transformation workloads (ETL) and analytics?",
            "choices": ["Amazon RDS", "Amazon EMR", "Amazon OpenSearch", "Amazon Redshift"],
            "answer": [1],
        },
        {
            "id": 14,
            "question": "You are planning to deploy a video streaming application with frequently accessed, throughput-intensive workloads on your EC2 instance which requires fast and consistent throughput. Which EBS volume type should you use?",
            "choices": [
                "Cold HDD",
                "General Purpose SSD",
                "Provisioned IOPS SSD",
                "Throughput Optimized HDD",
            ],
            "answer": [3],
        },
        {
            "id": 15,
            "question": "Which AWS service lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define?",
            "choices": ["Virtual Private Gateway", "Amazon WorkSpaces", "Amazon Lightsail", "Amazon VPC"],
            "answer": [3],
        },
        {
            "id": 16,
            "question": "A company has a hybrid cloud architecture where their on-premises data center interacts with cloud resources in AWS. Which services can be used to deploy applications to servers running on-premises?",
            "choices": [
                "AWS Systems Manager",
                "AWS Elastic Beanstalk",
                "AWS CloudFormation",
                "AWS Batch",
                "AWS CodeDeploy",
            ],
            "answer": [0, 4],
        },
        {
            "id": 17,
            "question": "Which of the following is true regarding Elastic Load Balancing?",
            "choices": [
                "It distributes incoming traffic across multiple targets in multiple Availability Zones",
                "It automatically increases or decreases the number of instances as demand changes",
                "It is a virtual server that allows applications to run in AWS Cloud",
                "It translates domain names into numeric IP addresses",
            ],
            "answer": [0],
        },
        {
            "id": 18,
            "question": "A DevOps engineer hosts an e-commerce website in the US East (Northern Virginia) Region. Due to regulatory changes, the company needs to relocate the entire infrastructure to another AWS Region with minimal downtime. Which solution helps achieve this?",
            "choices": [
                "Enable RDS Multi-AZ and move standby instances to the new region",
                "Take EBS snapshots and copy them to the new region",
                "Create a golden AMI and redeploy instances to the new region",
                "Create a CloudFormation template and deploy it in the new region",
            ],
            "answer": [3],
        },
        {
            "id": 19,
            "question": "A company has a fleet of on-premises servers that require centralized, scalable, and durable file storage supporting massive parallel access. Which service is most appropriate?",
            "choices": [
                "Amazon Redshift",
                "Amazon Elastic File System",
                "Amazon Storage Gateway - File Gateway",
                "Amazon S3",
            ],
            "answer": [1],
        },
        {
            "id": 20,
            "question": "Which of the following is not required when launching an EBS-backed EC2 instance?",
            "choices": ["VPC and subnet specification", "EBS Root volume", "Elastic IP address", "Security group"],
            "answer": [2],
        },
        {
            "id": 21,
            "question": "Which AWS service allows you to provision additional storage capacity for your local data center without migrating data?",
            "choices": ["AWS Direct Connect", "AWS Storage Gateway", "AWS Backup", "AWS Snowball Edge"],
            "answer": [1],
        },
        {
            "id": 22,
            "question": "A company is using Amazon S3 to store various types of documents in a single bucket, with different access frequency through S3 Access Points. Data must not be overwritten or deleted. Which feature should be used?",
            "choices": [
                "S3 Versioning",
                "S3 Event Notifications",
                "S3 Lifecycle",
                "S3 Glacier Vault Lock",
            ],
            "answer": [0],
        },
        {
            "id": 23,
            "question": "A customer needs to retrieve instance ID, instance profile, and other information of an EC2 instance for an application running within the instance. Where can this information be found?",
            "choices": ["Resource tags", "Amazon Machine Image", "Instance user data", "Instance metadata"],
            "answer": [3],
        },
        {
            "id": 24,
            "question": "What service allows you to create alarms that notify you when EC2 CPU utilization thresholds are breached?",
            "choices": ["Amazon CloudWatch", "Amazon SNS", "AWS Config", "AWS Auto Scaling"],
            "answer": [0],
        },
        {
            "id": 25,
            "question": "A company has large amounts of data stored in multiple sources such as S3, Redshift, and RDS and needs to extract, transform, and load this data into a data warehouse. Which service is best suited?",
            "choices": ["AWS Glue", "AWS Lambda", "Amazon EC2", "Amazon Athena"],
            "answer": [0],
        },
        {
            "id": 26,
            "question": "Which of the following will you use to create a data warehouse in AWS for your business intelligence needs?",
            "choices": ["Amazon RDS", "Amazon DynamoDB", "Amazon S3", "Amazon Redshift"],
            "answer": [3],
        },
        {
            "id": 27,
            "question": "What type of EBS volume is recommended for most workloads and is also suitable as a boot volume?",
            "choices": ["Cold HDD", "Provisioned IOPS SSD", "General Purpose SSD", "Throughput Optimized HDD"],
            "answer": [2],
        },
        {
            "id": 28,
            "question": "Which options allow you to launch a new Amazon RDS database cluster into your VPC?",
            "choices": [
                "AWS Management Console",
                "AWS Concierge",
                "AWS CloudFormation",
                "AWS Systems Manager",
                "AWS CodePipeline",
            ],
            "answer": [0, 2],
        },
        {
            "id": 29,
            "question": "You have a large number of log files that will be archived in AWS for a long time and should have a retrieval time of 1 to 12 hours. Which service is the most cost-effective storage class?",
            "choices": [
                "Amazon EBS Cold HDD",
                "Amazon S3 Glacier Instant Retrieval",
                "Amazon S3 Standard-IA",
                "Amazon S3 Glacier Deep Archive",
            ],
            "answer": [3],
        },
        {
            "id": 30,
            "question": "Which of the following is a data transport solution that accelerates moving terabytes to petabytes of data in and out of AWS using appliances with on-board storage and compute capabilities?",
            "choices": ["AWS Snowcone", "AWS Snowball Edge", "AWS DataSync", "Lambda@Edge"],
            "answer": [1],
        },
    ],
    # ==================================================================================================
    #                         Security and Compliance
    # ==================================================================================================
    "Security and Compliance": [
        {
            "id": 1,
            "question": "An employee is asking for access to your S3 bucket. What should be the level of access that you should provide them?",
            "choices": [
                "Give him administrator access levels",
                "Ask what type of access he requires and only provide him those permissions",
                "Give him S3 full access",
                "Give him read-only access",
            ],
            "answer": [1],
        },
        {
            "id": 2,
            "question": "Which of the following is typically used to secure Amazon VPC subnets?",
            "choices": ["Network ACL", "AWS IAM", "Security Group", "AWS Config"],
            "answer": [0],
        },
        {
            "id": 3,
            "question": "Which service lets you create rules to filter web traffic based on conditions that include IP addresses, HTTP headers, or custom URIs?",
            "choices": ["Security Group", "AWS WAF", "Network ACL", "AWS Trusted Advisor"],
            "answer": [1],
        },
        {
            "id": 4,
            "question": "As an AWS customer, what offering do you naturally inherit from AWS after you sign up?",
            "choices": [
                "All the responsibilities in enforcing security and compliance policies of your organization",
                "All the best practices of AWS policies, architecture, and operational processes built to satisfy your requirements",
                "All the data you store in and retrieve from AWS",
                "All the hardware and software that you provision in the AWS Cloud",
            ],
            "answer": [0],
        },
        {
            "id": 5,
            "question": "You are permitted to conduct security assessments and penetration testing without prior approval against which AWS resources?",
            "choices": [
                "AWS Security Token Service (STS)",
                "AWS Identity and Access Management (IAM)",
                "Amazon Aurora",
                "Amazon S3",
                "Amazon RDS",
            ],
            "answer": [2, 4],
        },
        {
            "id": 6,
            "question": "Which among the following services can be used to test and troubleshoot IAM and resource-based policies?",
            "choices": [
                "Amazon Inspector",
                "AWS IAM Policy Simulator",
                "AWS Config",
                "AWS Systems Manager",
            ],
            "answer": [1],
        },
        {
            "id": 7,
            "question": "Which of the following security group rules are valid?",
            "choices": [
                "Inbound HTTP rule with security group ID as source",
                "Outbound MySQL rule with IP address as source",
                "Inbound TCP rule with instance ID as source",
                "Outbound HTTPS rule with hostname as destination",
                "Inbound RDP rule with an address range as source",
            ],
            "answer": [0, 4],
        },
        {
            "id": 8,
            "question": "There is an incident where an S3 object was deleted using an account without the owner's knowledge. What can be done to prevent unauthorized deletion of S3 objects?",
            "choices": [
                "Create access control policies that only you can perform S3-related actions",
                "Set up stricter IAM policies that will prevent users from deleting S3 objects",
                "Configure MFA delete on the S3 bucket",
                "Set your S3 buckets to private so that objects are not publicly readable or writable",
            ],
            "answer": [2],
        },
        {
            "id": 9,
            "question": "Which of the following instances is it better to use IAM roles rather than IAM users?",
            "choices": [
                "If you have employees who will constantly need access to your AWS resources",
                "When you have outside entities that need to perform specific actions in your AWS account",
                "When you want to provide AWS services permissions to do certain actions",
                "When you need a GUI to interact with your AWS environment",
                "When you need an administrator to handle the AWS account for you",
            ],
            "answer": [2],
        },
        {
            "id": 10,
            "question": "Which of the following IAM identities is associated with the access keys that are used in managing your cloud resources via the AWS Command Line Interface?",
            "choices": ["IAM User", "IAM Policy", "IAM Group", "IAM Role"],
            "answer": [0],
        },
        {
            "id": 11,
            "question": "Which service in AWS protects resources from common DDoS attacks in a proactive manner?",
            "choices": ["Security groups", "AWS Shield", "Amazon Inspector", "AWS WAF"],
            "answer": [1],
        },
        {
            "id": 12,
            "question": "What service should you use in order to add user sign-up, sign-in, and access control to your mobile app with a feature that supports sign-in with social identity providers such as Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0?",
            "choices": [
                "AWS Single Sign-On (SSO)",
                "Amazon Cognito",
                "AWS Directory Service",
                "AWS Identity and Access Management (IAM)",
            ],
            "answer": [1],
        },
        {
            "id": 13,
            "question": "Which of the following is needed to retrieve a list of Amazon EC2 instances using the AWS CLI?",
            "choices": ["MFA", "EC2 key pairs", "Access keys", "Username and password"],
            "answer": [2],
        },
        {
            "id": 14,
            "question": "What is the best way to keep track of all activities made in your AWS account?",
            "choices": [
                "Use LDAP authentication on your AWS account",
                "Create a multi-region trail in AWS CloudTrail",
                "Use Amazon CloudWatch Logs to log all activities",
                "Set up MFA logging to know who is currently in your environment",
            ],
            "answer": [1],
        },
        {
            "id": 15,
            "question": "An e-commerce company launches several EC2 instances to run their web application. Which of the following services can be used to help ensure security compliance?",
            "choices": [
                "AWS Systems Manager",
                "Amazon MQ",
                "AWS CloudFormation",
                "Amazon Inspector",
                "AWS Trusted Advisor",
            ],
            "answer": [3, 4],
        },
        {
            "id": 16,
            "question": "A customer needs to identify the IAM user who terminated their production EC2 instance in AWS. Which service should they use?",
            "choices": ["Amazon CloudWatch", "AWS CloudTrail", "AWS Systems Manager", "Amazon AppStream 2.0"],
            "answer": [1],
        },
        {
            "id": 17,
            "question": "Which of the following is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads?",
            "choices": ["Amazon GuardDuty", "AWS WAF", "Amazon Macie", "AWS Shield"],
            "answer": [0],
        },
        {
            "id": 18,
            "question": "AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Which option best describes an account alias in IAM?",
            "choices": [
                "Your IAM root username",
                "The name AWS assigns to your account",
                "The numerical value of your account ID",
                "A substitute for an account ID in the web address for your account",
            ],
            "answer": [3],
        },
        {
            "id": 19,
            "question": "Which of the following is part of the best practices in securing your AWS account?",
            "choices": [
                "Grant most privilege",
                "Always manually define permissions for each IAM user",
                "Enable MFA only on the root account",
                "Create an IAM user with admin privileges instead of using root",
            ],
            "answer": [3],
        },
        {
            "id": 20,
            "question": "What is the most secure way to provide applications temporary access to your AWS resources?",
            "choices": [
                "Create an IAM group that has access to the resources and add the application there",
                "Create an IAM policy that allows the application to access the resources and attach the policy to the application",
                "Create an IAM role and have the application assume the role",
                "Create an IAM user with access keys and assign it to the application",
            ],
            "answer": [2],
        },
        {
            "id": 21,
            "question": "Which of the following statements is true of AWS CloudTrail?",
            "choices": [
                "When you create a trail in the AWS Management Console, the trail applies to all AWS Regions by default",
                "CloudTrail is disabled by default for newly created AWS accounts",
                "CloudTrail charges you for every management event trail created",
                "CloudTrail is able to capture application error logs from your Amazon EC2 instances",
            ],
            "answer": [0],
        },
        {
            "id": 22,
            "question": "In compliance with the Sarbanes-Oxley Act (SOX), a US-based company is required to provide SOC 1 and SOC 2 reports of its cloud resources. Where are these AWS compliance documents located?",
            "choices": ["AWS Artifact", "AWS Certificate Manager", "AWS Audit Manager", "AWS GovCloud"],
            "answer": [0],
        },
        {
            "id": 23,
            "question": "Which of the following is a benefit of using AWS Config?",
            "choices": [
                "Facilitates adherence to regulatory requirements and best practices",
                "Facilitates the management of user access to AWS resources",
                "Facilitates real-time monitoring of AWS resources for security threats",
                "Facilitates the monitoring of AWS resource deployments",
            ],
            "answer": [0],
        },
        {
            "id": 24,
            "question": "Which of the following tasks fall under the responsibility of AWS based on the shared responsibility model?",
            "choices": [
                "Implementing IAM policies",
                "Patch management",
                "Applying Amazon S3 bucket policies",
                "Physical and environmental controls",
            ],
            "answer": [3],
        },
        {
            "id": 25,
            "question": "Which of the following should be used to provide temporary AWS credentials for users authenticated via social media logins as well as for guest users without authentication?",
            "choices": [
                "AWS IAM Identity Center",
                "AWS AppSync",
                "Amazon Cognito Identity Pool",
                "Amazon Cognito User Pool",
            ],
            "answer": [2],
        },
        {
            "id": 26,
            "question": "A company is using Amazon S3 to store static media content such as photos and videos. Which of the following should be used to provide specific access to individual S3 objects?",
            "choices": ["Network Access Control List", "Bucket Policy", "SSH keys", "Security Group"],
            "answer": [1],
        },
        {
            "id": 27,
            "question": "In the AWS Shared Responsibility Model, who is responsible for patching the host operating system of an Amazon EC2 instance?",
            "choices": ["Both AWS and the customer", "AWS", "Neither AWS nor the customer", "Customer"],
            "answer": [1],
        },
        {
            "id": 28,
            "question": "A customer has recently experienced an SQL injection attack on their web application's database hosted in EC2. They submitted a complaint ticket to AWS. What should be the response from AWS?",
            "choices": [
                "AWS should secure the infrastructure better to reduce these incidents",
                "AWS should be held fully liable for the damages since the customer properly patched the EC2 instance",
                "AWS should customer should contact a third-party auditor to verify the incident",
                "AWS should reiterate that the customer is responsible for the security of their applications in the Cloud",
            ],
            "answer": [3],
        },
        {
            "id": 29,
            "question": "Which of the following policies grant the necessary permissions required to access Amazon S3 resources?",
            "choices": [
                "Network access control policies",
                "Bucket policies",
                "Object policies",
                "Routing policies",
                "User policies",
            ],
            "answer": [1, 4],
        },
    ],
    # ==================================================================================================
    #        Billing, Pricing and Support
    # ==================================================================================================
    "Billing, Pricing and Support": [
        {
            "id": 1,
            "question": "In Amazon EC2, which pricing construct adjusts its price based on supply and demand of EC2 instances?",
            "choices": [
                "Convertible Reserved Instance",
                "On-Demand Instance",
                "Spot Instance",
                "Standard Reserved Instance",
            ],
            "answer": [2],
        },
        {
            "id": 2,
            "question": "A company is currently using On-Demand EC2 instances for their application and plans to migrate to a Reserved EC2 instance to save on cost. Which option would be the most cost-effective if the application runs more than 3 years?",
            "choices": [
                "No Upfront Convertible Reserved Instance pricing for a 3-year term",
                "All Upfront Convertible Reserved Instance pricing for a 1-year term",
                "All Upfront Standard Reserved Instance pricing for a 3-year term",
                "No Upfront Standard Reserved Instance pricing for a 1-year term that is renewed every year",
            ],
            "answer": [2],
        },
        {
            "id": 3,
            "question": "Which service should a company use to centrally manage account policies and consolidate billing across multiple AWS accounts?",
            "choices": ["AWS Trusted Advisor", "AWS Cost Explorer", "AWS Budgets", "AWS Organizations"],
            "answer": [3],
        },
        {
            "id": 4,
            "question": "Which of the following is the most cost-effective AWS Support Plan to use if you need access to AWS Support API for programmatic case management?",
            "choices": ["Developer", "Basic", "Enterprise", "Business"],
            "answer": [3],
        },
        {
            "id": 5,
            "question": "Which Cost Management tool allows tracking of Amazon EC2 Reserved Instance (RI) usage and provides visibility into the discounted RI rate charged to resources?",
            "choices": [
                "AWS Cost and Usage Report",
                "AWS Budgets",
                "AWS Cost Explorer",
                "AWS Price List Bulk API",
            ],
            "answer": [0],
        },
        {
            "id": 6,
            "question": "A customer is on a Basic support plan and plans to use Infrastructure Event Management, Well-Architected Reviews, and Operations Reviews features in the most cost-effective manner. What should they do?",
            "choices": [
                "None since these features are already included in their Basic support plan",
                "Upgrade to Business support plan",
                "Upgrade to Enterprise support plan",
                "Upgrade to Developer support plan",
            ],
            "answer": [2],
        },
        {
            "id": 7,
            "question": "Which of the following is the most cost-effective payment option when you purchase either a Standard or Convertible Reserved Instance for a 1-year term?",
            "choices": ["No Upfront", "Deferred", "All Upfront", "Partial Upfront"],
            "answer": [2],
        },
        {
            "id": 8,
            "question": "Which of the following are characteristics of Amazon EC2 Convertible Reserved Instances?",
            "choices": [
                "Have the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value",
                "Allows you to make your capacity reservation to a specific instance family within a fraction of a day, weeks, or a month",
                "Allows you to change instance family, operating system, tenancy, and payment option",
                "Allows you to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or lesser value",
                "Provides the most significant discount of the RI types and are best suited for steady-state usage",
            ],
            "answer": [0, 2],
        },
        {
            "id": 9,
            "question": "A company is planning to adopt a hybrid cloud architecture with AWS. Which option can they use to help them estimate their costs?",
            "choices": ["AWS Pricing Calculator", "Consolidated billing", "AWS Cost Explorer", "Cost allocation tags"],
            "answer": [0],
        },
        {
            "id": 10,
            "question": "Which of the following allows you to set coverage targets and receive alerts when your utilization drops below the threshold you define?",
            "choices": ["AWS Budgets", "AWS Trusted Advisor", "Amazon CloudWatch Billing Alarm", "AWS Cost Explorer"],
            "answer": [0],
        },
        {
            "id": 11,
            "question": "Which of the following actions will incur AWS charges?",
            "choices": [
                "Provisioning Elastic IPs and attaching them to running EC2 instances",
                "Transfer of EC2 data between two AWS Regions",
                "Setting up additional VPCs in your account",
                "Using AWS CloudFormation to create resources",
                "Network charges for the transfer of data from your data center to S3 through a VPN",
            ],
            "answer": [1],
        },
        {
            "id": 12,
            "question": "Which pricing and support option offers the most significant discount compared to On-Demand instance pricing to process steady-state workloads that will continuously be running for a year and also provide capacity reservation?",
            "choices": ["Savings Plans", "Standard Reserved Instance", "Convertible Reserved Instance", "Dedicated Instance"],
            "answer": [1],
        },
        {
            "id": 13,
            "question": "What is the lowest support plan that allows an unlimited number of technical support cases to be opened?",
            "choices": ["Developer", "Basic", "Enterprise", "Business"],
            "answer": [0],
        },
        {
            "id": 14,
            "question": "Where can the customer view Reserved Instance usage for the past month?",
            "choices": ["Amazon S3", "Amazon EC2", "AWS Organizations", "AWS Billing Console"],
            "answer": [3],
        },
        {
            "id": 15,
            "question": "Which of the following is a key financial benefit of migrating systems hosted on your on-premises data center to AWS?",
            "choices": [
                "Opportunity to replace variable operational expenses (OPEX) with low upfront capital expenses (CAPEX)",
                "Opportunity to replace variable capital expenses (CAPEX) with low upfront costs",
                "Opportunity to replace upfront capital expenses (CAPEX) with low variable costs",
                "Opportunity to replace upfront operational expenses (OPEX) with low variable operational expenses",
            ],
            "answer": [2],
        },
        {
            "id": 16,
            "question": "A manufacturing company has multiple AWS accounts for various departments and is experiencing an increase in AWS costs. Which option allows them to take advantage of volume discounts in AWS?",
            "choices": [
                "Move all AWS resources into a single global account",
                "Upgrade to an AWS Enterprise support plan",
                "Use AWS Organizations and enable consolidated billing",
                "Opt for an All Upfront Convertible Reserved Instance pricing for a 3-year term",
            ],
            "answer": [2],
        },
        {
            "id": 17,
            "question": "A company plans to launch an Amazon EC2 instance with an attached Amazon Elastic Block Store (Amazon EBS) volume in the default configuration. Billing is incurred only when the EBS storage has the instance in which state?",
            "choices": ["Terminated", "Running", "Stopped", "Pending"],
            "answer": [2],
        },
        {
            "id": 18,
            "question": "A leading mobile game company has a mission-critical server that is currently down in AWS. Which AWS Support plan allows the administrator to contact technical support immediately?",
            "choices": ["Developer", "Enterprise On-Ramp", "Business", "Enterprise"],
            "answer": [3],
        },
        {
            "id": 19,
            "question": "A startup plans to build a data lake using Amazon S3 as the primary storage platform. Which options should be used?",
            "choices": [
                "Expose data to the internet",
                "Ingest data from the internet",
                "Creating S3 bucket policies",
                "Modifying S3 event notifications",
                "Setting up S3 lifecycle policies",
            ],
            "answer": [4],
        },
        {
            "id": 20,
            "question": "Which of the following allows you to categorize and track your AWS costs on a detailed level?",
            "choices": ["Cost allocation tags", "Consolidated billing", "AWS Budgets", "Amazon Aurora Backtrack"],
            "answer": [0],
        },
        {
            "id": 21,
            "question": "Which of the following is true regarding the AWS Cost and Usage Report?",
            "choices": [
                "Provides you with granular data about your AWS costs and usage",
                "Lets you set custom cost and usage budgets that alert you when thresholds are exceeded",
                "Helps you visualize, understand, and manage your AWS costs and usage over time via an intuitive interface",
                "Allows you to load your cost and usage information into Amazon Athena, Amazon Redshift, and AWS QuickSight",
                "Provides you a dashboard that helps you view the status of your month-to-date AWS expenditure and provides access to other cost management products",
            ],
            "answer": [0, 3],
        },
        {
            "id": 22,
            "question": "You have an Amazon Linux EC2 instance running for an hour and thirty minutes. How will AWS bill you in terms of usage?",
            "choices": [
                "You will be billed for an hour and thirty minutes according to the per-second billing rule",
                "You will only be billed for an hour according to the hourly billing rule",
                "You will be billed for one hour and thirty minutes according to the hourly billing rule",
                "You will be billed for an hour and twenty-nine minutes according to the per-second billing rule",
            ],
            "answer": [0],
        },
        {
            "id": 23,
            "question": "Which payment plan will give you the largest discount when purchasing EC2 Reserved Instances?",
            "choices": [
                "Partial upfront payment for a 3-year term purchase",
                "Partial upfront payment for a 1-year term purchase",
                "All upfront payment for a 1-year term purchase",
                "All upfront payment for a 3-year term purchase",
            ],
            "answer": [3],
        },
        {
            "id": 24,
            "question": "Which of the following Amazon EC2 instance types is the most suitable and cost-effective if the customer will be running mission-critical workloads continuously for a whole year?",
            "choices": ["On-Demand Instance", "Reserved Instance", "Spot Instance", "Dedicated Instance"],
            "answer": [1],
        },
        {
            "id": 25,
            "question": "A customer is choosing the best AWS support plan which includes a designated Technical Account Manager. Which of the following should they choose?",
            "choices": ["Enterprise On-Ramp", "Developer", "Business", "Enterprise"],
            "answer": [3],
        },
        {
            "id": 26,
            "question": "Which of the following is the most cost-effective instance purchasing option for hosting an application which will run non-interruptible workloads for a period of three years?",
            "choices": [
                "Amazon EC2 Spot Instances",
                "Amazon EC2 Standard Reserved Instances",
                "Amazon EC2 On-Demand Instances",
                "Amazon EC2 Convertible Reserved Instances",
            ],
            "answer": [1],
        },
        {
            "id": 27,
            "question": "Which of the following provides you access to Reserved Instance purchase recommendations based on your past usage and indicates potential cost savings compared to On-Demand usage?",
            "choices": ["AWS Budgets", "AWS Cost Explorer", "AWS Billing Dashboard", "AWS Cost and Usage Report"],
            "answer": [1],
        },
        {
            "id": 28,
            "question": "Which of the following provides the most granular data about AWS costs and usage and can also load that information into Amazon Athena, Amazon Redshift, and Amazon QuickSight?",
            "choices": ["AWS Cost and Usage Report", "AWS Budgets", "Consolidated billing", "AWS Cost Explorer"],
            "answer": [0],
        },
        {
            "id": 29,
            "question": "A company is using multiple AWS services to host its application and wants to ensure the environment is optimized by adhering to AWS best practices. Which service reviews resources and makes recommendations to lower expenditures, improve system performance, and increase security?",
            "choices": ["AWS Budgets", "AWS Trusted Advisor", "AWS Cost Explorer", "Amazon Inspector"],
            "answer": [1],
        },
        {
            "id": 30,
            "question": "Among the following payment options, which can be chosen when purchasing a Standard or Convertible Reserved Instance?",
            "choices": [
                "All upfront payment",
                "Bill-as-you-go payment",
                "Deferred payment",
                "Reserved payment",
                "No upfront payment",
                "Partial upfront payment",
            ],
            "answer": [0, 4, 5],
        },
    ],
}


# =============================
# SESSION STATE
# =============================


def initialize_session_state() -> None:
    defaults = {
        "page": "menu",
        "selected_exam": "Cloud Concepts",
        "q_index": 0,
        "answers": {},
        "show_answer": False,
        "start_time": None,
        "duration": 1800,
        "failed_questions": {},
        "is_revision_mode": False,
        "exam_mode": "normal",
        "questions_working": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def format_time(seconds: int) -> str:
    minutes, remaining = divmod(seconds, 60)
    return f"{minutes}:{remaining:02d}"


def build_working_questions() -> list[dict]:
    base_questions = EXAMS[st.session_state.selected_exam]

    if st.session_state.is_revision_mode:
        failed_ids = st.session_state.failed_questions.get(st.session_state.selected_exam, [])
        base_questions = [q for q in base_questions if q["id"] in failed_ids]

    if st.session_state.exam_mode == "normal":
        return base_questions

    shuffled_questions = []
    for q in base_questions:
        idx = list(range(len(q["choices"])))
        random.shuffle(idx)

        shuffled_questions.append(
            {
                "id": q["id"],
                "question": q["question"],
                "choices": [q["choices"][i] for i in idx],
                "answer": [idx.index(i) for i in q["answer"]],
            }
        )

    random.shuffle(shuffled_questions)
    return shuffled_questions


def calculate_results(questions: list[dict], answers: dict[int, list[int]]) -> tuple[int, list[int]]:
    score = 0
    failed_ids = []

    for i, question in enumerate(questions):
        user_answer = answers.get(i, [])
        if sorted(user_answer) == sorted(question["answer"]):
            score += 1
        else:
            failed_ids.append(question["id"])

    return score, failed_ids


def show_results(score: int, total: int, failed_ids: list[int]) -> None:
    st.success(f"🎉 Score final : {score} / {total}")

    if failed_ids:
        st.warning(f"⚠️ {len(failed_ids)} question(s) ratée(s) sauvegardée(s) pour révision")
    else:
        st.balloons()
        st.info("🏆 Parfait ! Toutes les réponses sont correctes !")


def finish_exam(questions: list[dict]) -> None:
    score, failed_ids = calculate_results(questions, st.session_state.answers)

    st.session_state.failed_questions[st.session_state.selected_exam] = failed_ids
    show_results(score, len(questions), failed_ids)

    if st.button("Retour au menu"):
        st.session_state.page = "menu"
        st.rerun()

    st.stop()


initialize_session_state()

# =============================
# MENU
# =============================

if st.session_state.page == "menu":
    st.title("🎓 AWS CCP Trainer")

    st.subheader("📚 Choisir un examen")
    selected = st.radio(" ", list(EXAMS.keys()), index=0)
    st.session_state.selected_exam = selected

    st.subheader("⚙️ Réglages")
    minutes = st.number_input(
        "Durée de l'examen (minutes)",
        min_value=5,
        max_value=180,
        value=30,
    )
    st.session_state.duration = minutes * 60

    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶️ Démarrer l'examen", use_container_width=True):
            st.session_state.page = "exam"
            st.session_state.q_index = 0
            st.session_state.answers = {}
            st.session_state.show_answer = False
            st.session_state.start_time = time.time()
            st.session_state.is_revision_mode = False
            st.session_state.questions_working = None
            st.rerun()

    with col2:
        failed_count = len(st.session_state.failed_questions.get(selected, []))

        if failed_count > 0:
            if st.button(f"🔄 Réviser ({failed_count} questions)", use_container_width=True):
                st.session_state.page = "exam"
                st.session_state.q_index = 0
                st.session_state.answers = {}
                st.session_state.show_answer = False
                st.session_state.start_time = time.time()
                st.session_state.is_revision_mode = True
                st.session_state.questions_working = None
                st.rerun()
        else:
            st.button("🔄 Réviser (0 questions)", disabled=True, use_container_width=True)

    st.markdown("---")
    st.subheader("🧪 Mode d'examen")

    colx, coly = st.columns(2)
    with colx:
        if st.button("🧠 Examen normal", use_container_width=True):
            st.session_state.exam_mode = "normal"
            st.session_state.questions_working = None
            st.success("Mode normal activé")

    with coly:
        if st.button("🔀 Examen mélangé", use_container_width=True):
            st.session_state.exam_mode = "shuffled"
            st.session_state.questions_working = None
            st.success("Mode mélangé activé")

    st.markdown("---")
    st.subheader("📊 Statistiques")

    has_failed = False
    for exam_name, questions in st.session_state.failed_questions.items():
        if questions:
            st.write(f"**{exam_name}** : {len(questions)} question(s) à réviser")
            has_failed = True

    if not has_failed:
        st.info("Aucune question ratée pour le moment. Bon courage ! 💪")

    if st.button("🗑️ Réinitialiser toutes les révisions"):
        st.session_state.failed_questions = {}
        st.rerun()


# =============================
# EXAM
# =============================

if st.session_state.page == "exam":
    if st.session_state.questions_working is None:
        st.session_state.questions_working = build_working_questions()

    QUESTIONS = st.session_state.questions_working
    TOTAL = len(QUESTIONS)

    if st.session_state.q_index >= TOTAL:
        st.session_state.q_index = 0

    if TOTAL == 0:
        st.warning("Aucune question à réviser !")
        if st.button("Retour au menu"):
            st.session_state.page = "menu"
            st.rerun()
        st.stop()

    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, st.session_state.duration - elapsed)
    st.caption(f"⏱️ Temps restant : {format_time(remaining)}")

    if remaining == 0:
        st.warning("⏰ Temps écoulé !")
        finish_exam(QUESTIONS)

    q = QUESTIONS[st.session_state.q_index]

    exam_title = st.session_state.selected_exam
    if st.session_state.is_revision_mode:
        exam_title += " (Révision)"

    st.title(exam_title)
    st.subheader(f"Question {st.session_state.q_index + 1} / {TOTAL}")
    st.progress((st.session_state.q_index + 1) / TOTAL)

    # =============================
    # ANSWER INPUT
    # =============================

    if len(q["answer"]) == 1:
        saved_answer = st.session_state.answers.get(st.session_state.q_index, [])
        default_index = saved_answer[0] if isinstance(saved_answer, list) and saved_answer else None

        choice_key = f"radio_{st.session_state.q_index}"
        selected_choice = st.radio(
            q["question"],
            options=range(len(q["choices"])),
            format_func=lambda x: q["choices"][x],
            index=default_index,
            key=choice_key,
        )
        st.session_state.answers[st.session_state.q_index] = (
            [selected_choice] if selected_choice is not None else []
        )
    else:
        st.markdown(q["question"])
        saved_answer = st.session_state.answers.get(st.session_state.q_index, [])
        selected_indexes = []

        for i, choice in enumerate(q["choices"]):
            checked = i in saved_answer
            checkbox_key = f"check_{st.session_state.q_index}_{i}"
            if st.checkbox(choice, value=checked, key=checkbox_key):
                selected_indexes.append(i)
        st.session_state.answers[st.session_state.q_index] = selected_indexes

    # =============================
    # SHOW ANSWER
    # =============================

    if st.button("💡 Afficher la bonne réponse"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        for index in q["answer"]:
            st.markdown(
                (
                    "<div style='background-color:#d4edda;"
                    "padding:0.5rem 0.75rem;"
                    "border-radius:0.5rem;"
                    "margin-bottom:0.5rem;'>"
                    f"{q['choices'][index]}"
                    "</div>"
                ),
                unsafe_allow_html=True,
            )

    # =============================
    # NAVIGATION
    # =============================

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.session_state.q_index > 0:
            if st.button("← Précédent"):
                st.session_state.q_index -= 1
                st.session_state.show_answer = False
                st.rerun()

    with col2:
        if st.button("🏠 Menu"):
            st.session_state.page = "menu"
            st.rerun()

    with col3:
        if st.session_state.q_index < TOTAL - 1:
            if st.button("Suivant →"):
                st.session_state.q_index += 1
                st.session_state.show_answer = False
                st.rerun()
        else:
            if st.button("✅ Terminer"):
                finish_exam(QUESTIONS)

    # =============================
    # MOBILE PAGINATION
    # =============================

    st.markdown("---")
    st.markdown("**🧭 Navigation rapide**")

    column_count = min(TOTAL, 10)
    cols = st.columns(column_count)
    for i in range(TOTAL):
        col_idx = i % column_count
        with cols[col_idx]:
            answered = i in st.session_state.answers
            label = f"{'✓' if answered else ''}{i + 1}"

            if st.button(
                label,
                key=f"nav_{i}",
                use_container_width=True,
            ):
                st.session_state.q_index = i
                st.session_state.show_answer = False
                st.rerun()
