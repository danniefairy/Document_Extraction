#!/bin/bash

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws cloudformation create-stack --stack-name exampleStack --template-body file://scripts/aws_deploy/template.json --parameters ParameterKey=KeyExample,ParameterValue=KeyExample