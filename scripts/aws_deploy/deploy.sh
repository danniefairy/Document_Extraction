#!/bin/bash

aws cloudformation create-stack --stack-name exampleStack --template-body file://scripts/aws_deploy/template.json --parameters ParameterKey=KeyExample,ParameterValue=KeyExample
