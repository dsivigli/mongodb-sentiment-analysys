# Detect sentiment from customer reviews with Amazon Comprehend and MongoDB Atlas

This example application creates and Amazon EventBridge event bus, an associated event rule and a lambda function. The lambda function calls Amazon Comprehend API to perform sentiment analysis on the input and return a message. 


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 12.x installed](https://nodejs.org/en/download/)

  
## Installation Instructions
1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

2. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

3. Create partner event source by linking AWS with EventBridge partner (e.g. using MongoDB Atlas DB Trigger integration with EventBridge).

4. Create a new directory, navigate to that directory in a terminal and using command line clone the repository: ```git clone https://github.com/dsivigli/mongodb-sentiment-analysys```.
5. From the command line, run:
```
cd ./mongodb-sentiment-analysys
sam deploy --guided

Choose a stack name, input the partner event source name, and allow SAM to create the event bus, rule, and Lambda function.

## How it works
* When a customer review is inserted in the MongoDB collection an event is generated and it triggers an event in the Amazon EventBridge event bus
* The EventBridge rule specified in `template.yaml` filters the events based upon the criteria in the `EventPattern` section.
* When the rule validates an event, it invokes the Lambda function. This will invoke Amaozn Comprehend API to perform sentiment analysis on the review. The result is returned. This information can be used to trigger other actions, it can be logged, it can be saved in another MongoDB collection to perform other analysis.


==============================================


Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.
